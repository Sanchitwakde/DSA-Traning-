#find power using recursion x^y

def power(x,y):
    if y == 0:
        return 1
    elif x == 0:
        return 0
    elif y == 1:
        return x 
    elif x ==1:
        return 1
    else:
        return x*(power(x,y-1))

if __name__ == '__main__':
    res = power(7,30)
    print(res)
    