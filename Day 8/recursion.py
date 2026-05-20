#loop is better choice than recursion 

def fact(n):
    n = 5
    if n == 0 or n == 1:
        return 1

    else:
        return n*fact(n-1)
    

    