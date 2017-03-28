#!/bin/python3

import sys
arr = []
Max = -99
currentMax = 0
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
for i in range(0,4):
    for j in range(0,4):
        currentMax = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
        Max = max(currentMax,Max)
        #print(arr[i][j],arr[i][j+1],arr[i][j+2])
        #print(arr[i+1][j+1])
        #print(arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2])
        #print()
    
print(Max)
        
