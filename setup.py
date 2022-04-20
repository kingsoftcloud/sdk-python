#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
from setuptools import setup, find_packages

import ksyun

ROOT = os.path.dirname(__file__)

setup(
    name='kingsoftcloud-sdk-python',
    install_requires=["requests==2.27.1"],
    version=ksyun.__version__,
    description='Kingsoft Cloud SDK for Python',
    long_description=open('README.rst').read(),
    author='Kingsoft Cloud',
    url='https://github.com/ksyun/ksyun-sdk-python',
    maintainer_email="liuhuicheng1@kingsoft.com",
    scripts=[],
    packages=find_packages(exclude=["tests*"]),
    license="Apache License 2.0",
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
