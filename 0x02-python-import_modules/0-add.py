#!/usr/bin/python3
a = 1
b = 2
# Importing add function from add_0.py
from add_0 import add

# Using string formatting to print the result
print("{} + {} = {}".format(a, b, add(a, b)))
