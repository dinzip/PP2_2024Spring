def squares(a, b):
    for i in range(a, b+1):
        yield i*i 


for i in squares(1, 5):
    print(i)