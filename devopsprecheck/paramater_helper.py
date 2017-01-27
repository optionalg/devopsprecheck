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
## Updated: Time-stamp: <2017-01-27 11:30:58>
##-------------------------------------------------------------------

__author__ = 'DennyZhang'
__email__ = 'contact@denyzhang.com'

import platform
import re
import sys

def fail_unless_root():
    return True

def fail_unless_os(supported_os_list = ['x86_64-with-Ubuntu-14.04']):
    os_platform = platform.platform()
    for supprted_os in supported_os_list:
        m = re.search(supprted_os, os_platform)
        if m is not None:
            return True
    print "ERROR: unsupported OS: %s." % (os_platform)
    sys.exit(1)

# TODO: parameters check
# function fail_unless_nubmer() {
# function ensure_variable_isset() {
# function is_ip() {
# function is_tcp_port() {
# function check_string_schema() {
# function check_list_fields() {
# function ip_ssh_reachable() {
# function ip_list_ping_reachable() {
# function enforce_ssh_check() {
# function enforce_ip_ping_check() {
# function parse_json() {
# function verify_ssh_key_file() {
# function verify_comon_jenkins_parameters() {
#
# function source_string() {
# function remove_hardline() {
# function string_strip_whitespace() {
# function string_strip_comments() {
# function parse_ip_from_string() {
# function caculate_date() {
# function last_monday() {
## File : paramater_helper.py ends
