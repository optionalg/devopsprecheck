# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : systeminfo_helper.py
## Author : Denny <denny@dennyzhang.com>
## Description :
## --
## Created : <2017-01-24>
## Updated: Time-stamp: <2017-01-27 17:17:01>
##-------------------------------------------------------------------

__author__ = 'DennyZhang'
__email__ = 'contact@denyzhang.com'

import platform
import re
import getpass

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

def fail_unless_os_username(supported_username_list = ['root']):
    current_username = getpass.getuser()
    for username in supported_username_list:
        if current_username == username:
            return True
    print "ERROR: unsupported os username: %s, supported users: %s" % \
        (current_username, str(supported_username_list))
    sys.exit(1)

# TODO: parameters check
# function python_basic_info() {
# function ruby_basic_info() {
# function nodejs_basic_info() {
# function java_basic_info() {
# function list_java_packages() {

## File : systeminfo_helper.py ends
