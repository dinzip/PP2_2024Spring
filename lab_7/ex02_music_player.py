# press 'r' - change corner roundness of icons/images of songs
# press 'esc' - change theme dark/light
# press 'K_UP', 'K_DOWN' - changing in position(through songs)
# press 'K_LEFT', 'K_RIGHT' - change volume of music
# press 'RETURN'/'ENTER' - run music
# press 'SPACE' - pause/unpause music

import pygame, os, re
from mutagen.mp3 import MP3
pygame.init()

screen_w = 800
screen_h = 370
win = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Music player')

theme = 1 # give a theme, to change PRESS 'ESC' - 'ESCAPE'
rounded_icons = False # to change PRESS LETTER 'r'

#for saving information i use lists, list[0] - dark theme information.
# list[1] - light theme information

# needed colors
background_color = [(20, 20, 20), (220, 220, 220)]
foreground_color = [(34, 34, 34), (255, 255, 255)]

selected_color = [(51, 51, 51), (220, 220, 220)]
song_color = [(218, 218, 218), (0, 0, 0)]
author_time_color = [(120, 120, 120), (137, 145, 144)]

line_background_color = [(67, 67, 67), (220, 220, 220)]
line_middle_color = [(120, 120, 120), (167, 174, 174)]
line_foreground_color = [(218, 218, 220), (31, 94, 216)]

path = r'C:\Users\ННЛОТ\Desktop\subjects\sem1\labs\PP2_2024spring\lab_7\music'
#images:
run5 = pygame.image.load(path + '\\addition\\run5.jpg')
stop5 = pygame.image.load(path + '\\addition\\stop5.jpg')
run4 = pygame.image.load(path + '\\addition\\run4.jpg')
stop4 = pygame.image.load(path + '\\addition\\stop4.jpg')

run_image = [run5, run4]
stop_image = [stop5, stop4]

sound1 = pygame.image.load(path + '\\addition\\sound1.jpg')
sound1 = pygame.transform.scale(sound1, (45, 40))
sound2 = pygame.image.load(path + '\\addition\\sound2.jpg')
sound2 = pygame.transform.scale(sound2, (45, 40))

sound = [sound1, sound2]

# end of song:
SONG_END = pygame.USEREVENT + 1 # custom event type named 'SONG_END'
pygame.mixer.music.set_endevent(SONG_END) # sets the custom event SONG_END to be triggered when the music playback ends. 
# It registers the custom event so that Pygame will generate this event when the music finishes playing

# give icons of theme
moon = pygame.image.load(path + '\\addition\\moon5.png')
moon = pygame.transform.scale(moon, (30, 30))
sun = pygame.image.load(path + '\\addition\\sun2.png')
sun = pygame.transform.scale(sun, (30, 30))
theme_icon = [moon, sun]
#print moon if dark theme, otherwise sun

# main class for music 
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
        print(self.time, self.time_text)

    def get_rounded_corner_image(self, image):
        size = image.get_size() # assign width and height of image to size
        rect_img = pygame.Surface(size, pygame.SRCALPHA) # create surface wth same dimension with image, pygame.SRCALPHA is allowing transparency.
        pygame.draw.rect(rect_img, (255,255,255), (0,0,*size), border_radius = 15)
        image_copy = image.copy().convert_alpha() # copying, and converts the image to a format with an alpha channel, enabling transparency.
        image_copy.blit(rect_img, (0,0), None, pygame.BLEND_RGBA_MIN) # blends the rounded rectangle (rect_img) onto the copied image
        # pygame.BLEND_RGBA_MIN - this blend mode ensures that the alpha values of the pixels are combined in a manner that preserves the minimum value, effectively creating a cut-out effect for the rounded corners.
        return image_copy

    def get_names(self, text): #text = path to music without head folders: Dirty_Thoughts(Chloe_Adams).mp3
        pattern = '(?P<song>.+)\((?P<author>.+)\)' # pattern to match, song = 'Dirty_Thoughts', author = 'Chloe_Adams'
        a = re.search(pattern, text)

        rep = lambda t: t.replace('_', ' ') # Dirty_Thoughts -> Dirty Thoughts
        return rep(a.group('song')), rep(a.group('author'))

    def get_time(self):
        audio = MP3(self.path_music)
        len = audio.info.length
        return len, f'{int(len/60)}:{int(len%60)//10}{int(len%60)%10}' #to have a time in format m:ss

    def print_image(self, x, y, width, height):
        image = pygame.transform.scale(self.image, (width, height)) #transform to given widthF and height
        if rounded_icons: # if we want corner rounded icons
            rounded_image = self.get_rounded_corner_image(image)
            win.blit(rounded_image, (x, y)) # put on x, y coordinates
        else:
            win.blit(image, (x, y))
    
    def play_music(self):
        pygame.mixer.music.load(self.path_music) 
        pygame.mixer.music.play()

    def print_text(self, text, text_color, size, x, y):
        text_font = pygame.font.Font(path + '\\addition\\Alice-Regular.ttf', size)
        img = text_font.render(text, True, text_color)
        win.blit(img, (x, y))

    def draw_block(self, order, active):
        color = foreground_color[theme] 
        if active: color = selected_color[theme]
        x, y = Music.give_coord_by_order(order)
        pygame.draw.rect(win, color, (x-5, y-5, 370, 65), border_radius=10)
        
        if active: # if we in active song, make its image transparent
            img = pygame.transform.scale(self.image, (55, 55))
            img.set_alpha(150 if not theme else 200) # if theme is dark, more transparent, otherwise less 
            if rounded_icons: #if we want corner rounded icons
                image = self.get_rounded_corner_image(img)
                win.blit(image, (x, y))
            else:
                win.blit(img, (x, y))
        else:
            self.print_image(x, y, 55, 55)
        self.print_text(self.song_name, song_color[theme], 15, x+60, y)
        self.print_text(self.author_name, author_time_color[theme], 15, x+60, y+20)
        if active and (running or stopped):
            self.print_text(give_current_time(), author_time_color[theme], 15, x+330, y+15)
        else:
            self.print_text(self.time_text, author_time_color[theme], 15, x+330, y+15)

    
    def give_coord_by_order(order):
        if order <= 3: x = 20
        else: x = 400
        y = 140 + (order-1)%3*70
        return x, y

path_music_list = path + '\\music_list'
musics_list = []
for i in os.listdir(path_music_list):
    el = Music(os.path.join(path_music_list, i))
    musics_list.append(el)


text_font = pygame.font.Font(path + '\\addition\\Alice-Regular.ttf', 25)

def give_current_time():
    time_seconds = int(pygame.mixer.music.get_pos()/1000)
    return f'{time_seconds//60}:{time_seconds%60//10}{time_seconds%60%10//1}'

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    win.blit(img, (x, y))

# for order, el in enumerate(musics_list, start = 1):
#     el.draw_block(order, False)
def lower_block(active_order):
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
    global last_played, running
    music = musics_list[current_music_order]
    #button:
    if going and not stopped:
        image = run_image[theme]
        win.blit(image, (31, 14))
    else:
        image = stop_image[theme]
        win.blit(image, (30, 15))

    #image:
    x, y = 170, 10
    musics_list[current_music_order].print_image(x, y, 60, 60)
    
    #text:
    music.print_text(music.song_name, song_color[theme], 18, x+70, y)
    music.print_text(music.author_name, author_time_color[theme], 16, x+70, y+25)
    if going or stopped:
        music.print_text(give_current_time(), author_time_color[theme], 15, x+400, y+25)
    else:
        music.print_text(music.time_text, author_time_color[theme], 15, x+400, y+25)

    #line:
    pygame.draw.line(win, line_background_color[theme], (x+70, y+51), (x+430, y+51), 3) #x+430 since line sjould end when time_text ends. y+51 - line after author&song names
    if going or stopped:
        last_played = current_music_order
        # print(pygame.mixer.music.get_pos(), ' - ', music.time * 1000)
        portion = pygame.mixer.music.get_pos() / (music.time * 1000)
        dx = x + 70 + (430-70)*portion
        dx = int(dx)
        # middle line:
        pygame.draw.line(win, line_middle_color[theme], (x+70, y+51), (min(dx+40, x+430), y+51), 3)
        # main line, show at what second of song
        pygame.draw.line(win, line_foreground_color[theme], (x+70, y+51), (dx, y+51), 3)
        if dx > x+430: going = False

    # sound image:
    sound_img = sound[theme]
    win.blit(sound_img, (610, 21))

    # sound line:
    x1, x2, y = 655, 740, 40
    pygame.draw.line(win, line_background_color[theme], (x1, y), (x2, y), 3)
    current_sound = pygame.mixer.music.get_volume()
    dx = x1 + (x2-x1) * (current_sound/1.0)
    pygame.draw.line(win, line_foreground_color[theme], (x1, y), (min(dx, x2), y), 3)

    running = going


def change_order(dx):
    global active_order, running, stopped, last_active_order
    previous = active_order
    active_order = limit(active_order + dx)
    if active_order != previous:
        last_active_order = previous
        running = stopped = False
        if pygame.mixer.music.get_busy(): pygame.mixer.music.stop()

    print("active_order:", active_order)

def change_val(dx):
    global sound_val
    if sound_val + dx >= 0 and sound_val + dx <= 1: 
        sound_val += dx
        pygame.mixer.music.set_volume(sound_val)


run = 1
active_order = last_active_order = 0
last_played = next_play = 0
sound_val = 1.0

limit = lambda x: min(len(musics_list)-1, max(0, x))
running, stopped = False, False
page = 1
# page cover: page = 1: [0:6], page = 2: [3:9], page = 3: [6:12], page = 4: [9:15]
# by formula: lower_bound = 3*(page-1), upper_bound = min(3*(page+1), len(list)), since number of songs can be less than 3*(page+1)
# number of song in each page <= 6

while run:
    if next_play:
        pygame.time.delay(500)
        change_order(+1)
        musics_list[active_order].play_music()
        running = True 
        stopped = next_play = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_order(-1)
            if event.key == pygame.K_DOWN: 
                change_order(+1)
            if event.key == pygame.K_LEFT:
                change_val(-0.05) # -5%
            if event.key == pygame.K_RIGHT:
                change_val(+0.05) # +5%
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                print("playing")
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
            if event.key == pygame.K_ESCAPE:
                theme = not theme
            if event.key == pygame.K_r:
                rounded_icons = not rounded_icons
        if event.type == SONG_END: # if sing ended without us, the next song will start
            print("ENDED")
            if last_played == active_order and active_order < len(musics_list):
                next_play = True
            running = stopped = False

    win.fill(background_color[theme])
    
    # upper_block:
    pygame.draw.rect(win, foreground_color[theme], (6, 6, screen_w-12, 70), width = 0, border_radius = 10)
    # lower block:
    pygame.draw.rect(win, foreground_color[theme], (6, 86, screen_w-12, 275), width = 0, border_radius = 10)

    draw_text("Мои треки", text_font, song_color[theme], 10, 90)
    upper_block(running, stopped, active_order)
    lower_block(active_order)
    win.blit(theme_icon[theme], (758, 8))
    pygame.display.update()


pygame.quit()