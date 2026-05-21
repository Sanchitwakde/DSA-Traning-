# Capgemini in its online written test has a coding question, wherein the students are given a
# string with multiple characters that are repeated consecutively. You're supposed to reduce the
# size of this string using mathematical logic given as in the example below:

# Input :
# aabbbbeeeeffggg
# Output:
# a2b4e4f2g3
# -----------------
# Input :
# abbccccc
# Output:
# ab2c5

strs ="aabbbbeeeeffggg"
count = 1
res=""

for i in range(len(strs)-1):
    if strs[i] == strs[i+1]:
        count +=1
        
    else:                       #this will run as the character changes
        res += strs[i]          # for ex- res += "a"
        if count >1:
            res += str(count)   # convert int to string 
        count = 1               #reset counter here again

res += strs[-1]                 #this is for the last character of the string
if count > 1:
    res += str(count)
print(res)



