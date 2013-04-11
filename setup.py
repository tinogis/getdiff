#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup for simple getdiff bash script
"""
import os
import sys
from distutils.core import setup, Command
from distutils.command.clean import clean as _clean

version='0.1'

setup(name='getdiff',
      description="getdiff: get PR's diff from github",
      author='tinogis',
      author_email='afita@gisce.net',
      url='http://gisthub.com/tinogis',
      version=version,
      license='General Public Licence 2',
      long_description='''getdiff [diff_url]''',
      scripts=['bin/getdiff',],
      )
