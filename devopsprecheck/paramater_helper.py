# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File : paramater_helper.py
## Author : Denny <contact@dennyzhang.com>
## Description :
## --
## Created : <2017-01-24>
## Updated: Time-stamp: <2017-09-07 21:35:01>
##-------------------------------------------------------------------

__author__ = 'DennyZhang'
__email__ = 'contact@denyzhang.com'

import sys, os
import stat
import re

def is_ip(string):
    pieces = string.split('.')
    if len(pieces) != 4: return False
    try:
        p0 = int(pieces[0])
        p1 = int(pieces[1])
        p2 = int(pieces[2])
        p3 = int(pieces[3])
        if p0 <= 0 or p0 > 255:
            return False
        if p1 < 0 or p1 > 255:
            return False
        if p2 < 0 or p2 > 255:
            return False
        if p3 <= 0 or p3 >= 255:
            return False
    except ValueError:
        return False
    return True

def is_ip_list(string):
    string_without_comment = string_strip_comments(string)
    ip_list = parse_ip_from_string(string_without_comment)
    for ip in ip_list:
        if is_ip(ip) is False:
            # print "ERROR: invalid ip: %s" % (ip)
            return False
    return True

def is_tcp_port(string):
    try:
        port = int(string)
        if port <=0 or port >= 65535:
            return False
    except ValueError:
        return False
    return True

def string_strip_comments(string, marker = '#'):
    ret = []
    for line in string.split("\n"):
        if marker in line:
            element = line[:line.index(marker)].strip()
        else:
            element = line.strip()
        if element =="":
            continue
        ret.append(element)
    return "\n".join(ret)

def parse_ip_from_string(string):
    # get ip addresses from string
    '''
     From:
 {
         # service hosts: deploy service to which host
         'couchbase_hosts':['172.17.0.2', '172.17.0.3'],
         'elasticsearch_hosts':['172.17.0.2', '172.17.0.3'],
         'mdm_hosts':['172.17.0.3', '172.17.0.4'],
         'haproxy_hosts':['172.17.0.2','172.17.0.3'],
         'nagios_server':'172.17.0.4',"
    To:
          ['172.17.0.2', '172.17.0.3', '172.17.0.4']
    '''
    string_without_comment = string_strip_comments(string)
    regexp = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    l = regexp.findall(string_without_comment)
    l = list(set(l))
    return l

################################################################################
# Only support linux
def verify_ssh_keyfile_linux(ssh_keyfile):
    if os.path.exists(ssh_keyfile) is False:
        return False
    file_mode = oct(stat.S_IMODE(os.lstat(ssh_keyfile).st_mode))
    if file_mode not in ['0600', '0400']:
        return False
    return True
################################################################################

# TODO: parameters check
# function fail_unless_nubmer() {
# function ensure_variable_isset() {
# function check_string_schema() {
# function check_list_fields() {
# function enforce_ssh_check() {
# function enforce_ip_ping_check() {
# function parse_json() {
# function verify_comon_jenkins_parameters() {
# function source_string() {
# function caculate_date() {
# function last_monday() {

## File : paramater_helper.py ends
