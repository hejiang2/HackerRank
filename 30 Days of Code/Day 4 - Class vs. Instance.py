# In Python, class variables are declared when a class is being constructed.
# This means that the class owns the variable — it is contained within the class — so all instances of the class will be able to access that variable. Class variables are shared by all instances that access the class.
# Instance variables, unlike class variables, are owned by an instance of a class.
# This means that the value of each instance variable can be different, whereas, in a class variable, the variable can only have one value that you assign when you declare the variable. Instance variables are declared inside a class method.
# In order to assign a value to these variables, we need to pass a set of values as parameters when we create an object instance of our class.

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")