with open('ex05.txt', 'w') as f:
    lst = [1, 'is', 'mine', [1, 1, 1], (1, 7), {1:5}, {1, 4, 5}]
    f.write(' '.join(map(str, lst)))
    
    f.write('\n')
    f.writelines(map(str, lst))