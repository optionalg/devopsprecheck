# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : network_helper.py
## Author : Denny <denny@dennyzhang.com>
## Description :
## --
## Created : <2017-01-24>
## Updated: Time-stamp: <2017-01-27 18:18:13>
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

# TODO: parameters check
# function check_ssh_available() {
# function check_network() {
# function ip_ssh_reachable() {
# function ip_list_ping_reachable() {

## File : network_helper.py ends
