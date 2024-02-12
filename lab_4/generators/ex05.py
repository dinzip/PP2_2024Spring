def down(n):
    if n==0:
        yield 0
        return
    yield n
    yield from down(n-1)

for i in down(5):
    print(i)