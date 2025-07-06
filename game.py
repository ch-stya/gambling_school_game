"""
Ballot Rock-Paper-Scissors
Le premier jeu  de Gambling School.
Une classe place au hasard une carte (feuille, papier ou ciseau) dans un pot.
Les 2 joueurs reçoivent 3 cartes aux hasard venant de ce pot.
Puis viens se jouer une partie de pierre-feuille-ciseaux. En cas draw, on continue
à jouer jusqu'à ce que les 3 cartes soient utilisées.
Le premier à remporter une manche gagne la partie.
"""

import pygame
from config import SCREEN_RESOLUTION, VALID_BUTTON_COO, VALID_BUTTON_RADIUS, FPS
from utils import load_image, fill_box, affichage, pick_player_cards, dist, allow_validation, draw_validation
from entities import Card


def run_game():
    pygame.init()
    pygame.display.set_caption("Kakegurui - Rock-Paper-Scissors")
    screen = pygame.display.set_mode(SCREEN_RESOLUTION)
    clock = pygame.time.Clock()

    # Images
    images = {
        "rock" : load_image("Cards/rock_card(170x220).png"),
        "scissors" : load_image("Cards/scissors_card(170x220).png"),
        "back" : load_image("Cards/back_cards(170x220).png"),
        "paper" : load_image("Cards/paper_card(170x220).png"),
        "img_yumeko" : load_image("yumeko(3)(300x250).png"),
        "img_saotome" : load_image("saotome_pretty(240x320).png"),
        "img_fond" : load_image("Fonds/fond(1).jpg")
    }

    # Main code
    box = fill_box() # Remplissage de la boîte
    box, ia_game = pick_player_cards(box) # Jeu de l'IA
    box, player_game = pick_player_cards(box) # Jeu du joueur
    print(ia_game)
    print(player_game)
    
    # Création des objets cartes
    playercard1 = Card(images, player_game[0], 0)
    playercard2 = Card(images, player_game[1], 1)
    playercard3 = Card(images, player_game[2], 2)
    player_cards = [playercard1, playercard2, playercard3]
    
    launched = True
    while launched:
        affichage(images)
        for card in player_cards :
            # Affichage des cartes du joueur
            card.update()
            card.draw()
        validate = allow_validation(player_cards)
        if validate :
            draw_validation()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                launched = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if event.button == 1 : #clic gauche effectué
                    mouse_pos = pygame.mouse.get_pos() #récupère la position du clic
                    for card in player_cards:
                        if card.rect.collidepoint(mouse_pos) and card.etat == 'down' :
                            card.go_up()
                        elif not card.rect.collidepoint(mouse_pos) and card.etat == 'up' :
                            card.go_down() 
                    if validate :
                        if dist(VALID_BUTTON_COO, mouse_pos) < VALID_BUTTON_RADIUS+2 :
                            #le joueur à validé son choix
                            print("Choix validé, let's play ! ")
            
        pygame.display.flip() #maj affichage
        clock.tick(FPS)

    pygame.quit()