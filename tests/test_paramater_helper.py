# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : test_paramater_helper.py
## Author : Denny <denny@dennyzhang.com>
## Description :
## --
## Created : <2017-01-26>
## Updated: Time-stamp: <2017-01-27 11:45:17>
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

    def test_fail_unless_os(self):
        self.assertEqual(paramater_helper.\
                         fail_unless_os(supported_os_list = ['x86_64-with-Ubuntu-14.04',\
                                                               'Darwin-.*-x86_64']), True)
    def test_is_ip(self):
        self.assertEqual(paramater_helper.is_ip("192.168.0.1"), True)
        self.assertEqual(paramater_helper.is_ip("192.168.0.0"), False)
        self.assertEqual(paramater_helper.is_ip("192.168.0.255"), False)
        self.assertEqual(paramater_helper.is_ip("192.168.0,0"), False)

    def test_fail_unless_root(self):
        self.assertEqual(paramater_helper.fail_unless_root(), True)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase())
    return suite
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
## File : test_paramater_helper.py ends
