#polymorphism 

# assigning additonal task to things(constructor, function, method) is called overloading 
# in python the function that is in last will be considered 
# no overloading concpt in the python 
#overloading 
def add(a):
    print (a)


#overloading

# variables are not override in runtime polymorphsim
# when child class functon is not satisfied witht the parent class function in that case child can override that fucntion

#overriding
# runtime polymorphism

class parent:
    def __init__(self):
        self.speed = 100
        print("cash")
    def bike(self):
        print("splendor",self.speed)

class child:
    def __init__(self):
        self.speed = 150
    def bike(self):
        print("splendor",self.speed)

obj = child()
obj.bike()


