#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.CountySelect',
      version='0.0.2',
      description=('A basic package to find a county by city/town in Massachusetts.'),
      long_description="## Overview\r\nThis package provides a way to ask the user's home county by city. \r\nIt reads the provided city and attempts to match with the closest county.\r\n\r\n## Usage\r\nThe package has a single file, counties.yml. To use it you should first include the question:\r\n```yaml\r\ninclude:\r\n  - docassemble.CountySelect:counties.yml\r\n```\r\nThen, you can request the variable `county` and the question will be provided. \r\nSince there are no mandatory blocks, you should make sure to order the code appropriately.\r\nFor example, you can say:\r\n```yaml:\r\ncode: |\r\n  need(some_other_variable, county)\r\n```\r\nYou can also set the `city` value to provide a default city.",
      long_description_content_type='text/markdown',
      author='Kendall Garner',
      author_email='garner.k@outlook.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/CountySelect/', package='docassemble.CountySelect'),
     )

