import re

l_str = 'l_str_fdew f_re_ds_dop'
x = re.sub(r'_.', lambda a: a.group()[1].upper(), l_str)
print(x)