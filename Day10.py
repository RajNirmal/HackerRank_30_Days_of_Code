#!/bin/python3
def consecutiveones(data):
    longest = 0
    current = 0
    for num in data:
        if( int(num) == 1 ):
            current += 1
        else:
            longest = max(current,longest)
            current = 0
    return max(current,longest)

n = int(input())
binaryRepresentation = (bin(n)[2:])
print(consecutiveones(binaryRepresentation))



#if(index != 0):
#        if(value == binaryRepresentation[index-1]):
#            count = count+1
   


    
    
