# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File : setup.py
## Author : Denny <contact@dennyzhang.com>
## Description :
## --
## Created : <2017-01-24>
## Updated: Time-stamp: <2017-09-07 21:35:01>
##-------------------------------------------------------------------
from setuptools import setup

# TODO
long_description = '''
Python precheck package for DevOps purpose
'''

setup(name='devopsprecheck',
      description='Python precheck package for DevOps purpose',
      long_description=long_description,
      version='0.0.2',
      url='https://github.com/DennyZhang/devopsprecheck',
      author='DennyZhang',
      author_email='contact@denyzhang.com',
      license='Apache2',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python'
      ],
      packages=['devopsprecheck'],
      install_requires=[
      ],
      entry_points={
          'console_scripts': [
              'encrypt=devopsprecheck.main:run'
          ]
      }
)
## File : setup.py ends
