import pygame as pg
from pygame.locals import *
import random
import numpy as np
from tp4 import point_aleatoire
from Vecteur import Vecteur
from quadrilatere import quadrilatere
from balle import balle

#simulation d'une bille tombant dans une boite sans ouverture, les rebords sont rebondissants
# Constantes

dt =1/40
# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLUE = (0, 0, 255)
   

###Ecran
# Générer une fenêtre de 800x600
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Bille dans une boite")

#dessiner le quadrilatere
q1 = quadrilatere()

#dessiner la balle
b1 = balle(5, 0, 20)
b1.point_aleatoire_quadri(q1)
b1.dessiner_balle(screen, ROUGE)



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
    b1.dessiner_balle(screen, ROUGE)
    # Mettre à jour la position de la balle
    b1.deplacer_balle(dt)
    b1.rebondir(q1)


  
   

    
    # Mettre à jour l'affichage
    pg.display.flip()
    

