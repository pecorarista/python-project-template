#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='nyan',
      version='0.1',
      description='A template for Python projects',
      author='Miyazawa Akira',
      author_email='miyazawa-a@nii.ac.jp',
      url='https://github.com/pecorarista/python-project-template',
      package=find_packages(),
      entry_points={"console_scripts": ["nyan = nyan.cmdline:main"]})
