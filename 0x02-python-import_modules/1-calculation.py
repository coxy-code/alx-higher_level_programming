#!/usr/bin/python3
a = 10
b = 5

calc = __import__("calculator_1")

add_result = calc.add(a, b)
sub_result = calc.sub(a, b)
mul_result = calc.mul(a, b)
div_result = calc.div(a, b)

print("{} + {} = {}".format(a, b, add_result))
print("{} - {} = {}".format(a, b, sub_result))
print("{} * {} = {}".format(a, b, mul_result))
print("{} / {} = {}".format(a, b, div_result))
