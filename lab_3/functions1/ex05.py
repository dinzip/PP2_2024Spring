from itertools import permutations

def perm(s):
    return list(permutations(s))


a = perm('abc')
for i in a:
    print(i)





# out=[]
# def perm(msg, i, length):
#     if i==length:
#         out.append("".join(msg))
#     else:
#         for j in range(i, length):
#             msg[i], msg[j] = msg[j], msg[i]
#             perm(msg, i+1, length)
#             msg[j], msg[i] = msg[i], msg[j]

# msg="acb"
# perm(list(msg), 0, len(msg))
# print(out)