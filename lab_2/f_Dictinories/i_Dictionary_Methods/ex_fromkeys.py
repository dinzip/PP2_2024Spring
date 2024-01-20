#Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)




#without specifying the value:
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)