#!/usr/bin/env python

import setuptools

with open("README.md", "r", encoding="utf-8") as rm:
    long_description = rm.read()

setuptools.setup(name='neuralmods',
    version='0.0.1',
    description='Custom TensorFlow scripts.',
    author='Anthony Demong',
    author_email='anthony.demong@live.ca',
    url='https://github.com/atd-code/modules/',
    long_description=long_description,

    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src'),
    )
