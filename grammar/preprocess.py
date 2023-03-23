#!/usr/bin/env python3

from icecream import ic
import sys

t = sys.stdin.readlines()
t.append('\n')

s = [0]
paren = 0
for l in t:
    if paren != 0:
        print(l.lstrip(), end='')
        continue
    if len(l.strip()) == 0:
        print()
        continue
    ident = [col for col, ch in enumerate(l) if ch != ' '][0]
    if ident > s[-1]:
        s.append(ident)
        print('{', end='')
    elif ident < s[-1]:
        while s[-1] > ident:
            s = s[:-1]
            print('}', end='')
        if s[-1] != ident:
            exit(1)
    if l.find('(') != -1:
        paren += 1
    if l.find(')') != -1:
        paren -= 1

    print(l.lstrip(), end='')

print('}' * (len(s) - 1), end='')
