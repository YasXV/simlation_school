import pygame as pg
from pygame.locals import *
import random
import numpy as np
from tp4 import point_aleatoire
from Vecteur import Vecteur
from quadrilatere import quadrilatere

GRAVITE = 9.81
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
    
    def dessiner_balle(self, screen, couleur):
        """Dessine la balle sur l'écran en prenant en compte le quadrilatére"""
        if abs(self.position) == 0 :
            raise ValueError("La position de la balle n'est pas définie")
        pg.draw.circle(screen, couleur, (self.position[0], self.position[1]), self.taille)

    def deplacer_balle(self, dt):
        """Déplace la balle en fonction de la gravité"""
        self.position[1] += self.v_initial * dt + 0.5 * GRAVITE * dt**2
        self.v_initial += GRAVITE * dt
        self.y = self.position[1]
        self.x = self.position[0]

    def colision_avec_face_exterieure(self, quadrilatere):
        """Vérifie si la balle touche la face extérieure du quadrilatère"""
        min_x, min_y, max_x, max_y = quadrilatere.get_bounding_box()
        if self.x + self.taille >= min_x and self.x - self.taille <= max_x and self.y + self.taille >= min_y and self.y - self.taille <= max_y:
            return True
        return False
    
    def colision_avec_bord(self, quadrilatere):
        """Vérifie si la balle touche le bord du quadrilatère"""
        min_x, min_y, max_x, max_y = quadrilatere.get_bounding_box()
        if self.x + self.taille >= min_x and self.x - self.taille <= max_x:          
            return True
        return False
    
    def rebondir(self, quadrilatere):
        """Fait rebondir la balle sur le bord du quadrilatère, continue sa chute si il y a colision avec le haut sinon rebondis"""
        min_x, min_y, max_x, max_y = quadrilatere.get_bounding_box()
        if self.colision_avec_bord(quadrilatere):
            self.v_initial = -self.v_initial
            self.position[0] = min_x - self.taille