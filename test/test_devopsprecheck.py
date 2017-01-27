# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : test_devopsprecheck.py
## Author : Denny <denny@dennyzhang.com>
## Description :
## --
## Created : <2017-01-26>
## Updated: Time-stamp: <2017-01-27 10:55:49>
##-------------------------------------------------------------------
import sys
import unittest

# import the package
import devopsprecheck

# import module
from devopsprecheck import paramater_helper

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.userid = "unittest"

    def tearDown(self):
        i = 1

    def testfun1(self):
        self.assertEqual(paramater_helper.fail_unless_root(), True)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("testfun1"))
    return suite
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
## File : test_devopsprecheck.py ends
