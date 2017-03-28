t = int(input())
#print (t)
#str = input().strip(' ')
for i in range(0,t):
    str = input().strip(' ')
    Ans1 = '';Ans2 = '';
    for i in range (0,len(str)):
        if(i % 2 == 0):
            Ans1 += str[i];
        else:
            Ans2 += str[i];
    print(Ans1 + " " + Ans2)    
        