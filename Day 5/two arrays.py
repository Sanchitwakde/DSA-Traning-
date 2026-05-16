# Intersection of 2 array 

arr = [2,3,4,4,5,6]
ar = [4,4]
ar3 = []

for i in arr:
    if i in ar and i not in ar3:
        ar3.append(i)
print(ar3)

