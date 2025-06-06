import pygame
import math

# Initialisation de Pygame
pygame.init()

# Définition de la couleur blanche
WHITE = (255, 255, 255)

# Définition de la taille de la fenêtre
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Définition des coordonnées du cercle
coo_circle = (320, 240)
circle_radius = 50

def dist(coo_point1, coo_point2) :
    x1, y1 = coo_point1
    x2, y2 = coo_point2
    distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
    return distance

print(dist((280,210),(360,265)))
    

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Récupération des coordonnées du clic de la souris
            mouse_x, mouse_y = event.pos
            circle_x, circle_y = coo_circle
            
            print(mouse_x, mouse_y)
            print(mouse_x - circle_x )
            print(mouse_y - circle_y )
            # Vérification si le clic est dans le cercle
            if dist((mouse_x, mouse_y), coo_circle) < circle_radius :
            #if (mouse_x > coo_circle[0]-circle_radius+10 and mouse_x < coo_circle[0]+circle_radius-10 and mouse_y > coo_circle[1]-circle_radius+10 and mouse_y < coo_circle[1]+circle_radius-10) :
                print("Clic dans le cercle !")

    
    # Dessin du cercle
    pygame.draw.circle(screen, WHITE, coo_circle, circle_radius)
    
    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()