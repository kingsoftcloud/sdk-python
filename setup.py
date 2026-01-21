# -*- coding: utf-8 -*-
import os
import io
from setuptools import setup, find_packages
import ksyun

ROOT = os.path.dirname(__file__)

with io.open(os.path.join(ROOT, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='kingsoftcloud-sdk-python',
    version=ksyun.__version__,
    description='Kingsoft Cloud SDK for Python',
    long_description=long_description,
    author='Kingsoft Cloud',
    maintainer_email="fengyikai@kingsoft.com",
    url='https://github.com/ksyun/ksyun-sdk-python',
    packages=find_packages(exclude=["tests*"]),
    scripts=[],
    install_requires=[
        "requests>=2.20.0,<3.0.0",
        "requests-aws4auth>=1.0.1,<2.0.0",
        "six>=1.10.0",
    ],
    license="Apache License 2.0",
    platforms='any',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.14',
    ],
)
