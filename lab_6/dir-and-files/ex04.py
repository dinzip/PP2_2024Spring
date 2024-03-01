import os

path = r'C:\Users\ННЛОТ\Desktop\subjects\sem1\labs\PP2_2024spring\lab_6\dir-and-files\ex04.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))