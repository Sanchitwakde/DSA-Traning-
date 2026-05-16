n = int(input("Enter size:"))
ele = []
sum = 0
for i in range (n):
    eles = int(input("Enter element:"))
    ele.append(eles)

for x in range(len(ele)):
    sum = sum + ele[x]
    print(sum)
    

