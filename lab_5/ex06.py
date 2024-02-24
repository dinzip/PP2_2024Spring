import re
l_str = 'my name, gl.,4'
x = re.sub('[\s,.]', ':', l_str)
print("Result:\n", x)
