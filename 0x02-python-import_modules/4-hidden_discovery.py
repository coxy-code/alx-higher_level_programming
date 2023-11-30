#!/usr/bin/python3
import marshal
import types

with open('hidden_4.pyc', 'rb') as file:
    bytecode = file.read()

code = marshal.loads(bytecode)
module = types.CodeType(*code)

names = set()

for const in module.co_consts:
    if isinstance(const, types.CodeType):
        names.update(const.co_names)

for name in sorted(names):
    if not name.startswith('__'):
        print(name)

