import pygame
 
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Пульс")

clock=pygame.time.Clock()

FPS=2
i=1
game_end=False
while not game_end:
    clock.tick(FPS) #(500,300),(600,300),(700,400),
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_end=True
    if i>0:
        screen.fill([0,0,0])
        circle_1=(250,400),(350,400)   
        #f_half=(100,400),(150,500),(400,750),(100,400),(200,300),(300,300),(400,400),(700,400),(500,300)
        s_half=(400,700),(200,400),(600,400)
 
        pygame.draw.polygon(screen,(255,0,0),s_half )
        pygame.draw.polygon(screen,(255,0,0), ((300,400),(450,700),(400,700) ))
        pygame.draw.circle(screen,(255,0,0), [300,400],100)
        pygame.draw.circle(screen,(255,0,0), [500,400],100)
        i=-1
        pygame.display.flip()
    """
    else:
        screen.fill([0,0,0])
        pygame.draw.rect(screen,(255,0,0),[150,150,100,100])
        i=1
        pygame.display.flip()
    """
pygame.quit()
