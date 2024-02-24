import re
l_str = 'HiMyNameIsDarynIt\'sMy 8th ex'
x = re.sub('[A-Z]', lambda a:f' {a.group()}', l_str)
print(x)
