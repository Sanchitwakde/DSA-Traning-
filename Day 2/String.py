# ""
# ''
# """ """ - paragraph and also used for comment 


Str = "yoo"
print(Str[::-1]) #to reverse a string 

#------------------------------------------------------------------------------------------------------

s = "Learning is fun and fast"
print(s.find("a"))
print(s.find("fu"))
print(s.rfind("r"))

sa="rthyjuhgbvcegnhmg"
print(s.count("h",1,10))
#------------------------------------------------------------------------------------------------------

sq = "learning python is very easy"
s1 = sq.replace("python","yoo")
print(s1)
#------------------------------------------------------------------------------------------------------
ls = sq.split()
print(ls)
print(len(ls))
#------------------------------------------------------------------------------------------------------
dt = "14-02-2004"
de = dt.split("-")
print(de)
#------------------------------------------------------------------------------------------------------
l = ["my","dog","name","is","maggie"]
jo = "|".join(l)
print(jo)
#------------------------------------------------------------------------------------------------

#spliting, reversing and joining the string
inp = "learning is very easy"
spt = inp.split()
rev = spt[::-1]
print(rev)
jo = " ".join(rev)
print(jo)

#-----------------------------------------------------------------------------------------
#reverse the alphabet not the order 
inps = "learning is quite easy"
spts = inps.split()
for x in spts:
    revp = x[::-1]
    print(revp,end=" ")

#-----------------------------------------------------------------------------------------
#unique value in s string
inputs = "ASDFGHJKAASDDSFSSHDHSHJHJNUEJEIFNPEMKFSNJJADFGHJKD"
sp = set(inputs)
jo = "".join(sp)
print(jo)

#alt method 
# emp=""
# for i in range(len(inputs)):
#     if inputs[i] not in emp:
#         emp = emp+inputs[i]
#     print(emp)
#----------------------------------------------------

