class Person:
    Age = 0;
    def __init__(self,initialAge):
        if initialAge < 0:
            Person.Age = 0
            print("Age is not valid, setting age to 0.")
        else:
            Person.Age = initialAge
        ## Add some more code to run some checks on initialAge
    def amIOld(self):
        #print(Person.Age)
        if Person.Age < 13:
            print ("You are young.")
        elif Person.Age >= 13 and Person.Age < 18:
            print ("You are a teenager.")
        else:
            print ("You are old.")
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        Person.Age = Person.Age + 1;
        # Increment the age of the person in here      