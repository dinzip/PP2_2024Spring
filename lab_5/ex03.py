import re
l_str = 'abdykadyr_daryn45d_add'
x = re.findall("[a-z]+_[a-z]+", l_str)
if x:
    print("Matched, sequences:", x)
else:
    print("Didn't match")