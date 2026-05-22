# Pre defined Character classes:
# # \s == > Space character
# \S == > Any character except space character
# # \d == > Any digit from 0 to 9 ,[0-9]
# \D == > Any character except digit [^0-9]*
# \w == > Any word character [a-zA-Z0-9]
# \W == > Any character except word character (Special Charac
# . == > Any character including special characters
import re
x="\\s"
x="\\S"
x="\\d"
x="\\D"
x="\\w"
x="\\W"
x="."

matcher =re.finditer(x,"a7b D 2@k2D8z")
for match in matcher:
    print(match.start(),"--",match.group())