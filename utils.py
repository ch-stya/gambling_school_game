import os
import pygame
from PIL import Image
from random import randint
import time
import math
from config import (SCREEN_RESOLUTION, LARGEUR_SCREEN, HAUTEUR_SCREEN, LARGEUR_CARD, HAUTEUR_CARD, MARGE, WHITE_COLOR, VALID_BUTTON_COO, 
                    VALID_BUTTON_RADIUS, SYMBOLS, TOTAL_STUDENTS, BLUE_COLOR, SCREEN_SURFACE, CARD_STATE, FPS)

def load_image(filename):
    """
    Fonction servant à charger une image.
    Entrée : Nom de l'image (str)
    Sortie : Image chargée
    """
    path = os.path.join("assets", "images", filename)

    try :
        image = pygame.image.load(path)
    except pygame.error as erreur :
        print(f"Impossible de charger l'image : {path}")
        raise SystemExit(erreur)
    
    image = image.convert_alpha()

    return image

def conversion_img(chemin, res) :
    """
    Fonction servant à convertir une image avec  Pillow.
    Ecrire "from PIL import Image" en début de programme pour l'utiliser.
    Entrées : Chemin de l'image (str), nouvelle résolution souhaitée (tuple)
    -> Convertit l'image et la place dans le même dossier, avec  taille de l'image dans le nom.
    -> Exemple d'utilisation : conversion_img("Images/saotome_pretty.png", (240, 320))
    """
    # Conversion d'une image avec Pillow (à ne faire qu'une fois)
    image = Image.open(chemin)
    # Redimensionnement de l'image
    nouvelle_image = image.resize(res)
    chemin = chemin[:-4]
    # Enregistrement de la nouvelle image
    nouvelle_image.save(chemin + "(" + str(res[0]) + "x" + str(res[1]) + ").png")

# Fonctions
def fill_box() :
    """
    Remplit la boîte avec des figures aléatoire, 1 carte par élève. 
    """
    box  = []
    for i in range(TOTAL_STUDENTS) :
        rand = randint(0,2)
        box = box + [SYMBOLS[rand]]
    return box

def generate_player_game(player_game, images):
    SYMBOLS_IMG = {'rock' : images["img_rock_card"],
                   'scissors' : images["img_scissors_card"],
                   'paper' : images["img_paper_card"] }
    
    #carte 1 joueur (objet rect)
    player_card1 = SYMBOLS_IMG[player_game[0]].get_rect()
    player_card1.x = LARGEUR_SCREEN/2-LARGEUR_CARD/2-LARGEUR_CARD-MARGE
    player_card1.y = HAUTEUR_SCREEN-HAUTEUR_CARD-MARGE    
    #carte 2 joueur
    player_card2 = SYMBOLS_IMG[player_game[1]].get_rect()
    player_card2.x = LARGEUR_SCREEN/2-LARGEUR_CARD/2
    player_card2.y = HAUTEUR_SCREEN-HAUTEUR_CARD-MARGE    
    #carte 3 joueur
    player_card3 = SYMBOLS_IMG[player_game[2]].get_rect() 
    player_card3.x = LARGEUR_SCREEN/2-LARGEUR_CARD/2+LARGEUR_CARD+MARGE
    player_card3.y = HAUTEUR_SCREEN-HAUTEUR_CARD-MARGE

    return player_card1, player_card2, player_card3

def affichage(player_game, player_cards, images) :
    """
    Appelle tout ce qui est nécessaire à afficher.
    """
    SYMBOLS_IMG = {'rock' : images["img_rock_card"],
                   'scissors' : images["img_scissors_card"],
                   'paper' : images["img_paper_card"] }
    
    #affichage du fond
    SCREEN_SURFACE.fill(BLUE_COLOR) #couleur de fond (en cas si l'image ne se charge pas)
    SCREEN_SURFACE.blit(images["img_fond"], (-520, -220))
    #affichage Yumeko dans le coin droit de la  fenêtre
    SCREEN_SURFACE.blit(images["img_yumeko"], (LARGEUR_SCREEN-300, HAUTEUR_SCREEN-250))
    #affichage Saotome dans le coin gauche de la  fenêtre
    SCREEN_SURFACE.blit(images["img_saotome"], (0, HAUTEUR_SCREEN-300))      
    #affichage carte 1,2,3 IA
    SCREEN_SURFACE.blit(images["img_back_card"], (LARGEUR_SCREEN/2-LARGEUR_CARD/2-LARGEUR_CARD-MARGE, MARGE))
    SCREEN_SURFACE.blit(images["img_back_card"], (LARGEUR_SCREEN/2-LARGEUR_CARD/2, MARGE))
    SCREEN_SURFACE.blit(images["img_back_card"], (LARGEUR_SCREEN/2-LARGEUR_CARD/2+LARGEUR_CARD+MARGE, MARGE))
    #affichage carte 1,2,3 joueur
    SCREEN_SURFACE.blit(SYMBOLS_IMG[player_game[0]], player_cards["player_card1"])
    SCREEN_SURFACE.blit(SYMBOLS_IMG[player_game[1]], player_cards["player_card2"])
    SCREEN_SURFACE.blit(SYMBOLS_IMG[player_game[2]], player_cards["player_card3"])
    
    return None


def pick_player_cards(box) :
    """
    Tire 3 cartes pour définir le jeu d'un joueur.
    Lorsqu'une carte est tiré, elle est retirée de la boîte.
    Entrée : box contenant la liste d'élements parmis lesquels il faut choisir (liste)
    Sortie : box avec retrait des éléments choisis (liste), deck du joueur (liste)
    """
    # Tire 3 cartes
    player_cards = []
    for i in range(3) : 
        a  = randint(0,len(box)-1)
        player_cards = player_cards + [box[a]]
        box.remove(box[a])
    return box, player_cards

def allow_validation(card_state) :
    carte_up = 0
    for cle in card_state :
        if card_state[cle] == 1 :
            carte_up += 1 
    if carte_up > 0 :        
        return True
    else :
        return False
        
def draw_validation() :
    img_validate_button = load_image("valid_icon(100x100).png")
    pygame.draw.circle(SCREEN_SURFACE, WHITE_COLOR, VALID_BUTTON_COO, VALID_BUTTON_RADIUS) #taille ecran, couleur, position, rayon
    SCREEN_SURFACE.blit(img_validate_button, (LARGEUR_SCREEN-MARGE*5.3, HAUTEUR_SCREEN/2-MARGE*1.25))

        
def dist(coo_point1, coo_point2) :
    """
    Calcule la distance entre deux points.
    Entrées : Tuple contenant les coordonnées du point1, Tuple contenant les coordonnées du point2
    """
    x1, y1 = coo_point1
    x2, y2 = coo_point2
    distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
    return distance


def card_go_up(card, player_cards, player_game, clock, images) :
    """
    Déplacement d'une carte vers le haut (lorsqu'on la sélectionne).    
    """
    # Vérifie qu'il n'y a pas une autre carte de levé, si oui, la replace à son état initial.
    if CARD_STATE['player_card1'] == 1 :
        card_go_down(player_cards["player_card1"], player_game, player_cards, clock, images)
        CARD_STATE['player_card1'] = 0
    elif CARD_STATE['player_card2'] == 1 :
        card_go_down(player_cards["player_card2"], player_game, player_cards, clock, images)
        CARD_STATE['player_card2'] = 0
    elif CARD_STATE['player_card3'] == 1 :
        card_go_down(player_cards["player_card3"], player_game, player_cards, clock, images)
        CARD_STATE['player_card3'] = 0
    i=0
    while i < 10 :
        pygame.event.pump()
        card.move_ip(0, -5) #déplace de 5 (x, y)
        affichage(player_game, player_cards, images)
        pygame.display.flip() #maj affichage
        clock.tick(FPS)
        i += 1  #incrémentation de i#clic gauche
    return None
    

def card_go_down(card, player_game, player_cards, clock, images) :
    """
    Déplacement d'une carte vers le bas.
    """
    i=0
    while i < 10 :
        pygame.event.pump()
        card.move_ip(0, 5) #déplace de 5 (x, y)
        affichage(player_game, player_cards, images)
        pygame.display.flip() #maj affichage
        clock.tick(FPS)
        i += 1  #incrémentation de i#clic gauche
    return None