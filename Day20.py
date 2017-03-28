#!/bin/python3

import sys


n = int(input().strip())
#a = [int(a_temp) for a_temp in input().strip().split(' ')]
a = list(map(int, input().split(' ')));
#print(*a)
numberOfSwaps = 0
for i in range (0,len(a)-1):
    for j in range (0,len(a)-1):
        #print("i is"+str(i)+" j is "+str(j))
        if(a[j]>a[j+1]):
            numberOfSwaps += 1
            a[j],a[j+1] = a[j+1],a[j]
print("Array is sorted in "+str(numberOfSwaps)+" swaps.");
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[-1]))

