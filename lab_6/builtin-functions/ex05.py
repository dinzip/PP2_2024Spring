def determine(num, t):
    print(f'tuple #{num} is {all(t)}')


t1 = (True, True, True, True)
t2 = (True, True, False, True)

determine(1, t1)
determine(2, t2)
