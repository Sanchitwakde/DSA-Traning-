# function is a self contained block which is designed and executed seperately and return output to main function
# function always returns a value 
#python function can return multiple values 

#main function of python syntaxx - if __name__ == 'main':
# add pass when there is nothing to write 
def add():
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    result = a+b
    print("Addition is:",result)
if __name__ == "__main__":
    add()

#-------------------------------------------------------------------------------------------
#function with parameters 

def add(a,b):
    result = a+b
    print("Addition is:",result)

if __name__ == "__main__":
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    add(a,b)

#-------------------------------------------------------------------------------------------
#function with parameter and return value 

def add(a,b):
    result = a+b
    return result

if __name__ == "__main__":
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    r = add(a,b)
    print("Addition is:",r)

#-------------------------------------------------------------------------------------------
#function with returning multiple values 
def add(a,b):
    r1 = a+b
    r2 = a-b
    r3 = a*b
    r4 = a/b
    return r1, r2, r3, r4

if __name__ == "__main__":
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    r1,r2,r3,r4 = add(a,b)
    print("Addition is:",r1)
    print("Subtraction is:",r2)
    print("Multiplication is:",r3)
    print("Division  is:",r4)