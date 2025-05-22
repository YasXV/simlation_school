
import pygame as pg
from pygame.locals import *
import random
import numpy as np
from tp4 import point_aleatoire
from Vecteur import Vecteur



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