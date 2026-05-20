#find sum of N using recursion

def sum(n):
    if n==0:
        return 0
    else:
        return n +sum(n-1)
if __name__ == '__main__':
    n= 99
    res = sum(n)
    print(res)