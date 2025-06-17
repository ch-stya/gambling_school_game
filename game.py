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
from config import SCREEN_RESOLUTION, VALID_BUTTON_COO, VALID_BUTTON_RADIUS
from utils import load_image, fill_box, affichage, pick_player_cards, dist, allow_validation, draw_validation


def run_game():
    pygame.init()
    pygame.display.set_caption("Kakegurui - Rock-Paper-Scissors")
    screen = pygame.display.set_mode(SCREEN_RESOLUTION)
    clock = pygame.time.Clock()

    # Main code
    box = fill_box() # Remplissage de la boîte
    box, ia_game = pick_player_cards(box) # Jeu de l'IA
    box, player_game = pick_player_cards(box) # Jeu du joueur

    print(ia_game)
    print(player_game)

    
    card_state = {'player_card1' : 0,
              'player_card2' : 0,
              'player_card3' : 0,} #0 down, 1 up
    
    

    launched = True
    while launched:
        player_card1, player_card2, player_card3 = affichage(player_game)
        validate = allow_validation(card_state)
        if validate :
            draw_validation()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                launched = False
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                if event.button == 1 : #clic gauche effectué
                    mouse_pos = pygame.mouse.get_pos() #récupère la position du clic
                    if player_card1.collidepoint(mouse_pos) and (card_state['player_card1'] == 0) :                   
                        #card_go_up(player_card1)
                        card_state['player_card1'] = 1 #état up
                    elif player_card2.collidepoint(mouse_pos) and card_state['player_card2'] == 0 :                   
                        #card_go_up(player_card2)     
                        card_state['player_card2'] = 1 
                    elif player_card3.collidepoint(mouse_pos) and card_state['player_card3'] == 0 :                   
                        #card_go_up(player_card3)     
                        card_state['player_card3'] = 1
                    elif not player_card1.collidepoint(mouse_pos) and not player_card2.collidepoint(mouse_pos) and not player_card3.collidepoint(mouse_pos):
                        #en cas de clic sur aucunes cartes, les remets toutes à emplacement initial
                        for cle in card_state :
                            if card_state[cle] == 1 :
                                #card_go_down(eval(cle))
                                card_state[cle] = 0
                    if validate :
                        if dist(VALID_BUTTON_COO, mouse_pos) < VALID_BUTTON_RADIUS+2 :
                            #le joueur à validé son choix
                            print("Choix validé, let's play ! ")
            
        pygame.display.flip() #maj affichage
        clock.tick(60)

    pygame.quit()