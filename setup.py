# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='parse-python-indentation',
    version='0.0.3',
    author='Johannes Wilm',
    author_email='mail@johanneswilm.org',
    packages=find_packages(),
    url='https://github.com/johanneswilm/parse_python_indentation.py',
    license='Apache 2.0, see LICENCE.txt',
    description='python method to parse the indention of a python-style indented file.',
    long_description=long_description,
    keywords='parsing python development',

)
