import pygame as pg
from pygame.locals import *
import random
import numpy as np
from tp4 import point_aleatoire
from Vecteur import Vecteur

#simulation d'une bille tombant dans une boite sans ouverture, les rebords sont rebondissants
# Constantes
GRAVITE = 9.81
dt = 1

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLUE = (0, 0, 255)


class quadrilatere() :
    def __init__(self):
        point1x = random.randint(0, 500)
        point1y = random.randint(50, 300)

        point2x = random.randint(500, 800)
        point2y = random.randint(50, 300)

        point3x = random.randint(50, 500)
        point3y = random.randint(300, 600)

        point4x = random.randint(500, 800)
        point4y = random.randint(300, 600)

        self.points = [(point1x, point1y), (point2x, point2y), (point3x, point3y), (point4x, point4y)]
        self.bounding_box = self.trouver_bounding_box()

    def trouver_bounding_box(self):
        """retourne les positions limites de la base"""
        xs, ys = zip(*self.points)
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        print(f"min_x: {min_x}, min_y: {min_y}, max_x: {max_x}, max_y: {max_y}")
        return min_x, min_y, max_x, max_y

    def points_du_quadrilatere(self):
        return self.points

    def get_bounding_box(self):
        """Retourne les coordonnées de la boîte englobante"""
        min_x, min_y, max_x, max_y = self.bounding_box
        return min_x, min_y, max_x, max_y

    def dessiner_quadrilaletare(self, screen, couleur, epaisseur):
        """Dessine le quadrilatère sur l'écran"""
        Points = self.points_du_quadrilatere()
        pg.draw.line(screen, couleur, Points[0], Points[1], epaisseur)
        pg.draw.line(screen, couleur, Points[2], Points[3], epaisseur)
        pg.draw.line(screen, couleur, Points[0], Points[2], epaisseur)
        pg.draw.line(screen, couleur, Points[1], Points[3], epaisseur)
    


class balle():
    def __init__(self, taille, v_initial, hauteur_balle):
        self.taille = taille
        self.v_initial = v_initial 
        self.hauteur_balle = hauteur_balle
        self.position = Vecteur([0, 0])
        self.y = self.position[1]
        self.x = self.position[0]
    

    def point_aleatoire_quadri(self,quadrilatere):
        min_x, min_y, max_x, max_y = quadrilatere.get_bounding_box()
        self.position = Vecteur([random.randint(min_x+self.hauteur_balle, max_x -self.hauteur_balle), min_y - self.hauteur_balle]) #on fait tomber la bille de hauteur_balle pixels au dessus de la boite)]
    
    def dessiner_balle(self, screen, couleur, quadrilatere):
        """Dessine la balle sur l'écran en prenant en compte le quadrilatére"""
        self.point_aleatoire_quadri(quadrilatere)
        pg.draw.circle(screen, couleur, (self.position[0], self.position[1]), self.taille)

    def deplacer_balle(self, dt):
        """Déplace la balle en fonction de la gravité"""
        self.y += self.v_initial * dt + 0.5 * GRAVITE * dt ** 2
        self.v_initial += GRAVITE * dt
        self.position = Vecteur([self.x, self.y])
        print(f"Position de la balle: {self.position}")
        if self.position[1] >= 600 - self.taille:
            self.v_initial = -self.v_initial
            self.position[1] = 600 - self.taille

    def rebondir(self, quadrilatere):
        """Gère le rebond de la balle sur les bords du quadrilatère"""
        min_x, min_y, max_x, max_y = quadrilatere.get_bounding_box()
        if self.position[0] <= min_x + self.taille or self.position[0] >= max_x - self.taille:
            self.v_initial = -self.v_initial
            self.position[0] = min(max(self.position[0], min_x + self.taille), max_x - self.taille)
        if self.position[1] <= min_y + self.taille or self.position[1] >= max_y - self.taille:
            self.v_initial = -self.v_initial
            self.position[1] = min(max(self.position[1], min_y + self.taille), max_y - self.taille)

    

###Ecran
# Générer une fenêtre de 800x600
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Bille dans une boite")

#dessiner le quadrilatere
q1 = quadrilatere()


#dessiner la balle
b1 = balle(10, 0, 20)
b1.dessiner_balle(screen, ROUGE, q1)



running = True
while running:
    for event in pg.event.get():
        if event.type == QUIT:
            running = False

    
    # Remplir l'écran de blanc
    screen.fill(BLANC)
    # Dessiner le quadrilatère
    q1.dessiner_quadrilaletare(screen, BLUE, 2)
    # Dessiner la balle
    b1.dessiner_balle(screen, ROUGE, q1)
    # Mettre à jour la position de la balle
    b1.deplacer_balle(dt)
    # Gérer le rebond de la balle
    b1.rebondir(q1)
   

    
    # Mettre à jour l'affichage
    pg.display.flip()
    

