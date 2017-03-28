def Factorial(a):
    if (a == 1):
        return 1;
    else:
        return (a * Factorial (a-1))
    
no = int(input())
print (Factorial(no))
