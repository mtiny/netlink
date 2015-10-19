'''
Created on 20 aug. 2015

@author: menno
'''
from socket import socket, AF_NETLINK, SOCK_RAW, NETLINK_ROUTE, AF_INET, AF_INET6, AF_UNSPEC
from struct import pack, unpack, calcsize
from constants import *
from ipaddress import IPv4Address, IPv6Address

BUFSIZE  = 10000

def itob (x):
    '''
    convert integer to list of bits
    '''
    if x in [0, 1]:
        return [x]
    else:
        return [x%2] + itob (x>>1)


def align(x):
    '''
    replaces RTA_ALIGN macro from rtnetlink.h
    '''
    return 4*((x+3)//4)

def bytes_to_data(fmt, table, l):
    '''
    convert list of bytes to human-readable data, given format string and table
    '''
    return {x:y for (x, y) in zip(table, list(unpack(fmt, l)))}

def rtnlsock():
    '''
    creates netlink socket
    '''
    return socket(AF_NETLINK, SOCK_RAW, NETLINK_ROUTE)

def nlmsghdr(length, cmd):
    '''
    see netlink.h
    '''
    return pack(nlmsghdr_fmt, NL_MSG_LEN + RT_MSG_LEN + RTA_LEN + length, rtmsgtypes.index (cmd), NLM_F_ROOT | NLM_F_REQUEST, 0, 0)

def rtnlmsghdr4(cmd):
    '''
    see rtnetlink.h nlmsghdr + rtgenmsg
    '''
    return pack(nlmsghdr_fmt+'B',calcsize(nlmsghdr_fmt + 'B'), rtmsgtypes.index (cmd), NLM_F_ROOT | NLM_F_REQUEST, 0, 0, AF_INET)

def rtnlmsghdr6(cmd):
    '''
    see rtnetlink.h nlmsghdr + rtgenmsg
    '''
    return pack(nlmsghdr_fmt+'B',calcsize(nlmsghdr_fmt + 'B'), rtmsgtypes.index (cmd), NLM_F_ROOT | NLM_F_REQUEST, 0, 0, AF_INET6)

def ifinfomsg(ifnr, flags):
    return pack(ifinfo_fmt, AF_UNSPEC, 0, 0, ifnr, flags, IFI_CHANGE)
    
def rta(length, cmd):
    return pack(rta_fmt, RTA_LEN + length, iflatypes.index(cmd))

def iff_flags(*stringlist):
    flag = 0
    for strng in stringlist: 
        flag |= 1<<(ifflags).index(strng)
    return flag

def get_msg (s):
    '''
    reads all records from netlink response
    '''
    l = s.recv (BUFSIZE)
    msghdr = strip_record(l, nlmsghdr_fmt)
    length = msghdr[0]
    while msghdr[1] not in [NLMSG_ERROR, NLMSG_DONE]:
        while len(l) < length + calcsize(nlmsghdr_fmt):
            l += s.recv (BUFSIZE)
        msghdr = strip_record (l[length:], nlmsghdr_fmt)
        length += msghdr[0]
    return l
    
def strip_record (l, fmt):
    '''
    gets first record from l
    '''
    rec = unpack(fmt, l[: calcsize(fmt)])
    return rec

def parse_ifrec_list (l, fmt):
    '''
    turns netlink response into a list op tuples:
    (message header, address, link  etc. record, raw data for rta records)
    fmt is format of record following msghdr, i.e. ifinfo_fmt etc.
    '''

    msghdr = strip_record(l, nlmsghdr_fmt)
    if msghdr[1] in [NLMSG_ERROR, NLMSG_DONE] :
        return [(msghdr, [])]
    else:
        return [(msghdr, strip_record(l[calcsize(nlmsghdr_fmt):], fmt), 
                 l[calcsize(nlmsghdr_fmt + fmt):msghdr[0]])] + parse_ifrec_list(l[msghdr[0]:], fmt)
    
def parse_ifrec (l):
    '''
    turns netlink data into list of rta records + corresponding binary data
    '''
    if len(l) == 0:
        return []
    else:
        rta = strip_record(l, rta_fmt)
        rta_len = rta[0]
        return [(rta, l[calcsize(rta_fmt) : rta_len])] + parse_ifrec(l[align(rta_len):])
    
def bytes_to_addr (l):
    '''
    prints hardware address from raw data
    '''
    return ':'.join([format(x, '02x') for x in l])

def bytes_to_ipaddr (l):
    '''
    prints IP address from raw data
    '''
    if len(l)==16:
        return IPv6Address(l)
    elif len(l)==4:
        return IPv4Address(l)
    else:
        return ('UNKNOWN ADDRESS FORMAT')

def show_rta_link (rta, l):
    '''
    turns link rta data into human-readable form
    '''
    rta_type = rta[1]
    fieldname = iflatypes[rta_type]
    if fieldname in ['IFLA_ADDRESS', 'IFLA_BROADCAST']:
        print (fieldname, bytes_to_addr(l))
    elif fieldname in ['IFLA_IFNAME', 'IFLA_QDISC']:
        print (fieldname, l.decode('ascii'))
    elif fieldname in ['IFLA_MTU', 'IFLA_TXQLEN', 'IFLA_GROUP', 'IFLA_PROMISCUITY', 'IFLA_TXQLEN', 
                       'IFLA_NUM_TX_QUEUES', 'IFLA_NUM_RX_QUEUES', 'IFLA_CARRIER_CHANGES']:
        print (fieldname, unpack('i', l)[0])
    elif fieldname in ['IFLA_OPERSTATE', 'IFLA_LINKMODE', 'IFLA_CARRIER']:
        print (fieldname, l[0])
    elif fieldname in ['IFLA_STATS']:
        print (fieldname, bytes_to_data('23I', stats_attr, l))
    elif fieldname in ['IFLA_STATS64']:
        print (fieldname, bytes_to_data('23Q', stats_attr, l))
    elif fieldname in ['IFLA_MAP']:
        print (fieldname,bytes_to_data('3Q8B', iflamap_attr, l))
    elif fieldname in ['IFLA_AF_SPEC']:
        print (fieldname)
        for e in parse_ifrec(l):
            address_family = e[0][1]
            print('adress family: {}'.format(address_family))
            for p in parse_ifrec(e[1]):
                rta = p[0]
                rta_type = rta[1]
                l = p[1]
                if address_family==AF_INET:
                    fieldname = ifla_inet_types[rta_type]
                else:
                    fieldname = ifla_inet6_types[rta_type]
                if fieldname in ['IFLA_INET6_CONF']:
                    print (fieldname, bytes_to_data('33I', ipv6_devconf_attr, l))
                elif fieldname in ['IFLA_INET6_TOKEN']:
                    print (fieldname, bytes_to_ipaddr(l))                    
                elif fieldname in ['IFLA_INET6_CACHEINFO']:
                    print (fieldname, bytes_to_data('4I', ipv6_cacheinfo_attr, l))                    
                elif fieldname in ['IFLA_INET6_ICMP6STATS']:
                    print (fieldname, bytes_to_data('6Q', inet6_icmpstats_attr, l))                    
                elif fieldname in ['IFLA_INET_CONF']:
                        print (fieldname, bytes_to_data('28I', ipv4_devconf_attr, l))
                elif fieldname in ['IFLA_INET6_STATS']:
                        print (fieldname, bytes_to_data('36Q', ipstats_attr, l))
                elif fieldname in ['IFLA_INET6_FLAGS']:
                    val = unpack('I', l)[0]
                    bits = itob(val)
                    print (fieldname, [if6addrflags[i] for i in range(len(bits)) if bits[i] == 1])
                else:
                    print (fieldname, l)
    elif fieldname in ['IFLA_PROTINFO']:
        print (fieldname)
        for p in parse_ifrec(l):
            rta = p[0]
            rta_type = rta[1]
            l = p[1]
            fieldname = ifla_inet6_types[rta_type]
            if fieldname in ['IFLA_INET6_CONF']:
                print (fieldname, bytes_to_data('33I', ipv6_devconf_attr, l))
            elif fieldname in ['IFLA_INET6_TOKEN']:
                print (fieldname, bytes_to_ipaddr(l))                    
            elif fieldname in ['IFLA_INET6_CACHEINFO']:
                print (fieldname, bytes_to_data('4I', ipv6_cacheinfo_attr, l))                    
            elif fieldname in ['IFLA_INET6_ICMP6STATS']:
                print (fieldname, bytes_to_data('6Q', inet6_icmpstats_attr, l))                    
            elif fieldname in ['IFLA_INET_CONF']:
                print (fieldname, bytes_to_data('28I', ipv4_devconf_attr, l))
            elif fieldname in ['IFLA_INET6_FLAGS']:
                val = unpack('I', l)[0]
                bits = itob(val)
                print (fieldname, [if6addrflags[i] for i in range(len(bits)) if bits[i] == 1])
            elif fieldname in ['IFLA_INET6_STATS']:
                print (fieldname, bytes_to_data('36Q', ipstats_attr, l))
            else:
                print (fieldname, l)
    else:        
        print (fieldname, len(l), parse_ifrec(l))
    
def show_rta_addr (rta, l):
    '''
    turns address rta data into human-readable form
    '''
    rta_type = rta[1]
    fieldname = ifatypes[rta_type]
    if fieldname in ['IFA_ADDRESS', 'IFA_LOCAL', 'IFA_BROADCAST']:
        print (fieldname, bytes_to_ipaddr(l))
    elif fieldname in ['IFA_LABEL']:
        print (fieldname, l.decode('ascii'))
    elif fieldname in ['IFA_CACHEINFO']:
        print (fieldname, bytes_to_data('4I', ifacacheinfo_attr, l))
    elif fieldname in ['IFA_FLAGS']:
        val = unpack('I', l)[0]
        bits = itob(val)
        print (fieldname, [ifaddrflags[i] for i in range(len(bits)) if bits[i] == 1])
    else:        
        print (fieldname, l)
        
def show_rta_route (rta, l):
    '''
    turns route rta data into human-readable form
    '''
    rta_type = rta[1]
    fieldname = rtatypes[rta_type]
    if fieldname in ['RTA_DST', 'RTA_PREFSRC', 'RTA_GATEWAY']:
        print (fieldname, bytes_to_ipaddr(l))
    elif fieldname in ['RTA_OIF', 'RTA_TABLE', 'RTA_PRIORITY', 'RTA_MP_ALGO']:
        print (fieldname, unpack('I', l)[0])
    elif fieldname in ['RTA_CACHEINFO']:
        print (fieldname, bytes_to_data('2Ii5I', rta_cacheinfo_attr, l))
    else:
        print (fieldname, l)

def show_rta_qdiscs_nested (rta, l):
    '''
    turns qdiscs nested rta data into human-readable form
    '''
    rta_type = rta[1]
    fieldname = tcastatstypes[rta_type]
    if fieldname in ['TCA_STATS_BASIC']:
        l = l[:-4] #strip pad byte
        print (fieldname, bytes_to_data('QI', tcabasic_attr, l))
    elif fieldname in ['TCA_STATS_QUEUE']:
        print (fieldname, bytes_to_data('5I', tcaqueue_attr, l))
    else:        
        print (fieldname, l)
        
def show_rta_qdiscs_red (rta, l):
    rta_type = rta[1]
    fieldname = tcaredtypes[rta_type]
    if fieldname in ['TCA_RED_PARMS']:
        print (fieldname, bytes_to_data ('3I4B', tcared_attr, l))
    elif fieldname in ['TCA_RED_MAX_P']:
        print (fieldname, 'probability: {:0.2f}'.format(unpack('I', l)[0]/2**32))
        
def show_rta_qdiscs_tbf (rta, l):
    rta_type = rta[1]
    fieldname = tcatbftypes[rta_type]
    print (fieldname, bytes_to_data (2*'BBHhHi'+'3I', tcatbf_attr, l))
        
def show_rta_qdiscs (rta, l):
    '''
    turns qdiscs rta data into human-readable form
    '''
    rta_type = rta[1]
    fieldname = tcatypes[rta_type]
    if fieldname in ['TCA_UNSPEC', 'TCA_KIND']:
        print (fieldname, l.decode('ascii'))
    elif fieldname in ['TCA_OPTIONS']:
        if len(l)==20:
            print (fieldname, {x:y for (x, y) in zip(tcprioqopt_attr, [unpack('I', l[:4])[0],
                           tuple(unpack('16B', l[4:]))])})
        elif len(l)==40:
            print(fieldname)
            p=parse_ifrec(l)
            show_rta_qdiscs_tbf (p[0][0], p[0][1])
        elif len(l)==72:
            print(fieldname, bytes_to_data('Ii8I4B7I', tcasfq_attr, l))
        elif len(l)==28:
            print(fieldname)
            p=parse_ifrec(l)
            show_rta_qdiscs_red(p[0][0], p[0][1])
            show_rta_qdiscs_red(p[1][0], p[1][1])
        elif len(l)==4:
            print(fieldname, 'limit', unpack('I', l)[0])
        else:
            print (fieldname, len(l), l)
    elif fieldname in ['TCA_STATS']:
        print (fieldname, bytes_to_data('Q8I', tcstats_attr, l))
    elif fieldname in ['TCA_XSTATS', 'TCA_STATS_APP']:
        if len(l)==16:
            print (fieldname, bytes_to_data('4I', tcaxstats_attr, l))
        else:
            print(fieldname, l)
    elif fieldname in ['TCA_STATS2']:
        print (fieldname)
        p = parse_ifrec(l)
        show_rta_qdiscs_nested(p[0][0], p[0][1])
        show_rta_qdiscs_nested(p[1][0], p[1][1])
    else:        
        print (fieldname, l)
        
def show_rta_neigh (rta, l):
    '''
    turns neighbor detect rta data into human-readable form
    '''
    rta_type = rta[1]
    fieldname = ndatypes[rta_type]
    if fieldname in ['NDA_DST']:
        print (fieldname, bytes_to_ipaddr(l))
    elif fieldname in ['NDA_LLADDR']:
        print (fieldname, bytes_to_addr(l))        
    elif fieldname in ['NDA_PROBES']:
        print (fieldname, unpack('i', l)[0])
    elif fieldname in ['NDA_CACHEINFO']:
        print (fieldname, bytes_to_data('4I', ndacacheinfo_attr, l))
    else:        
        print (fieldname, l)
        
def show_rta_default (rta, l):
    print (rta, l)
    
def show_ififo (ififo):
    print('interface index: ',ififo[3])
    flags = itob(ififo[4])
    print ('flags: ', [ifflags[i] for i in range(len(flags)) if flags[i]==1])
    
def show_link_records (l):
    for msg in l:
        header = msg[0]
        headertype = header[1]
        if headertype not in [NLMSG_ERROR, NLMSG_DONE]:
            ififo = msg[1]
            show_ififo(ififo)
            ifrec = msg[2]
            for (rta_record, rta_data) in parse_ifrec(ifrec):
                show_rta_link(rta_record, rta_data)
                
def show_ifaddr (ifaddr):
    print('interface index: ',ifaddr[4])
    flags = itob(ifaddr[2])
    print ('flags: ', [ifaddrflags[i] for i in range(len(flags)) if flags[i]==1])

def show_address_records (l):
    for msg in l:
        header = msg[0]
        headertype = header[1]
        if headertype not in [NLMSG_ERROR, NLMSG_DONE]:
            ifaddr = msg[1]
            show_ifaddr(ifaddr)
            ifrec = msg[2]
            for (rta_record, rta_data) in parse_ifrec(ifrec):
                show_rta_addr(rta_record, rta_data)

def show_route (rtmsg):
    for i in range(len(rtmsg_attr)):
        print ('{}:'.format(rtmsg_attr[i]), rtmsg[i])

def show_route_records (l):
    for msg in l:
        header = msg[0]
        headertype = header[1]
        if headertype not in [NLMSG_ERROR, NLMSG_DONE]:
            rtmsg = msg[1]
            show_route(rtmsg)
            ifrec = msg[2]
            for (rta_record, rta_data) in parse_ifrec(ifrec):
                show_rta_route(rta_record, rta_data)

def show_neigh (ndmsg):
    for i in range(len(ndmsg_attr)):
        print ('{}:'.format(ndmsg_attr[i]), ndmsg[i])

def show_neigh_records (l):
    for msg in l:
        header = msg[0]
        headertype = header[1]
        if headertype not in [NLMSG_ERROR, NLMSG_DONE]:
            ndmsg = msg[1]
            show_neigh(ndmsg)
            ifrec = msg[2]
            for (rta_record, rta_data) in parse_ifrec(ifrec):
                show_rta_neigh(rta_record, rta_data)

def show_qdiscs (tcmsg):
    for i in range(len(tcmsg_attr)):
        print ('{}:'.format(tcmsg_attr[i]), tcmsg[i])

def show_qdisc_records (l):
    for msg in l:
        header = msg[0]
        headertype = header[1]
        if headertype not in [NLMSG_ERROR, NLMSG_DONE]:
            tcmsg = msg[1]
            show_qdiscs(tcmsg)
            ifrec = msg[2]
            for (rta_record, rta_data) in parse_ifrec(ifrec):
                show_rta_qdiscs(rta_record, rta_data)
