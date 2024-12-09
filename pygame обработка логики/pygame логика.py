import pygame

pygame.init()

width,height=600, 600

size=(width, height)
screen=pygame.display.set_mode(size)

clock=pygame.time.Clock()
FPS=30

bg=pygame.image.load('space.jpg')
ufo=pygame.image.load('ufoRed.png')

ufo_dim=91
ufo_x=20
ufo_y=20
ufo_speed=15

move_x=0
move_y=0

game_end=False
while not game_end:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_end=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                move_y=1
            if event.key==pygame.K_w:
                move_y=-1
            if event.key==pygame.K_a:
                move_x=-1            
            if event.key==pygame.K_d:
                move_x=1
    
    ufo_x+=ufo_speed*move_x
    ufo_y+=ufo_speed*move_y
    
    if ufo_x<0 or ufo_x>width-ufo_dim:
        ufo_x+=ufo_speed*move_x*-1
    if ufo_y<0 or ufo_y>height-ufo_dim:
        ufo_y+=ufo_speed*move_y*-1
    
    
    move_x = 0
    move_y = 0    
    
    screen.blit(bg,(0,0))
    screen.blit(ufo,(ufo_x,ufo_y))
    
    pygame.display.flip()

pygame.quit()
    
