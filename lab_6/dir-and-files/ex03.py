import os 

path = r'C:\Users\ННЛОТ\Desktop\subjects\sem1\labs\PP2_2024spring\lab_6\dir-and-files\ex02.py'
# path.replace('\\', '/')

if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')