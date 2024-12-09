import pygame

class play:
    def __init__(self, screen_width, screen_height):
        self.__screen_width=91
        self.__screen_height=91
        self.__sprite = pygame.transform.smoothscale(
            pygame.image.load("ufoRed.png").convert_alpha(),
            (self.__screen_width, self.__screen_height)
        )
    
        self.__ufo_x=20
        self.__ufo_y=20
            
        self.__speed=15    
        self.__move_x=0
        self.__move_y=0
    def check_event(self, event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                self.__move_y=1
            if event.key==pygame.K_w:
                self.__move_y=-1
            if event.key==pygame.K_a:
                self.__move_x=-1            
            if event.key==pygame.K_d:
                self.__move_x=1   
    
    def check_logic(self, screen_width, screen_height):
        if self.__ufo_x<0 or self.__ufo_x>self.__width-self.__screen_width:
            self.__ufo_x+=self.__ufo_speed*self.__move_x*-1
        if self.__ufo_y<0 or self.__ufo_y>self.__height-self.__screen_height:
            self.__ufo_y+=self.__ufo_speed*self.__move_y*-1 
            
    
    def move(self):
        self.__ufo_x+=self.__ufo_speed*self.__move_x
        self.__ufo_y+=self.__ufo_speed*self.__move_y            
    
    def draw(self, screen):
        screen.blit(self.__sprite,(self.__ufo_x, self.__ufo_y))
        
class Game:
    def __init__(self, width=600,height=600, fps=30):
        pygame.init()
        self.__width=width
        self.__height=height
        self.__screen=pygame.display.set_mode((self.__width, self.__height))
        self.__bg_sprite = pygame.transform.smoothscale(
            pygame.image.load("space.jpg").convert(),
            (self.__width, self.__height)
        )
        self.__fps=fps
        self.__clock=pygame.time.Clock()        
        self.__game_end=False
        
        self.__player=play(self.__width, self.__height)
    
    def __del__(self):
        pygame.quit()    
    
    def run(self):
        while not self.__game_end:
            self.__check_events()
            self.__check_logic()
            self.__move_obj()
            self.__draw()
            
            self.__clock.tick(self.__fps)    
    
    def __check_events(self):
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.__game_end=True
            self.__player.check_event(event)
    
    def __check_logic(self):
        self.__player.check_logic(self.__screen_width, self.__screen_height) 
    
    def __move_obj(self):
        self.__player.move()
     
    
    def __draw(self):
        self.__screen.blit(self.__bg_spritebg,(0,0))
        self.__screen.blit(self.__ufo,(self.__ufo_x,self.__ufo_y))
        pygame.display.flip
    
def main():
    game=Game()
    game.run()
main()