# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='boto3_exceptions',
    version='0.1.0',
    description='Export boto3 exceptions explicitly',
    long_description=readme,
    author='Siteshen',
    author_email='blog@siteshen.com',
    url='https://github.com/siteshen/boto3_exceptions',
    license=license,
    packages=find_packages())
