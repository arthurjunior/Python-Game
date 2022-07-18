
import pygame
import os
import random
import time
pygame.font.init()

#declarando a LARGURA DO DISPLAY em uma constante 
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Space war python")

#Navi inimigas imagens

RED_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))

#JOGADOR PRINCIPAL

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))

#LASERS
RED_SPACE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
GREEN_SPACE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
BLUE_SPACE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
YELLOW_SPACE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

#BACKGROUD
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")),(WIDTH, HEIGHT))

class Ship:
    def _init_(self, x, y, health = 100):
        self.x = x
        self.y = yself.health = health
        self.ship_img = None
        self.lase_img = None
        self.lasers = []
        self.cool_down_counter = 0

#Looping de verificação de de quadros "FPS" e opção de sair
#declarando variais do game
def main():
    run = True
    FPS = 60
    level = 1
    life = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    
    clock = pygame.time.Clock()
    
    # estabilazndo o plano de fundo "backgroud" no eixo que fique estatico___i
    def redraw_window():
        WIN.blit(BG, (0,0))
        #draw text player status 
        life_label = main_font.render(f"Vida: {life}",1,(255,255,255))
        level_label = main_font.render(f"Level: {level",1,(255,255,255))

        WIN.blit(life_lebel, (10,10))
        WIN.blit(level_lebel, (WIDTH - level_label.get_width() - 10,10))
        
        pygame.display.update()
    #______________________________________________________________________l
    
    
    while run:
        clock.tick(FPS)
        redraw_window() # Chamando a função para dentro do looping
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
main()                
                