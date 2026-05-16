d ={}
d[100] = "peter"
d[200] = "steve"
d[300] = "gon"

print(d[200])

#--------------------------------------------------------------------------------------------------------------------

n ={}
stud = int(input("Enter number of student: "))
for x in range(stud):
    name = input("enter your name: ")
    city = input("enter your city: ")
    n[name]=city

print(n)
for y in n:
    print(x,"",n[y])

#---------------------------------------------------------------------------------------------------------------------

d={100:"sish", 200: "shant", 300:"deep"}
print(d.keys())
for k in d.keys(): # to print only keys 
    print(k)
for y in d.values(): # to only print values of keys
    print(y)

#------------------------------------------------------------------------------------------------------------------
