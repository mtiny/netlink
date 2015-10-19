'''
Created on 21 aug. 2015

@author: menno
'''

import struct
'''
from netlink.h
'''
NLM_F_ROOT = 0x100
NLM_F_REQUEST = 1
NLM_F_ACK = 4

'''
from rtnetlink.h
'''
IFI_CHANGE = 0xffffffff

'''
from if_link.h:
'''
iflatypes = [
    'IFLA_UNSPEC',
    'IFLA_ADDRESS',
    'IFLA_BROADCAST',
    'IFLA_IFNAME',
    'IFLA_MTU',
    'IFLA_LINK',
    'IFLA_QDISC',
    'IFLA_STATS',
    'IFLA_COST',
    'IFLA_PRIORITY',
    'IFLA_MASTER',
    'IFLA_WIRELESS',
    'IFLA_PROTINFO',
    'IFLA_TXQLEN',
    'IFLA_MAP',
    'IFLA_WEIGHT',
    'IFLA_OPERSTATE',
    'IFLA_LINKMODE',
    'IFLA_LINKINFO',
    'IFLA_NET_NS_PID',
    'IFLA_IFALIAS',
    'IFLA_NUM_VF',
    'IFLA_VFINFO_LIST',
    'IFLA_STATS64',
    'IFLA_VF_PORTS',
    'IFLA_PORT_SELF',
    'IFLA_AF_SPEC',
    'IFLA_GROUP',
    'IFLA_NET_NS_FD',
    'IFLA_EXT_MASK',
    'IFLA_PROMISCUITY',
    'IFLA_NUM_TX_QUEUES',
    'IFLA_NUM_RX_QUEUES',
    'IFLA_CARRIER',
    'IFLA_PHYS_PORT_ID',
    'IFLA_CARRIER_CHANGES',
    '__IFLA_MAX']

'''
from if_link.h
'''
ifla_inet_types = ['IFLA_INET_UNSPEC',
    'IFLA_INET_CONF',
    'IFLA_INET_MAX']


'''
from if_link.h
'''
ifla_inet6_types = [    'IFLA_INET6_UNSPEC',
    'IFLA_INET6_FLAGS',
    'IFLA_INET6_CONF',
    'IFLA_INET6_STATS',
    'IFLA_INET6_MCAST',
    'IFLA_INET6_CACHEINFO',
    'IFLA_INET6_ICMP6STATS',
    'IFLA_INET6_TOKEN',
    'IFLA_INET6_MAX']

'''
from if_link.h
'''
ifla_inet_types = ['IFLA_INET_UNSPEC',
    'IFLA_INET_CONF',]

'''
from netlink.h:
'''
nlmsgtypes = [
    'NLMSG_DUMMY',
    'NLMSG_NOOP',
    'NLMSG_ERROR',
    'NLMSG_DONE',
    'NLMSG_OVERRUN'
    ] + ['NLMSG_DUMMY'] * 12 + ['NLMSG_MIN_TYPE']

'''
from rtnetlink.h:
'''
rtmsgtypes = ['RTM_DUMMY'] * 16 + [
         'RTM_NEWLINK',
         'RTM_DELLINK',
         'RTM_GETLINK',
         'RTM_SETLINK',
         'RTM_NEWADDR',
         'RTM_DELADDR',
         'RTM_GETADDR',
         'RTM_DUMMY',
         'RTM_NEWROUTE',
         'RTM_DELROUTE',
         'RTM_GETROUTE',
         'RTM_DUMMY',
         'RTM_NEWNEIGH',
         'RTM_DELNEIGH',
         'RTM_GETNEIGH',
         'RTM_DUMMY',
         'RTM_NEWRULE',
         'RTM_DELRULE',
         'RTM_GETRULE',
         'RTM_DUMMY',
         'RTM_NEWQDISC',
         'RTM_DELQDISC',
         'RTM_GETQDISC',
         'RTM_DUMMY',
         'RTM_NEWTCLASS',
         'RTM_DELTCLASS',
         'RTM_GETTCLASS',
         'RTM_DUMMY',
         'RTM_NEWTFILTER',
         'RTM_DELTFILTER',
         'RTM_GETTFILTER',
         'RTM_DUMMY',
         'RTM_NEWACTION',
         'RTM_DELACTION',
         'RTM_GETACTION',
         'RTM_DUMMY',
         'RTM_NEWPREFIX',
         'RTM_DUMMY',         
         'RTM_DUMMY',
         'RTM_DUMMY',
         'RTM_DUMMY',
         'RTM_DUMMY',
         'RTM_GETMULTICAST',
         'RTM_DUMMY',
         'RTM_DUMMY',
         'RTM_DUMMY',
         'RTM_GETANYCAST',
         'RTM_DUMMY',
         'RTM_NEWNEIGHTBL',
         'RTM_DUMMY',
         'RTM_GETNEIGHTBL',
         'RTM_SETNEIGHTBL',
         'RTM_NEWNDUSEROPT',
         'RTM_DUMMY',
         'RTM_DUMMY',
         'RTM_DUMMY',
         'RTM_NEWADDRLABEL',
         'RTM_DELADDRLABEL',
         'RTM_GETADDRLABEL',
         'RTM_DUMMY',
         'RTM_DUMMY',
         'RTM_DUMMY',
         'RTM_GETDCB',
         'RTM_SETDCB',
         'RTM_NEWNETCONF',
         'RTM_DUMMY',
         'RTM_GETNETCONF',
         'RTM_DUMMY',
         'RTM_NEWMDB',
         'RTM_DELMDB',
         'RTM_GETMDB',
         'RTM_DUMMY',
         'RTM_NEWNSID',
         'RTM_DELNSID',
         'RTM_GETNSID',
         'RTM_MAX']

'''
from if_addr.h
'''
ifatypes = [
         'IFA_UNSPEC',
         'IFA_ADDRESS',
         'IFA_LOCAL',
         'IFA_LABEL',
         'IFA_BROADCAST',
         'IFA_ANYCAST',
         'IFA_CACHEINFO',
         'IFA_MULTICAST',
         'IFA_FLAGS',
         'IFA_MAX']

'''
from if_link.h:
'''
stats_attr = [
 'rx_packets',
 'tx_packets',
 'rx_bytes',
 'tx_bytes',
 'rx_errors',
 'tx_errors',
 'rx_dropped',
 'tx_dropped',
 'multicast',
 'collisions', 
 'rx_length_errors',
 'rx_over_errors',
 'rx_crc_errors',
 'rx_frame_errors',
 'rx_fifo_errors',
 'rx_missed_errors',
 'tx_aborted_errors',
 'tx_carrier_errors',
 'tx_fifo_errors',
 'tx_heartbeat_errors',
 'tx_window_errors',
 'rx_compressed',
 'tx_compressed']

'''
from rtnetlink.h:
'''
rtatypes = [
    'RTA_UNSPEC',
    'RTA_DST',
    'RTA_SRC',
    'RTA_IIF',
    'RTA_OIF',
    'RTA_GATEWAY',
    'RTA_PRIORITY',
    'RTA_PREFSRC',
    'RTA_METRICS',
    'RTA_MULTIPATH',
    'RTA_PROTOINFO',
    'RTA_FLOW',
    'RTA_CACHEINFO',
    'RTA_SESSION',
    'RTA_MP_ALGO',
    'RTA_TABLE',
    'RTA_MARK',
    'RTA_MFC_STATS',
    'RTA_MAX']

'''
from rtnetlink.h:
'''
tcatypes = [
    'TCA_UNSPEC',
    'TCA_KIND',
    'TCA_OPTIONS',
    'TCA_STATS',
    'TCA_XSTATS',
    'TCA_RATE',
    'TCA_FCNT',
    'TCA_STATS2',
    'TCA_STAB',
    'TCA_MAX']

'''
from neigbour.h:
'''
ndatypes = [
    'NDA_UNSPEC',
    'NDA_DST',
    'NDA_LLADDR',
    'NDA_CACHEINFO',
    'NDA_PROBES',
    'NDA_VLAN',
    'NDA_PORT',
    'NDA_VNI',
    'NDA_IFINDEX',
    'NDA_MASTER',
    'NDA_MAX']

'''
from if.h (struct ifmap):
'''
iflamap_attr = [
'mem_start',
'mem_end',
'base_addr', 
'irq',
'dma',
'port']

'''
from if_addr.h
'''
ifacacheinfo_attr = [
    'ifa_prefered',
    'ifa_valid',
    'cstamp',
    'tstamp']

'''
from if_addr.h:
'''
ifaddrflags = [
'IFA_DUMMY',
'IFA_F_SECONDARY',
'IFA_F_NODAD',
'IFA_F_OPTIMISTIC',
'IFA_F_HOMEADDRESS',
'IFA_F_DEPRECATED',
'IFA_F_TENTATIVE',
'IFA_F_PERMANENT',
'IFA_F_MANAGETEMPADDR',
'IFA_F_NOPREFIXROUTE',
'IFA_F_MCAUTOJOIN',
'IFA_F_STABLE_PRIVACY']

'''
from if_inet6.h
'''
if6addrflags = ['IF_DUMMY']*4 + ['IF_RS_SENT',
'IF_RA_RCVD',
'IF_RA_MANAGED',
'IF_RA_OTHERCONF'] + ['IF_DUMMY']*23+['IF_READY']

'''
from neigbour.h
'''
ndacacheinfo_attr = [
'ndm_confirmed',
'ndm_used',
'ndm_updated',
'ndm_refcnt']

'''
from pkt_sched.h:
'''
tcstats_attr = [
'bytes',
'packets',
'drops',
'overlimits',
'bps',
'pps',
'qlen',
'backlog']

'''
from gen_stats.h:
'''
tcastatstypes = [
    'TCA_STATS_UNSPEC',
    'TCA_STATS_BASIC',
    'TCA_STATS_RATE_EST',
    'TCA_STATS_QUEUE',
    'TCA_STATS_APP',
    'TCA_STATS_RATE_EST64',
    'TCA_STATS_MAX']

'''
from pkt_sched.h
'''

tcatbf_attr = ['rate_cell_log',
    'rate_linklayer',
    'rate_overhead',
    'rate_cell_align',
    'rate_mpu',
    'rate_rate',
    'peak_cell_log',
    'peak_linklayer',
    'peak_overhead',
    'peak_cell_align',
    'peak_mpu',
    'peak_rate',
    'limit',
    'buffer',
    'mtu']

'''
from pkt_sched.h
'''

tcasfq_attr = ['quantum',
'perturb_period',
'limit',
'divisor',
'flows',        
'depth',
'headdrop',
'red_limit',
'qth_min',
'qth_max',
'Wlog',
'Plog',
'Scell_log',
'flags',
'max_P',
'prob_drop',
'forced_drop',
'prob_mark',
'forced_mark',
'prob_mark_head',
'forced_mark_head'
              ]
'''
from pkt_sched.h
'''
tcatbftypes = ['TCA_TBF_UNSPEC',
    'TCA_TBF_PARMS',
    'TCA_TBF_RTAB',
    'TCA_TBF_PTAB',
    'TCA_TBF_RATE64',
    'TCA_TBF_PRATE64',
    'TCA_TBF_BURST',
    'TCA_TBF_PBURST',
    'TCA_TBF_MAX']

'''
from pkt_sched.h
'''

tcaredtypes = ['TCA_RED_UNSPEC',
    'TCA_RED_PARMS',
    'TCA_RED_STAB',
    'TCA_RED_MAX_P',
    'TCA_RED_MAX'
]

tcared_attr = ['limit',
'qth_min',
'qth_max',
'Wlog',
'Plog',
'Scell_log',
'flags']

tcaxstats_attr = [
'early',
'pdrop',
'other',
'marked'        ]

'''
from gen_stats.h
'''
tcabasic_attr = [
'bytes',
'packets']

tcaqueue_attr = [
'qlen',
'backlog',
'drops',
'requeues',
'overlimits']

'''
from pkt_sched.h:
'''
tcprioqopt_attr = [
'bands',
'priomap']

'''
from if.h:
'''
ifflags=[
    'IFF_UP',
    'IFF_BROADCAST',
    'IFF_DEBUG',
    'IFF_LOOPBACK',
    'IFF_POINTOPOINT',
    'IFF_NOTRAILERS',
    'IFF_RUNNING',
    'IFF_NOARP',
    'IFF_PROMISC',
    'IFF_ALLMULTI',
    'IFF_MASTER',
    'IFF_SLAVE',
    'IFF_MULTICAST',
    'IFF_PORTSEL',
    'IFF_AUTOMEDIA',
    'IFF_DYNAMIC',
    'IFF_LOWER_UP',
    'IFF_DORMANT',
    'IFF_ECHO']

rtmsg_attr = [
    'family',
    'dst_len',
    'src_len',
    'tos',
    'table',
    'protocol',
    'scope',
    'type',
    'flags']

'''
from neighbor.h
'''
ndmsg_attr = [
    'ndm_family',
    'pad1',
    'pad2',
    'ndm_ifindex',
    'ndm_state' ,
    'ndm_flags',
    'ndm_type']

tcmsg_attr = [
    'tcm_family',
    'pad1',
    'pad2',
    'tcm_ifindex',
    'tcm_handle',
    'tcm_parent',
    'tcm_info']
 
'''
from ipv6.h
'''
ipv6_devconf_attr = [
    'forwarding',
    'hop_limit',
    'mtu6',
    'accept_ra',
    'accept_redirects',
    'autoconf',
    'dad_transmits',
    'rtr_solicits',
    'rtr_solicit_interval',
    'rtr_solicit_delay',
    'force_mld_version',
    'temp_valid_lft',
    'temp_prefered_lft',
    'regen_max_retry',
    'max_desync_factor',
    'max_addresses',
    'use_tempaddr',
    'accept_ra_defrtr',
    'accept_ra_pinfo',
    'accept_ra_rtr_pref',
    'rtr_probe_interval',
    'accept_ra_rt_info_max_plen',
    'proxy_ndp',
    'accept_source_route',
    'optimistic_dad',
    'mc_forwarding',
    'disable_ipv6',
    'accept_dad',
    'force_tllao',
    'ndisc_notify',
    'mldv1_unsolicited_report_interval',
    'mldv2_unsolicited_report_interval',
    'suppress_frag_ndisc'
]

'''
from snmp.h
'''

inet6_icmpstats_attr = [
    'icmp6_mib_num',
    'icmp6_mib_inmsgs',
    'icmp6_mib_inerrors',
    'icmp6_mib_outmsgs',
    'icmp6_mib_outerrors',
    'icmp6_mib_csumerrors'
    ]

'''
from if_link.h
'''

ipv6_cacheinfo_attr = [
'max_reasm_len',
'tstamp',
'reachable_time',
'retrans_time'
]

'''
from if_link.h, include/uapi/linux/ip.h
'''

ipv4_devconf_attr = ['ipv4_devconf_forwarding',
    'ipv4_devconf_mc_forwarding',
    'ipv4_devconf_proxy_arp',
    'ipv4_devconf_accept_redirects',
    'ipv4_devconf_secure_redirects',
    'ipv4_devconf_send_redirects',
    'ipv4_devconf_shared_media',
    'ipv4_devconf_rp_filter',
    'ipv4_devconf_accept_source_route',
    'ipv4_devconf_bootp_relay',
    'ipv4_devconf_log_martians',
    'ipv4_devconf_tag',
    'ipv4_devconf_arpfilter',
    'ipv4_devconf_medium_id',
    'ipv4_devconf_noxfrm',
    'ipv4_devconf_nopolicy',
    'ipv4_devconf_force_igmp_version',
    'ipv4_devconf_arp_announce',
    'ipv4_devconf_arp_ignore',
    'ipv4_devconf_promote_secondaries',
    'ipv4_devconf_arp_accept',
    'ipv4_devconf_arp_notify',
    'ipv4_devconf_accept_local',
    'ipv4_devconf_src_vmark',
    'ipv4_devconf_proxy_arp_pvlan',
    'ipv4_devconf_route_localnet',
    'ipv4_devconf_igmpv2_unsolicited_report_interval',
    'ipv4_devconf_igmpv3_unsolicited_report_interval'
]

'''
from snmp.h
'''

ipstats_attr = [
    'ipstats_mib_num',
    'ipstats_mib_inpkts',
    'ipstats_mib_inoctets',
    'ipstats_mib_indelivers',
    'ipstats_mib_outforwdatagrams',
    'ipstats_mib_outpkts',
    'ipstats_mib_outoctets',
    'ipstats_mib_inhdrerrors',
    'ipstats_mib_intoobigerrors',
    'ipstats_mib_innoroutes',
    'ipstats_mib_inaddrerrors',
    'ipstats_mib_inunknownprotos',
    'ipstats_mib_intruncatedpkts',
    'ipstats_mib_indiscards',
    'ipstats_mib_outdiscards',
    'ipstats_mib_outnoroutes',
    'ipstats_mib_reasmtimeout',
    'ipstats_mib_reasmreqds',
    'ipstats_mib_reasmoks',
    'ipstats_mib_reasmfails',
    'ipstats_mib_fragoks',
    'ipstats_mib_fragfails',
    'ipstats_mib_fragcreates',
    'ipstats_mib_inmcastpkts',
    'ipstats_mib_outmcastpkts',
    'ipstats_mib_inbcastpkts',
    'ipstats_mib_outbcastpkts',
    'ipstats_mib_inmcastoctets',
    'ipstats_mib_outmcastoctets',
    'ipstats_mib_inbcastoctets',
    'ipstats_mib_outbcastoctets',
    'ipstats_mib_csumerrors',
    'ipstats_mib_noectpkts',
    'ipstats_mib_ect1pkts',
    'ipstats_mib_ect0pkts',
    'ipstats_mib_cepkts']

nlmsghdr_fmt = 'IHHII'
addr_fmt = '4Bi'
ifinfo_fmt = 'BBHiII'
route_fmt = '8BI'
tcmsg_fmt = 'BBHi3I'
ndmsg_fmt = 'BBHiHBB'
rtmsg_fmt = '8Bi'
rta_fmt = 'HH'

NLMSG_DONE = nlmsgtypes.index('NLMSG_DONE')
NLMSG_ERROR = nlmsgtypes.index('NLMSG_ERROR')
RTA_LEN = struct.calcsize(rta_fmt)
NL_MSG_LEN = struct.calcsize(nlmsghdr_fmt)
RT_MSG_LEN = struct.calcsize(ifinfo_fmt)
