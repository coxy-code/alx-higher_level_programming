#!/usr/bin/python3
from sys import argv

if len(argv) <= 1:
    print(0)
else:
    result = sum(int(arg) for arg in argv[1:])
    print(result)
