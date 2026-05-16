s = "A man, a plan, a canal: Panama"
st = ""
for i in range(len(s)):
    if s[i].isalpha():
        st += s[i].lower()
    else:
        pass

print("After:",st)

rev = ""
for x in range(len(st)-1,-1,-1):
    rev = rev+st[x]



if st == rev:
    print(" It is palindrome")
else:
    print("Not a palindrome")

