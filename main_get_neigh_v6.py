'''
Created on 19 okt. 2015

@author: menno                                         
'''

from utilities import *

if __name__ == '__main__':
    s = rtnlsock()
    s.send(rtnlmsghdr6('RTM_GETNEIGH'))
    show_neigh_records(parse_ifrec_list(get_msg(s), ndmsg_fmt))
