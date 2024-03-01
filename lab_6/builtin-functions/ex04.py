import time, math 

def test(a, t):
    time.sleep(t/1000)
    print(f'Square root of {a} after {t} miliseconds is {math.sqrt(a)}')


a, t = float(input('Input:\n')), float(input())
test(a, t)