tn = 2025
sv = tn
cnt = 0
while sv>0:
    sv=sv//10
    cnt=cnt+1

if cnt%2==0:
    mid = cnt/2
    n1 = tn%10**mid
    n2 = tn//10**mid
    sum = n1 + n2 
    sqr = sum*sum
    print(n1,n2)
    print("sum :",sum)
    print("Sqp",sqr)

    if sqr == tn:
        print("tech number")
    else:
         print("not a tech no")
        
