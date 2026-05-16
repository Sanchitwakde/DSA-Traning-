#nested for loop
n = 1
for i in range(1,5):
    for j in range(1,6):
        print(n,end="")
        n = n+1
    print()

    #       j1 j2 j3 j4
    #i=1    1  1  1  1
    #i=2    2  2  2  2
    #i=3    3  3  3  3
    #i=4    4  4  4  4

# _____________________________________________________________________________________

n = 1
for i in range(1,5):
    for j in range(1,6):
        print(n,end="\t")
        n = n+1
    print()

#------------------------------------------------------------------------------------------------------
# askii values  0-266 in c lang 
# 0-65535 value in java
# A - 65, a = 97, 0-48
# B - 66, b = 98, 1-49
# C - 67, c = 99, 2-50

# askii value only take unsigned value 

# signed = - and +
# unsigned = only + positive 
# chr - to askii
# ord - from chr to ordinary
#------------------------------------------------------------------------------------------------------
n = 65
for x in range(1,6):
    for y in range(1,7):
        print(chr(n), end= "")
        n = n+1
    print()