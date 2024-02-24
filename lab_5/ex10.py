import re
l_str = 'YouTube, iPhone and eBay'
x = re.sub('.[A-Z]', lambda a: f'{a.group().lower()[0]}_{a.group().lower()[1]}', l_str)
print(x)