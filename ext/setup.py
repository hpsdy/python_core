#!/usr/bin/env python3
from distutils.core import setup,Extension
setup(name='first_ext',ext_modules=[Extension('ext_1',sources=['ext_1.cpp'])])
