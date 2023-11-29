#!/usr/bin/python3
def uppercase(s):
    result = ''
    for letter in s:
        if ord('a') <= ord(letter) <= ord('z'):
            result += chr(ord(letter) - 32)
        else:
            result += letter
    print(result)
