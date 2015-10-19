'''
Created on 31 aug. 2015

@author: menno

'''

import sys, struct, utilities

if __name__ == '__main__':
    ifnr = int(sys.argv [1])
    data = [int(x, 16) for x in sys.argv[2].split(':')]
    #data = (sys.argv[2] + '\0').encode('ascii')
    #data = struct.pack('I', int(sys.argv[2]))
    s = utilities.rtnlsock()
    hdr = utilities.nlmsghdr(len(data), 'RTM_NEWLINK')
    #flag = utilities.iff_flags('IFF_UP', 'IFF_MULTICAST')
    ifinfo = utilities.ifinfomsg(ifnr, 0)
    rta = utilities.rta(len(data), 'IFLA_ADDRESS')
    data = struct.pack('B' * len(data), *data)
    msg = hdr + ifinfo + rta + data
    s.send(msg)
    s.recv(512)
