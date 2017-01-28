# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : test_network_helper.py
## Author : Denny <denny@dennyzhang.com>
## Description :
## --
## Created : <2017-01-26>
## Updated: Time-stamp: <2017-01-27 18:09:27>
##-------------------------------------------------------------------
import sys, unittest

# import the package
import devopsprecheck

# import module
from devopsprecheck import network_helper

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.userid = "unittest"

    def tearDown(self):
        i = 1

    # TODO: enable testcase
    # def test_is_port_reachable(self):
    #     self.assertEqual(network_helper.is_port_reachable('445', '127.0.0.1'), True)
    #     self.assertEqual(network_helper.is_port_reachable('27013', '45.33.87.74'), False)
    #     self.assertEqual(network_helper.is_port_reachable('27013', '45.33.87.75'), False)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase())
    return suite
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
## File : test_network_helper.py ends
