# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File : test_paramater_helper.py
## Author : Denny <contact@dennyzhang.com>
## Description :
## --
## Created : <2017-01-26>
## Updated: Time-stamp: <2017-09-07 21:35:01>
##-------------------------------------------------------------------
import sys, unittest
# import the package
import devopsprecheck

# import module
from devopsprecheck import paramater_helper

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.userid = "unittest"

    def tearDown(self):
        i = 1

    def test_is_ip(self):
        self.assertEqual(paramater_helper.is_ip("192.168.0.1"), True)
        self.assertEqual(paramater_helper.is_ip("192.168.0.0"), False)
        self.assertEqual(paramater_helper.is_ip("192.168.0.255"), False)
        self.assertEqual(paramater_helper.is_ip("192.168.0,0"), False)

    def test_is_ip_list(self):
        msg1 ='''
# CB
192.168.0.1 # cb-01
192.168.0.2
# Elasticsearch
192.168.0.3
192.168.0.4
'''
        self.assertEqual(paramater_helper.is_ip_list(msg1), True)

        msg2 ='''
# CB
192.168.0.1 # cb-01
192.168.0.2
# Elasticsearch
192.168.0.3
192.168.0.0
'''
        self.assertEqual(paramater_helper.is_ip_list(msg2), False)

    def test_is_tcp_port(self):
        self.assertEqual(paramater_helper.is_tcp_port("48080"), True)
        self.assertEqual(paramater_helper.is_tcp_port("65536"), False)
        self.assertEqual(paramater_helper.is_tcp_port("20,"), False)

    def test_string_strip_comments(self):
        msg1 = '''
{
 "common_basic":
        {
        # service hosts: deploy service to which host
        "couchbase_hosts":["10.0.1.2", "10.0.1.3"],
        "elasticsearch_hosts":["10.0.1.4", "10.0.1.5"],
        "app_hosts":["10.0.1.6", "10.0.1.7"], # application nodes
        # mdm app nodes, which we don't want to be recognized by loadbalancer
        "app_hosts_noloadbalancer":["10.0.1.8", "10.0.1.9"],
'''
        msg1_ret = '''{
"common_basic":
{
"couchbase_hosts":["10.0.1.2", "10.0.1.3"],
"elasticsearch_hosts":["10.0.1.4", "10.0.1.5"],
"app_hosts":["10.0.1.6", "10.0.1.7"],
"app_hosts_noloadbalancer":["10.0.1.8", "10.0.1.9"],'''
        self.assertEqual(paramater_helper.string_strip_comments(msg1), msg1_ret)

    def parse_ip_from_string(self):
        msg1 = '''
 {
 # service hosts: deploy service to which host
 'couchbase_hosts':['172.17.0.2', '172.17.0.3'],
 'elasticsearch_hosts':['172.17.0.2', '172.17.0.3'],
 'mdm_hosts':['172.17.0.3', '172.17.0.4'],
 'haproxy_hosts':['172.17.0.2','172.17.0.3'],
 'nagios_server':'172.17.0.4',"
'''
        l = ['172.17.0.2', '172.17.0.3', '172.17.0.4']
        self.assertEqual(paramater_helper.parse_ip_from_string(msg1), l)

    def test_verify_ssh_keyfile_linux(self):
        self.assertEqual(paramater_helper.verify_ssh_keyfile_linux("/Users/mac/.ssh/id_rsa"), True)
        self.assertEqual(paramater_helper.verify_ssh_keyfile_linux("/Users/mac/.ssh/id_rsa_false"), False)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase())
    return suite
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
## File : test_paramater_helper.py ends
