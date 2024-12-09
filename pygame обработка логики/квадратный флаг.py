import pygame
pygame.init()

#size
width=500
height=300
size=(width,height)
screen=pygame.display.set_mode(size)

#color
GREEN=(0,255,0)
RED=(255,0,0)
WHITE = (255,255,255)
BLACK=(0,0,0)

first=WHITE
second=RED

FPS=60
clock=pygame.time.Clock()
speed=1
first_rect=pygame.Rect((150,100),(200,100))
second_rect=pygame.Rect((50,125),(50,50))

game_end=False
while not game_end:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_end=True
    if first_rect.colliderect(second_rect):
        second=GREEN
    else:
        second=RED
    screen.fill(BLACK)
    second_rect.x+=speed
    
    pygame.draw.rect(screen, first, first_rect)
    pygame.draw.rect(screen, second, second_rect)
    pygame.display.flip()
    
pygame.quit()    