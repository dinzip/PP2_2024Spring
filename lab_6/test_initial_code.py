from msvcrt import getch
from colorama import Fore, Back, Style
from clear_screen import clear 
import os


def give_sorted_dirs(path): #take a content of directory, by order: folders then files
    lst = [i for i in os.scandir(path)]
    lst.sort(key = lambda x: x.is_file()) #sort by is_file, such that directories have value flase = 0, file true = 1, directories at the beginig
    return lst

def correct_active(mx): #to change active if it exceeds limits
    global active 
    if active < 0:
        active = mx-1
    elif active >= mx:
        active = 0


def print_console(path): 
    current = 0
    content = give_sorted_dirs(path)
    correct_active(len(content))

    for i in content:
        if current != active:
            print(Back.BLACK + i.name, end = '')
        else:
            print(Back.LIGHTMAGENTA_EX + i.name, end='')
        current += 1
        print(Back.BLACK + '')

active = 0
stack_paths = []
stack_paths.append(os.getcwd())
name_and_content_of_file = []



while True:
    # os.system('cls') #clean window
    clear() #clean window
    path = stack_paths[-1] #take last path/directory
    print_console(path)
    if len(name_and_content_of_file) != 0:
        name, content = name_and_content_of_file
        print(f'\nContent of file "{name}":\n')
        print(content)
        name_and_content_of_file = []

    key = ord(getch())
    if key == 27: #ESC
        if len(stack_paths) != 1:
            stack_paths.pop()
        else:
            last_path = stack_paths[0]
            parent = os.path.dirname(last_path)
            stack_paths.pop()
            stack_paths.append(parent)
        active = 0
    elif key == 13: #Enter
        content = give_sorted_dirs(path)
        new_cont = content[active]
        if new_cont.is_dir():
            new_path = stack_paths[-1] + '\\' + new_cont.name
            stack_paths.append(new_path)
            active = 0
        else:
            new_path = stack_paths[-1] + '\\' + new_cont.name
            with open(new_path, 'r', encoding='utf8') as f:
                name_and_content_of_file = [new_cont.name, f.read()]
    elif key == 80: #Down arrow
        active += 1
    elif key == 72: #Up arrow
        active -= 1
    elif key == 8 or (key >= ord('0') and key <= ord('9')): #press delete or any number button to stop program
       break

