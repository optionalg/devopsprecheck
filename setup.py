# -*- coding: utf-8 -*-
#!/usr/bin/python
##-------------------------------------------------------------------
## @copyright 2017 DennyZhang.com
## Licensed under MIT 
##   https://raw.githubusercontent.com/DennyZhang/devops_public/master/LICENSE
##
## File : setup.py
## Author : Denny <denny@dennyzhang.com>
## Description :
## --
## Created : <2017-01-24>
## Updated: Time-stamp: <2017-01-26 16:46:27>
##-------------------------------------------------------------------
from setuptools import setup
from pypandoc import convert_file

#: Converts the Markdown README in the RST format that PyPi expects.
long_description = convert_file('README.md', 'rst')

setup(name='devopsprecheck',
      description='Python precheck package for DevOps purpose'
      long_description=long_description,
      version='0.0.1',
      url='https://github.com/DennyZhang/devopsprecheck',
      author='DennyZhang',
      author_email='contact@denyzhang.com',
      license='Apache2',
      classifiers=[
          'Development Status :: 1 - Beta',
          'Intended Audience :: DevOps enigneers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3'
      ],
      packages=['devopsprecheck'],
      install_requires=[
          # TODO
      ],
      entry_points={
          'console_scripts': [
              'encrypt=devopsprecheck.main:run'
          ]
      }
)
## File : setup.py ends
