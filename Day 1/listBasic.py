# mylist = ["prashant","Ashish","komal","ankush","ashish","77","Sandip",60.52,"prashant"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
#Output 
# ['prashant', 'Ashish', 'komal', 'ankush', 'ashish', '77', 'Sandip', 60.52, 'prashant']
# <class 'list'>
# prashant
# Ashish
# komal
# prashant
# ['komal', 'ankush', 'ashish']
# ['prashant', 'Ashish', 'komal', 'ankush', 'ashish']
# ['Ashish', 'komal', 'ankush', 'ashish', '77', 'Sandip', 60.52, 'prashant']
# ['Ashish', 'ankush', '77', 60.52]

# mylist[2]="Akshay"
# print(mylist)

# if "ankush" in mylist:
#     print("Yes ankush is available")
# else:
#     print("not available")    

# mylist.append('harsh')  #.append is used for adding a element on top of list like stack
# mylist.append("laxman")
# print(mylist)

# mylist.insert(3,"sanket")
# print(mylist)

# mylist.remove("Sandip")
# print(mylist)

# newlist = mylist.copy()
# print(newlist)

# ---------------------------------------------------------------
# mylist = [['prashant','jah'],['86.56'],[444022,'yyy']]
# print("example of multidimentional list ")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# Output
# example of multidimentional list 
# [['prashant', 'jah'], ['86.56'], [444022, 'yyy']]
# prashant
# jah
# 86.56
# 444022
# yyy

# -----------------------------

# list2 =[50,25.34,'prashant']
# #del list2[2]  to delete particular element
# del list2  #to delete the whole list
# print(list2)


# list2 =[50,25.34,'prashant']
# list2.clear() # to empty the list not to delete like del
# print(list2)

# ------------------------------

# name = "prashant"
# print(name)
# myname = list(name) # list() called as list constructor
# print(myname)
# # Output
# # prashant
# # ['p', 'r', 'a', 's', 'h', 'a', 'n', 't']

# ------------------------------

#sorting 
# mylist=[44,22,77,0,9,88]
# mylist.sort() # default asecnding order  # must conatin homogenous element in sort function otherwise error 
# mylist.sort(reverse=True) #desecding order
# print(mylist)

# --------------------------------

#alising concept  means assigning one variable reference to another variable 
mylist=[44,22,77,0,9,88]
newlist = mylist  #change in one also shows in other bcoz both are pointing to the same address
print(id(newlist))
print(id(mylist))

