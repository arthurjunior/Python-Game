import pygame
import os
import random
import time

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
BG = pygame.image.load(os.path.join("assets","background-black.png"))

#Looping de verificação de de quadros "FPS" e opção de sair
def main():
    run = True
    FPS = pygame.time.Clock()
    
    # estabilazndo o plano de fundo "backgroud" no eixo que fique parado___i
    def redraw_window():
        WIN.blit(BG, (0,0))
        
        pygame.display.update()
    #______________________________________________________________________l
    
    
    while run:
        clock.tick(FPS)
        redraw_window() # Chamando a função para dentro do looping
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
main()                
                