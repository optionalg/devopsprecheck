# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : paramater_helper.py
## Author : Denny <denny@dennyzhang.com>
## Description :
## --
## Created : <2017-01-24>
## Updated: Time-stamp: <2017-01-27 15:48:25>
##-------------------------------------------------------------------

__author__ = 'DennyZhang'
__email__ = 'contact@denyzhang.com'

import platform
import re
import sys

def fail_unless_os(supported_os_list = ['x86_64-with-Ubuntu-14.04']):
    # Sample:
    # fail_unless_os(supported_os_list = ['x86_64-with-Ubuntu-14.04', 'Darwin-.*-x86_64'])
    os_platform = platform.platform()
    for supprted_os in supported_os_list:
        m = re.search(supprted_os, os_platform)
        if m is not None:
            return True
    print "ERROR: unsupported OS: %s." % (os_platform)
    sys.exit(1)

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

def fail_unless_root():
    return True

def parse_ip_from_string(string):
    # get ip addresses from string
    '''
     parse_ip_from_string
 {
         # service hosts: deploy service to which host
         'couchbase_hosts':['172.17.0.2', '172.17.0.3'],
         'elasticsearch_hosts':['172.17.0.2', '172.17.0.3'],
         'mdm_hosts':['172.17.0.3', '172.17.0.4'],
         'haproxy_hosts':['172.17.0.2','172.17.0.3'],
         'nagios_server':'172.17.0.4',"
    # -->
       #  ['172.17.0.2', '172.17.0.3', '172.17.0.4']
    '''
    string_without_comment = string_strip_comments(string)
    # TODO: update this
    l = ['172.17.0.2', '172.17.0.3', '172.17.0.4']
    return l

# TODO: parameters check
# function parse_ip_from_string() {
# function fail_unless_nubmer() {
# function ensure_variable_isset() {
# function is_tcp_port() {
# function check_string_schema() {
# function check_list_fields() {
# function enforce_ssh_check() {
# function enforce_ip_ping_check() {
# function parse_json() {
# function verify_ssh_key_file() {
# function verify_comon_jenkins_parameters() {
# function source_string() {
# function caculate_date() {
# function last_monday() {
## File : paramater_helper.py ends
