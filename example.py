#!/usr/bin/env python

from parse_python_indentation import parse_python_indentation

with open ("test.data", "r") as input_file:
    rawdata = input_file.read()

print parse_python_indentation(rawdata)
