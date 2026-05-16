arr = [-1,2,-3,-4,5,-6,8]
par = []
nar = []
res= []
for i in arr:
    if i >0:
        par.append(i)
    else:
        nar.append(i)

print("Positive: ",par,"Negative: ",nar)

for i in range(len(nar)):
    res.append(nar[i])
    res.append(par[i])
print(res)