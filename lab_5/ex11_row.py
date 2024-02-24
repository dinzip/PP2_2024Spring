import re, csv 

with open('row.txt', 'r', encoding='utf8') as f:
    row = f.read()


pattern = r'\n(?P<order>[0-9]+\.)\n(?P<name>.+)\n(?P<count>.+) x (?P<price>.+)\n(?P<price2>.+)\n(?P<cost>.+)\n(?P<worth>.+)'
x = re.finditer(pattern, row)

tof = lambda s: float(re.sub('[\s,]', lambda a: '.' if a.group()==',' else '', s))
# for i in x:
#     print(i.group('name'))
with open('row_data.csv', 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['order', 'name', 'count', 'price', 'cost', 'worth'])
    for i in x:
        rrr = 'Чистая линия скраб мягкий 50 мл'
        writer.writerow([
            i.group('order'), 
            rrr, 
            f'{tof(i.group('count'))}*{tof(i.group('price'))}', 
            tof(i.group('price2')), 
            i.group('cost'), 
            tof(i.group('worth'))])
