lst = input()
lower = list(filter(lambda x: x.isupper(), lst))
upper = list(filter(lambda x: x.islower(), lst))
print(f'{len(lower)} - lowercase letters\n{len(upper)} - uppercase letters')