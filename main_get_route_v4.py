'''
Created on 19 okt. 2015

@author: menno
'''

from utilities import *

if __name__ == '__main__':
    s = rtnlsock()
    s.send(rtnlmsghdr4('RTM_GETROUTE'))
    show_route_records(parse_ifrec_list(get_msg(s), rtmsg_fmt))
