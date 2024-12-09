import pygame

pygame.init()

WIDTH = 500
HEIGHT = 300
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
GREEN=(0,255,0)
RED=(255,0,0)
BLACK = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock()

speed = 1
my_rect = pygame.Rect((150, 100), (200, 100))
color_rect = RED

is_pressed=False

game_end = False
while not game_end:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                x,y=pygame.mouse.get_pos()
                is_pressed=True
                
    if is_pressed:
        if (my_rect.x<=x<=my_rect.x+my_rect.width and my_rect.y<=y<=my_rect.y+my_rect.height):
            if color_rect==RED:
                color_rect=GREEN
            else:
                color_rect=RED
        is_pressed=False
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, color_rect, my_rect)
    pygame.display.flip()
        
pygame.quit()
    