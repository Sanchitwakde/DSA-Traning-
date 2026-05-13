# when using the stack use only append and pop 
# .extend() used to merge an array 
# sort() to arrange text 
# clear() to clear the list

arr = [[10,2],13,[67,54]]
for i in range(len(arr)):
    print(arr[i])

#matrix
ar = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(ar)):
    for j in range(len(ar[i])):
        print(ar[i][j],end=" ") #end = " " is used to print in matrix from because normally it will print line by line
        # print(ar[i][j])
    print()

#------------------------------------------------------------------------------------------------
#tuple can be created by 
#read only , no duplicates, 
# t = (), t = tuple(), t = any number by default it is tuple 
tup = (7,6,4,3)
print(tup)
print(type(tup))

#-------------------------------------------------------------------------------------------------------
# set only store unique value no matter you write duplicates
s = {1,2,4,8,8,8,5,5,9}
print(s)

#ex - remove duplicates from this list    (by using set)
aoo = [1,5,5,6,7,8,9,23,23,5,8]
s = set(aoo)
aoo = list(s)
print(aoo)

#take user input and print it
n = int(input("Enter size of list: "))
lis = (list(map(int,input().split())))
for i in range(n):
    ele = int(input("Enter element: "))
    lis.append(ele)
for x in range(len(lis)):
    print(lis[x])




#-----------------------------------------------------------------------------------------------------------------------
a = int(input)
a, b = map(int,input().split())

aff = list(map(int,input().split())) # to write things in same line in one input only 

