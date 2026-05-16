arr = []
n = int(input("Enter size of array: "))
for i in range(n):
    arr.append(int(input("Enter number: ")))

key = int(input("Enter key which is to be inserted: "))
loc = int(input("Enter the location: "))
arr.append(0)

for i in range(len(arr)-1,loc,-1):
    arr[i] = arr[i-1]
arr[loc]=key
print(arr)

for x in range(loc+1,len(arr)):
    arr[x-1]= arr[x]
arr.pop()
print(arr)


