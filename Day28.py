#!/bin/python3

import sys
import re
out = []
s2 = "@gmail.com"
N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    x = emailID.find(s2)
    if x >= 0:
        out.append(firstName)
out.sort()
print(*out,end='',sep='\n')
    