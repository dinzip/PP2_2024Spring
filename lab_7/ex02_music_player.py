import pygame, os, re
from mutagen.mp3 import MP3
pygame.init()

screen_w = 800
screen_h = 370
win = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Music_player')

# needed colors:
white = (255, 255, 255)
gray = (220,220,220)
gray_dark = (137, 145, 144)
black = (0, 0, 0)
blue_dark = (7, 101, 98)

# paths:
path_to_lab7m =  r'C:\Users\ННЛОТ\Desktop\subjects\sem1\labs\PP2_2024spring\lab_7\music'
path_to_font = os.path.join(path_to_lab7m, r'addition\Alice-Regular.ttf')
path_to_music_list = os.path.join(path_to_lab7m, 'music_list')
path_to_run_img = os.path.join(path_to_lab7m, r'addition\run4.jpg')
path_to_stop_img = os.path.join(path_to_lab7m, r'addition\stop4.jpg')

class Music:
    def __init__(self, path_folder):
        content = os.listdir(path_folder)
        # print(content, content[::-1])
        path_image = [i for i in content if re.search('(jpeg)|(png)', i)][0]
        path_music = [i for i in content if re.search('.mp3', i)][0]
        # print(path_image, path_music)
        self.path_image = os.path.join(path_folder, path_image) # get a full path from initial path to image/music path
        self.path_music = os.path.join(path_folder, path_music)

        self.image = pygame.image.load(self.path_image).convert()
        
        self.song_name, self.author_name = self.get_names(path_music) # split to song and author names

        self.time, self.time_text = self.get_time()
        # print(self.time, self.time_text)


    def get_names(self, text): #text = path to music without head folders: Dirty_Thoughts(Chloe_Adams).mp3
        pattern = '(?P<song>.+)\((?P<author>.+)\)' # pattern to match, song = 'Dirty_Thoughts', author = 'Chloe_Adams'
        a = re.search(pattern, text)

        rep = lambda t: t.replace('_', ' ') # Dirty_Thoughts -> Dirty Thoughts
        return rep(a.group('song')), rep(a.group('author'))

    def get_time(self):
        audio = MP3(self.path_music) #use another library to efficiently getting time
        len = audio.info.length
        return len, f'{int(len/60)}:{int(len%60)//10}{int(len%60)%10}' #to have a time in format m:ss

    def print_image(self, x, y, width, height):
        imp = pygame.transform.scale(self.image, (width, height)) #transform to given width and height
        win.blit(imp, (x, y)) # put on x, y coordinates
    
    def play_music(self):
        pygame.mixer.music.load(self.path_music) 
        pygame.mixer.music.play()

    def print_text(self, text, text_color, size, x, y):
        text_font = pygame.font.Font(path_to_font, size)
        img = text_font.render(text, True, text_color)
        win.blit(img, (x, y))

    def draw_block(self, order, active):
        color = white 
        if active: color = gray

        x, y = Music.give_coord_by_order(order)
        # print(x, ' - ', y)
        pygame.draw.rect(win, color, (x-5, y-5, 370, 65), border_radius=10)
        self.print_image(x, y, 55, 55)
        self.print_text(self.song_name, black, 15, x+60, y)
        self.print_text(self.author_name, gray_dark, 15, x+60, y+20)
        self.print_text(self.time_text, gray_dark, 15, x+330, y+15)

    
    def give_coord_by_order(order):
        if order <= 3: x = 20
        else: x = 400
        y = 140 + (order-1)%3*70
        # match order:
        #     case 1: return 20, 140
        #     case 2: return 20, 210
        #     case 3: return 20, 280
        #     case 4: return 400, 140
        #     case 5: return 400, 210
        #     case 6: return 400, 280
        return x, y


musics_list = []
for i in os.listdir(path_to_music_list):
    el = Music(os.path.join(path_to_music_list, i))
    musics_list.append(el)

# print(type(musics_list[0]))
def check():
    x = 10
    y = 100
    for i in musics_list:
        i.print_image(x, y, 70, 70);
        x+=90

text_font = pygame.font.Font(path_to_font, 25)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    win.blit(img, (x, y))

# for order, el in enumerate(musics_list, start = 1):
#     el.draw_block(order, False)
def lower_block(last_active_order, active_order):
    global page
    end = max(6, 3 * (page+1)) # one page cover 6 songs, end = order of last song in current page
    id_start = end - 6 # 6 elements in one page
    id_end = min(end, len(musics_list)) #prevention, if page have 5 songs, but end == 6. It causes trubles, list out of range 

    if active_order >= 3*(page+1): # open new 3 songs
        page += 1
        end = 3*(page+1)
        id_start = end - 6
        id_end = min(end, len(musics_list))
    elif active_order < 3 * (page-1): # open previous 3 songs
        page -= 1
        id_end = 3*(page+1)
        id_start = id_end - 6
        id_end = min(len(musics_list), id_end)

    for order, el in enumerate(musics_list[id_start:id_end], start = 1):
        if order == active_order - 3*(page-1) + 1: #if order in current song, make background gray
            el.draw_block(order, True)
        else: 
            el.draw_block(order, False)

def upper_block(going, stopped, current_music_order):
    music = musics_list[current_music_order]
    #button:
    if going and not stopped:
        image = pygame.image.load(path_to_run_img).convert()
        win.blit(image, (30, 14))
    else:
        image = pygame.image.load(path_to_stop_img).convert()
        win.blit(image, (30, 15))

    #image:
    x, y = 170, 10
    musics_list[current_music_order].print_image(x, y, 60, 60)
    # musics_list[current_music_order].draw_block(current_music_order, False, 200, 15)
    #text:
    music.print_text(music.song_name, black, 18, x+70, y)
    music.print_text(music.author_name, gray_dark, 16, x+70, y+25)
    music.print_text(music.time_text, gray_dark, 15, x+400, y+25)

    #line:
    pygame.draw.line(win, gray, (x+70, y+51), (x+430, y+51), 3)
    if going or stopped:
        portion = pygame.mixer.music.get_pos() / (music.time * 1000)
        dx = x + 70 + (430-70)*portion
        dx = int(dx)
        pygame.draw.line(win, blue_dark, (x+70, y+51), (dx, y+51), 3)
        if dx > 430: going = False

    global running
    running = going

    #Names:
    # musics_list[current_music_order].print_text()

def change_order(dx):
    global active_order, running, stopped, last_active_order
    previous = active_order
    active_order = limit(active_order + dx)
    if active_order != previous:
        last_active_order = previous
        running = stopped = False
        if pygame.mixer.music.get_busy(): pygame.mixer.music.stop()

    # print(active_order)

run = 1
active_order = last_active_order = 0
limit = lambda x: min(len(musics_list)-1, max(0, x))
running, stopped = False, False
page = 1
clock = pygame.time.Clock()
# page cover: page = 1: [0:6], page = 2: [3:9], page = 3: [6:12], page = 4: [9:15]
# by formula: lower_bound = 3*(page-1), upper_bound = min(3*(page+1), len(list)), since number of songs can be less than 3*(page+1)
# number of song in each page <= 6

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                change_order(-1)
            if event.key == pygame.K_DOWN: 
                change_order(+1)
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                # print("playing")
                musics_list[active_order].play_music()
                running = True
            if event.key == pygame.K_SPACE:
                if not stopped and not pygame.mixer.music.get_busy():
                    musics_list[active_order].play_music()
                    running = True
                    stopped = not stopped
                elif stopped:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                stopped = not stopped
    
    win.fill(gray)
    
    pygame.draw.rect(win, white, (6, 6, screen_w-12, 70), width = 0, border_radius = 10)
    pygame.draw.rect(win, white, (6, 86, screen_w-12, 275), width = 0, border_radius = 10)
    # check()
    # musics_list[0].print_image(100, 200, 100, 100)
    draw_text("Мои треки", text_font, (0, 0, 0), 10, 90)

    upper_block(running, stopped, active_order)
    lower_block(last_active_order, active_order)
    pygame.display.update()
    clock.tick(60)

pygame.quit()