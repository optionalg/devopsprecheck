# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File : network_helper.py
## Author : Denny <contact@dennyzhang.com>
## Description :
## --
## Created : <2017-01-24>
## Updated: Time-stamp: <2017-09-07 21:35:01>
##-------------------------------------------------------------------

__author__ = 'DennyZhang'
__email__ = 'contact@denyzhang.com'

import socket
import urllib

def is_port_reachable(tcp_port, server_ip = '127.0.0.1'):
    # TODO: add timeout mechanism
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((server_ip, int(tcp_port)))
    return result == 0

def check_url_200(http_url):
    return urllib.urlopen(http_url).getcode() == 200

def ip_ssh_reachable(ssh_ip, ssh_port, ssh_keyfile, username):
    # TODO
    return True

# TODO: parameters check
# function check_network() {
# function ip_list_ping_reachable() {

## File : network_helper.py ends
