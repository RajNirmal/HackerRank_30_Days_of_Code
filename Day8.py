noOfEntries = int(input())
#print ('THe no of entries is ' + str(noOfEntries))
PhoneBook = {};
for i in range (0,noOfEntries):
    #print (i)
    a = input();
    a = a.split(' ')
    PhoneBook[a[0]] = a[1]
#print(PhoneBook)
while (1):
    ValueToSearch = input();
    #print (ValueToSearch)
    Output = PhoneBook.get(ValueToSearch,"NONE")
    if(Output == "NONE"):
        print('Not found')
    else:
        print(ValueToSearch+"="+Output)
    
