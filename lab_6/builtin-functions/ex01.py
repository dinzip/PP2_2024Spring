l = [1, 2, 3, 5]
print(eval('*'.join(map(str, l))))

# p = 1
# def func(x):
#     global p 
#     p *= x
#     return x
# print(p if list(map(func, l)) else '')

# or:
# print(p if list(filter(func, l)) else '')
# or:
# ne = l.sort(key = func)
# print(p)
