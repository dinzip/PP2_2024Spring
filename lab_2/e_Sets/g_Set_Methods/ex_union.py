x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)
print(z)


x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}

result = x.union(y, z)
print(result)