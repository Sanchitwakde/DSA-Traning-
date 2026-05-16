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