import pygame, math, time
pygame.init()
m = s = 0
def curr_time(): 
    global m, s
    m, s = time.localtime().tm_min, time.localtime().tm_sec

screen_w = 900
screen_h = 675
win = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Clock3')

img_main = pygame.image.load('mickeyclock_body.png')
img_main = pygame.transform.scale(img_main, (screen_w, screen_h))

img_hand1 = pygame.image.load('mmc1.png')
img_hand1 = pygame.transform.scale(img_hand1, (221, 350))

img_hand2 = pygame.image.load('mmc2.png')
img_hand2 = pygame.transform.scale(img_hand2, (165, 300))
radius = 15

def print_hand(img, degree):
    img = pygame.transform.rotate(img, degree)
    rect = img.get_rect()
    rect.center = win.get_rect().center
    rect.centerx += radius * math.sin(math.radians(-degree))
    rect.centery -= radius * math.cos(math.radians(-degree))

    win.blit(img, rect)

clock = pygame.time.Clock()
run = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = 0
    
    curr_time()
    win.blit(img_main, (0, 0))
    print_hand(img_hand1, s * (-6))
    print_hand(img_hand2, m * (-6))
    
    pygame.display.update()
    clock.tick(60)