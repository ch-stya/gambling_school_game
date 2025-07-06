from config import (SCREEN_SURFACE, LARGEUR_SCREEN, HAUTEUR_SCREEN, LARGEUR_CARD, HAUTEUR_CARD, MARGE, FPS)

class Card:
    def __init__(self, images, symbole, num):
        self.image = images[symbole]
        self.symbole = symbole
        self.rect = self.image.get_rect()
        if num == 0 :
            # carte 1 du joueur
            self.rect.x = LARGEUR_SCREEN/2-LARGEUR_CARD/2-LARGEUR_CARD-MARGE
        elif num == 1 :
            # carte 2 du joueur
            self.rect.x = LARGEUR_SCREEN/2-LARGEUR_CARD/2
        else :
            # carte 3 du joueur
            self.rect.x = LARGEUR_SCREEN/2-LARGEUR_CARD/2+LARGEUR_CARD+MARGE
        self.rect.y = HAUTEUR_SCREEN-HAUTEUR_CARD-MARGE
        self.etat = 'down'

    def draw(self) :
        SCREEN_SURFACE.blit(self.image, self.rect)
        return None
    
    def go_up(self) :
        """
        Déplacement d'une carte vers le haut (lorsqu'on la sélectionne).    
        """
        if self.etat != 'up':
            self.target_y = self.rect.y - 50
            self.etat = 'moving_up'
        return None
    
    def go_down(self):
        """
        Déplacement d'une carte vers le bas (lorsqu'on la sélectionne).    
        """
        if self.etat != 'down' :
            self.target_y = self.rect.y + 50
            self.etat = 'moving_down'
        return None


    def update(self) :
        """
        Affichage des mouvements de la carte, frame par frame.    
        """
        if self.etat == 'moving_up' :
            if self.rect.y > self.target_y :
                self.rect.y -= 5
                if self.rect.y <= self.target_y:
                    self.rect.y = self.target_y
                    self.etat = 'up'
            else :
                self.etat = 'up'
        elif self.etat == 'moving_down' :
            if self.rect.y < self.target_y :
                self.rect.y += 5
                if self.rect.y >= self.target_y:
                    self.rect.y = self.target_y
                    self.etat = 'down'
            else :
                self.etat = 'down'
        return None