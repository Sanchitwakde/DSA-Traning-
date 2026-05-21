#for loop (for and while both are called entry point loop)

# for i in range(5): #default i=0 also by defatlt increment by 1
#     print(i)

# for i in range(2,11): #start from 2   upto 10 checks i<11
#     print(i)

# for i in range(2,11,2): #increment by 2
#     print(i)

# for i in range(5,1,-1): #decrement by 1
#     print(i)

# for i in range(1,11): # for table of any number ex=2
#     print(i * 2)

#tables
# for i in range(1,11):
#     print(i*1," ",i*2," ",i*3," ",i*4," ",i*5)

# print("--------------------------------------------------")
# for i in range(1,11):
#     print(i*11," ",i*12," ",i*13," ",i*44," ",i*15)

#wap to accept three paper marks and calculate total , percentage and check if he/she is passed in all the subject 
#so print pass else print fail

# m1 = int(input("Enter marks of paper 1:"))
# m2 = int(input("Enter marks of paper 2:"))
# m3 = int(input("Enter marks of paper 3:"))

# total = m1+m2+m3
# per = total/3

# print("Total = " , total)
# print("Percentage = ", per , "%")
# if m1>=60 and m2>=60 and m3>=60:
#     print("Pass")
# else:
#     print("Fail")    

# #if percentage is greater then 65 and gender = "male" so he is eligible for placement else not eligible 
# gender = input("Enter the gender(M/F):")

# if per >=65 and gender=="M" :
#     print("Eligible for placment.")
# else:
#     print("Not eligible.")    

#required output 1  5
#                2  4
#                4  2
#                5  1

for i in range(1,6):
    if i == 3:
        continue
    print(i ," ",6-i) 

#zip() we can take multiple range funtion inside zip()
# example:-  for i,j in zip(range(1,6),range(5,0,-1)):    