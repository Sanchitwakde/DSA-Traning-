for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end = "")
    print()

#------------------------------------------------------------------------------------------------------
sp = 0
for x in range(4,0,-1):
    for z in range(sp):
        print(" ", end="")
    for y in range(1,x+1):
        print("* ",end="")
    print()
    sp =sp+1

ps = 3
for x in range(1,6):
    for z in range(sp):
        print(" ", end="")
    for y in range(1,x+1):
        print("*",end="")
    print()
    ps =ps+1