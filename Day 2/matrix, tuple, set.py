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
lis = [] 
for i in range(n):
    # ele = list(map(int,input("Enter Element: ").split()))
    ele = list(map(int,input("Enter Element: "))) # take input in one go 
    lis.append(ele)
for x in range(len(lis)):
    print(lis[x],end = "")




#-----------------------------------------------------------------------------------------------------------------------
a = str(input("enter ele: "))

a, b = map(str,input("enter ele: ").split()) #only work upto 2 words in same line in a single input 
print("value of a:",a)
print("values of b:",b)

no = 2
disc = []
for x in range(no):
    aff = list(map(int,input("enter ele: ").split())) # to write things in same line in one input only 
    disc.append(aff)
print(disc)

l = list(map(int,input("enter ele: ").split()))
print(l)

