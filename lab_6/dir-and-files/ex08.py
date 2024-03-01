import os 

path = r'C:\Users\ННЛОТ\Desktop\subjects\sem1\labs\PP2_2024spring\lab_6\dir-and-files\ex08.txt'
name = os.path.basename(path)

if os.path.exists(path):
    print(f'File "{name}" exists')
    if os.access(path, os.X_OK):
        print(f'File "{name}" can be eliminated')
        os.remove(path)
        print(f'"{name}" is deleted')
    else:
        print(f'File "{name}" can\'t be eliminated')
else:
    print(f'File "{name}" does\'t exist')