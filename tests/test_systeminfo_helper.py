# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File : test_systeminfo_helper.py
## Author : Denny <contact@dennyzhang.com>
## Description :
## --
## Created : <2017-01-26>
## Updated: Time-stamp: <2017-09-07 21:35:00>
##-------------------------------------------------------------------
import sys, unittest
# import the package
import devopsprecheck

# import module
from devopsprecheck import systeminfo_helper

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.userid = "unittest"

    def tearDown(self):
        i = 1

    def test_fail_unless_os(self):
        self.assertEqual(systeminfo_helper.\
                         fail_unless_os(supported_os_list = ['x86_64-with-Ubuntu-14.04',\
                                                             'Darwin-.*-x86_64']), True)

    def test_fail_unless_os_username(self):
        self.assertEqual(systeminfo_helper.fail_unless_os_username(["root", "mac"]), True)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase())
    return suite
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
## File : test_systeminfo_helper.py ends
