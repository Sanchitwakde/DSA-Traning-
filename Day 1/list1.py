# mylist=[44,22,77,0,9,88]
# for i in mylist:
#     print(i)

#move the zeros in last
# io = [0,1,4,0,2,5]   
# # op = [1,4,2,5,0,0] 

# for i in io :
#     if io[i]==0:
#       del io[i]  # also io.remove(i)
#       io.append(0) #    io.append(i)
    
# print(io)

# find the second largest elememt 

# list = [7,3,9,2,8] # sort it then print -2 value.
# lar = list[0]
# slar = list[0]
# for i in list:
#     if list[i] > lar:
#         slar = lar
#         lar = list[i]
#     else:
#         slar = list[i]  #unsolved 
# print(slar)

# -------------------------------------
# a=[1,2,3,4,5,6,7,8,9]
# a[::2] = 10,20,30,40,50,60
# print(a) #error since a will not have space to insert 60

# -----------------------------------

# a=[1,2,3,4,5]
# print(a[3:0:-1]) #output = [4,3,2]

# ---------------------------------

# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [8,9,10,11],
#        [12,13,14,15]]

# for i in range(0,4):
#     print(arr[i].pop())

# #output
# 4
# 7
# 11
# 15  

# --------------------------------------

# arr = [1,2,3,4,5,6]

# for i in range(1,6):
#     arr[i-1] = arr[i]

# for i in range(0,6):
#     print(arr[i], end = " ")

#Output 2 3 4 5 6 6 
# ------------------------------------

# fru_list1= ['Apple','Berry','Cherry','Papaya']
# fru_list2 = fru_list1
# fru_list3 = fru_list1[:]

# fru_list2[0]='Guava'
# fru_list3[1]='Kiwi'

# sum = 0

# for ls in (fru_list1,fru_list2,fru_list3):
#     if ls[0] == 'Guava':
#         sum += 1

#     if ls[1] == 'Kiwi':
#         sum += 20

# print(sum)            

# ----------------------------------

# A =[1,2,3]
# B =[2,3,4]
# C =[3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)

# ----------------------------------

size = int(input("Enter the size of array :"))
arr = []
for i in range(0,size):
    val = int(input())
    arr.append(val)

print(arr)
sum = 0
for i in range(size-1):
     sum += abs(arr[i] - arr[i+1])

print(sum) 

# Enter the size of array :5
# 10
# 11
# 7
# 12
# 14
# [10, 11, 7, 12, 14]
# 12