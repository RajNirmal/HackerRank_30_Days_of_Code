#!/bin/python3

import sys


S = input().strip()
try:
    int(S)
    print(int(S))
except ValueError:
    print('Bad String')