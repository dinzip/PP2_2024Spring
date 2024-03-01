# import shutil 

# shutil.copy('ex04.txt', 'ex07.txt')

with open('ex04.txt', 'r') as f1:
    with open('ex07.txt', 'w') as f2:
        f2.write(f1.read())
        # for i in f1: f2.write(i)