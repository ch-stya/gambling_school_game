import pygame

LARGEUR_SCREEN = 1400
HAUTEUR_SCREEN = 900
SCREEN_RESOLUTION = (LARGEUR_SCREEN, HAUTEUR_SCREEN)
SCREEN_SURFACE  = pygame.display.set_mode(SCREEN_RESOLUTION)
BLUE_COLOR = (89, 152, 255) #(R, G, B) taux de red, green, blue (0-255)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
LARGEUR_CARD = 170
HAUTEUR_CARD = 220
MARGE = 40
VALID_BUTTON_COO = (LARGEUR_SCREEN-MARGE*4, HAUTEUR_SCREEN/2)
VALID_BUTTON_RADIUS = 45
TOTAL_STUDENTS = 24
SYMBOLS = ['rock', 'paper', 'scissors']
SYMBOLS_WIN = {'rock' : 'scissors',
               'scissors' : 'paper',
               'paper' : 'rock' }


