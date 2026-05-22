import re
x = "[abc]"
x = "[^abc]"
x = "[a-z]"
x = "[0-9]"
x = "[a-zA-Z0-9]"
x = "[^a-zA-Z0-9]"
matcher = re.finditer(x,"ab34#$%#@87%6589zsABGh")
for match in matcher:
    print(match.start(),"--",match.group()) #  ' ' -single quote will also work 

    #cannot directly print as it is a iterable will give you address only


    