# Qunatifiers:
# We can use quantifiers to specify the number of
# occurrences to match.
# a== > Exactly one 'a'

# a+== > Atleast one 'a'

# a*== > Any number of a's including zero number

# a?a{m}== > Exactly m number of a's

# a{m, n} ==> Minimum m number of a's and Maximum n number of a's

import re
x="a"
x="a+"
x="a*"
x="a?"
x="a{3}"
x="a{2,3}"
matcher = re.finditer(x,"aabbabaabbabaaaa")
for match in matcher:
    print(match.start(),"--",match.group())