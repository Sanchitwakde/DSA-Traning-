#why python is called as dynamically types lang?
# age = 33
# pi = 3.14
# name = "prashant"
# result = True
#  print(type(age))
#  print(type(pi))
#  print(type(name))
#  print(type(result))
# print(id(age))
# print(id(pi))
# print(id(name))
# print(id(result))

#why all fundamental datatypes are immutable
# math = 50
# chem = 50
# phy = 50
# print(id(math))
# print(id(chem))
# print(id(phy)) #all have same memory block allocated ,its a temp memory . 


#simple if
# a = int(input("Enter any single digit :"))

# if a>0: 
#     print("Positive number")
# if a<0:
#     print("Negative number") 
# if a==0:
#     print("zero")      

#if-else

# day = input("Enter a day(lowercase):")

# if day =="saturday" or "sunday":
#      print("Weekend day")
# else :
#      print("Working day")  

#if-elif

# per = 65
# if per >=65:
#     print("grade A")
# elif per<=65 and per>=50 :
#     print("grade B")    
# else :
#     print("fail")        

#Askey
chr = ord(input("Enter any one character :")) #ord functuon is used to convert into askey code ex, a=65

if chr >= 65 and chr<=90 :
    print("upper case")
elif chr>=97 and chr<=122  :
    print("lower case")   
elif chr >=48 and chr<=57 :
    print("digit")   
else:
    print("Special symbols")    