import re

l_str = 'cdabbds'

x = re.search(r"ab{2,3}", l_str)
if x:
    print("Matched -", x.group())
else:
    print("Didn't match")