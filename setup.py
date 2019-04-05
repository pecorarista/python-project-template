import os
from setuptools import setup

name = 'nyan'
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, name, '__version__.py')) as f:
    version = f.readline() \
        .split('=')[1] \
        .replace('"', '') \
        .replace("'", '') \
        .strip()

setup(name=name,
      version=version,
      description='Financial Article Generator',
      author='Miyazawa Akira',
      author_email='miyazawa-a@nii.ac.jp',
      url='https://github.com/pecorarista/python-project-template',
      packages=['nyan',
                'nyan.preprocessing'],
      entry_points={"console_scripts": ["nyan = nyan.main:main"]},
      test_suite='tests')
