from random import randint
from PIL import Image
import pygame
import time
import math

"""
Ballot Rock-Paper-Scissors
Le premier jeu  de Gambling School.
Une classe place au hasard une carte (feuille, papier ou ciseau) dans un pot.
Les 2 joueurs reçoivent 3 cartes aux hasard venant de ce pot.
Puis viens se jouer une partie de pierre-feuille-ciseaux. En cas draw, on continue
à jouer jusqu'à ce que les 3 cartes soient utilisées.
"""

def conversion_img(chemin, res) :
    """
    Fonction servant à convertir une image avec  Pillow.
    Ecrire "from PIL import Image" en début de programme pour l'utiliser.
    Entrées : Chemin de l'image, nouvelle résolution souhaitée
    -> Convertit l'image et la place dans le même dossier, avec  taille de l'image dans le nom.
    """
    # Conversion d'une image avec Pillow (à ne faire qu'une fois)
    image = Image.open(chemin)
    # Redimensionnement de l'image
    nouvelle_image = image.resize(res)
    chemin = chemin[:-4]
    # Enregistrement de la nouvelle image
    nouvelle_image.save(chemin + "(" + str(res[0]) + "x" + str(res[1]) + ").png")

#conversion_img("Images/valid_icon.png", (100, 100))
#conversion_img("Images/saotome_pretty.png", (240, 320))

# Données
pygame.init()
# Chargement des images
largeur_win = 1400
hauteur_win = 900
window_resolution = (largeur_win, hauteur_win)
pygame.display.set_caption("Kakegurui - Rock-Paper-Scissors")
window_surface  = pygame.display.set_mode(window_resolution)
img_rock_card = pygame.image.load("assets/images/Cards/rock_card(170x220).png") 
img_rock_card.convert_alpha() 
img_back_card = pygame.image.load("assets/images/Cards/back_cards(170x220).png") 
img_back_card.convert_alpha() 
img_scissors_card = pygame.image.load("assets/images/Cards/scissors_card(170x220).png") 
img_scissors_card.convert_alpha() 
img_paper_card = pygame.image.load("assets/images/Cards/paper_card(170x220).png") 
img_paper_card.convert_alpha() 
img_yumeko = pygame.image.load("assets/images/yumeko(3)(300x250).png")
img_yumeko.convert_alpha()
img_saotome = pygame.image.load("assets/images/saotome_pretty(240x320).png")
img_saotome.convert_alpha()
img_fond = pygame.image.load("assets/images/Fonds/fond(1).jpg")
img_validate_button = pygame.image.load("assets/images/valid_icon(100x100).png")
img_validate_button.convert_alpha()
img_saotome.convert() 

symbols_img = {'rock' : img_rock_card,
               'scissors' : img_scissors_card,
               'paper' : img_paper_card }
card_state = {'player_card1' : 0,
              'player_card2' : 0,
              'player_card3' : 0,} #0 down, 1 up
nb_students = 24
symbol_win = {'rock' : 'scissors',
               'scissors' : 'paper',
               'paper' : 'rock' }
symbol = ['rock', 'paper', 'scissors']
blue_color = (89, 152, 255) #(R, G, B) taux de red, green, blue (0-255)
black_color  = (0, 0, 0)
white_color = (255, 255, 255)
largeur_card = 170
hauteur_card = 220
marge = 40
circle_valid_coo = (largeur_win-marge*4, hauteur_win/2)
circle_valid_radius = 45
validate = False
    
# Fonctions
def fill_box() :
    """
    Remplit la boîte avec des figures aléatoire, 1 carte par élève. 
    """
    box  = []
    for i in range(nb_students) :
        rand = randint(0,2)
        box = box + [symbol[rand]]
    return box

def pick_player_cards() :
    """
    Tire 3 cartes pour définir le jeu d'un joueur.
    Lorsqu'une carte est tiré, elle est retirée de la boîte.
    """
    global box
    # Tire 3 cartes
    player_cards = []
    for i in range(3) : 
        a  = randint(0,len(box)-1)
        player_cards = player_cards + [box[a]]
        box.remove(box[a])
    return player_cards

def affichage() :
    """
    Appelle tout ce qui est nécessaire à afficher.
    """
    global validate
    #affichage du fond
    window_surface.blit(img_fond, (-520, -220))
    #affichage Yumeko dans le coin droit de la  fenêtre
    window_surface.blit(img_yumeko, (largeur_win-300, hauteur_win-250))
    #affichage Saotome dans le coin gauche de la  fenêtre
    window_surface.blit(img_saotome, (0, hauteur_win-300))      
    #affichage carte 1,2,3 IA
    window_surface.blit(img_back_card, (largeur_win/2-largeur_card/2-largeur_card-marge, marge))
    window_surface.blit(img_back_card, (largeur_win/2-largeur_card/2, marge))
    window_surface.blit(img_back_card, (largeur_win/2-largeur_card/2+largeur_card+marge, marge))
    #affichage carte 1,2,3 joueur
    window_surface.blit(symbols_img[player_game[0]], player_card1)
    window_surface.blit(symbols_img[player_game[1]], player_card2)
    window_surface.blit(symbols_img[player_game[2]], player_card3)
    validate = False
    #affichage du bouton validé si une carte est sélectionné
    for cle in card_state :
        if card_state[cle] == 1 :           
            pygame.draw.circle(window_surface, white_color, circle_valid_coo, circle_valid_radius) #taille ecran, couleur, position, rayon
            window_surface.blit(img_validate_button, (largeur_win-marge*5.3, hauteur_win/2-marge*1.25))
            validate = True
    return None
    
def card_go_up(card) :
    """
    Déplacement d'une carte vers le haut (lorsqu'on la sélectionne).    
    """
    global card_state
    # Vérifie qu'il n'y a pas une autre carte de levé, si oui, la replace à son état initial.
    if card_state['player_card1'] == 1 :
        card_go_down(player_card1)
        card_state['player_card1'] = 0
    elif card_state['player_card2'] == 1 :
        card_go_down(player_card2)
        card_state['player_card2'] = 0
    elif card_state['player_card3'] == 1 :
        card_go_down(player_card3)
        card_state['player_card3'] = 0
    i=0
    while i < 10 :
        time.sleep(.010) #milliseconde, sinon par défaut c'est en seconde
        card.move_ip(0, -5) #déplace de 5 (x, y)
        affichage()
        pygame.display.flip() #maj affichage
        i += 1  #incrémentation de i#clic gauche
    return None
    

def card_go_down(card) :
    """
    Déplacement d'une carte vers le bas.
    """
    i=0
    while i < 10 :
        time.sleep(.010) #milliseconde, sinon par défaut c'est en seconde
        card.move_ip(0, 5) #déplace de 5 (x, y)
        affichage()
        pygame.display.flip() #maj affichage
        i += 1  #incrémentation de i#clic gauche
    return None
        
def dist(coo_point1, coo_point2) :
    """
    Calcule la distance entre deux points.
    Entrées : Tuple contenant les coordonnées du point1, Tuple contenant les coordonnées du point2
    """
    x1, y1 = coo_point1
    x2, y2 = coo_point2
    distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
    return distance

# Main code
window_surface.fill(blue_color) #couleur de fond (en cas si l'image ne se charge pas)
box = fill_box() # Remplissage de la boîte
ia_game = pick_player_cards() # Jeu de l'IA
player_game = pick_player_cards() # Jeu du joueur

#carte 1 joueur (objet rect)
player_card1 = symbols_img[player_game[0]].get_rect()
player_card1.x = largeur_win/2-largeur_card/2-largeur_card-marge
player_card1.y = hauteur_win-hauteur_card-marge    
#carte 2 joueur
player_card2 = symbols_img[player_game[1]].get_rect()
player_card2.x = largeur_win/2-largeur_card/2
player_card2.y = hauteur_win-hauteur_card-marge    
#carte 3 joueur
player_card3 = symbols_img[player_game[2]].get_rect() 
player_card3.x = largeur_win/2-largeur_card/2+largeur_card+marge
player_card3.y = hauteur_win-hauteur_card-marge

print(ia_game)
print(player_game)

launched = True
while launched:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            launched = False
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            if event.button == 1 : #clic gauche effectué
                mouse_pos = pygame.mouse.get_pos() #récupère la position du clic
                if player_card1.collidepoint(mouse_pos) and (card_state['player_card1'] == 0) :                   
                    card_go_up(player_card1)
                    card_state['player_card1'] = 1 #état up
                elif player_card2.collidepoint(mouse_pos) and card_state['player_card2'] == 0 :                   
                    card_go_up(player_card2)     
                    card_state['player_card2'] = 1 
                elif player_card3.collidepoint(mouse_pos) and card_state['player_card3'] == 0 :                   
                    card_go_up(player_card3)     
                    card_state['player_card3'] = 1
                elif not player_card1.collidepoint(mouse_pos) and not player_card2.collidepoint(mouse_pos) and not player_card3.collidepoint(mouse_pos):
                    #en cas de clic sur aucunes cartes, les remets toutes à emplacement initial
                    for cle in card_state :
                        if card_state[cle] == 1 :
                            card_go_down(eval(cle))
                            card_state[cle] = 0
                if validate :
                    if dist(circle_valid_coo, mouse_pos) < circle_valid_radius+2 :
                        #le joueur à validé son choix
                        print("Choix validé, let's play ! ")
           
    # Corps du programme
    # Affichage
    affichage()
    pygame.display.flip() #maj affichage

pygame.quit()