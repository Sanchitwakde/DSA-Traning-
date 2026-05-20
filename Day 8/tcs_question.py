# Q. Compute the nearest larger number by interchanging its digits updated. Given 2
# numbers a and b find the smallest number greater than b by interchanging the digits of
# a and if not possible print -1.
# . Input Format : 2 numbers a and b, separated by space.
# . Output Format: A single number greater than b. If not possible, print -1
# . Constraints: 1 <= a,b <= 10000000

# Explanation of the Examples:
# Example 1:
# Input:
# a=459
# b=500
# Permutations of 459:[459,495,549,594,945,954]
# Valid numbers greater than 500: [549,594,945,954]
# Smallest valid number:
# 549



from itertools import permutations
def generate_permutations(a,b):
    num = str(a)
    perm = set(permutations(num)) # so that there are no duplicates 
    res = []
    for i in perm:
        nums = int("".join(i))
        if nums>b:
            res.append(nums)

    if len(res) == 0:
        return -1
    
    return min(res)

if __name__ =='__main__':
    a = 5678
    b = 6789
    obj = generate_permutations(a,b)
    print(obj)



  
