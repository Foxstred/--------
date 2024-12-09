import pygame 

pygame.init()

WIDTH=500
HEIGHT=300
size=(WIDTH, HEIGHT)
screen=pygame.display.set_mode(size)

GREEN=(0,255,0)
RED=(255,0,0)
WHITE = (255,255,255)
BLACK=(0,0,0)

FPS=60
clock=pygame.time.Clock()
speed=1
my_rect=pygame.Rect((150,100),(200,100))

color_rect=WHITE
x_ball=20
y_ball=150

r_ball=20
color_ball=RED
game_end=False
while not game_end:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_end=True
            
    if my_rect.collidepoint((x_ball,y_ball)):
        color_ball=GREEN
    else:
        color_ball=RED
        
    screen.fill(BLACK)
    x_ball+=speed
        
    pygame.draw.rect(screen, color_rect, my_rect)
    pygame.draw.circle(screen, color_ball, (x_ball, y_ball), r_ball)
    pygame.display.flip()        
    
pygame.quit()        