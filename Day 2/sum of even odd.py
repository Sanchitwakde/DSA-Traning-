n = int(input("enter size:"))
arr = []
even = 0
odd = 0 
e =0
o =0

for i in range (n):
    ele = int(input("enter element: "))
    arr.append(ele)

for x in arr:
    if x%2 == 0 :
        even = even +x
        e = e+1
    else :
        odd = odd + x
        o = o +1

print("sum of even ", even )
print("sum of odd :", odd)
print(e,o)

