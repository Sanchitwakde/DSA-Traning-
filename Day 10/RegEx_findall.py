# to find all occurences 

import re
list = re.findall("[0-9]","ab4$+#7s9")
print(list)
for x in list:
    print(x)

