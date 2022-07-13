import pygame
import os
import random
import time

#declarando a LARGURA DO DISPLAY em uma constante 
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Space war python")

#NAVE imagens

RED_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))

#JOGADOR PRINCIPAL

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_yellow_small.png"))

#LASERS
RED_SPACE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_red_small.png"))
GREEN_SPACE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_green_small.png"))
BLUE_SPACE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_blue_small.png"))
YELLOW_SPACE_LASER = pygame.image.load(os.path.join("assets","pixel_laser_yellow_small.png"))

#BACKGROUD
BG = pygame.image.load(os.path.join("assets","background-black.png"))

