n = int(input())
l = (i for i in range(n+1) if i%2==0)
for i in l:
    print(i, end=', ' if i!=n-n%2 else '')
