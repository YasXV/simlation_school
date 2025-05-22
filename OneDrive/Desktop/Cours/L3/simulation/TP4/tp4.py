from Vecteur import Vecteur
import os
import numpy as np 
import matplotlib.pyplot as plt

#constante
lam_bda = 0.1
prescision = 10e-6
nbr_limite_iterations = 10000

def f(xy : Vecteur) -> float:
    """Fonction à minimiser"""
    x, y = xy[0], xy[1]
    return (x**2/10 - x + np.sin(y))**2 + (y**2/10 - y + np.cos(x))**2

def point_aleatoire(n):
    """Génère un point aléatoire dans l'espace de dimension n"""
    return [np.random.uniform(-10, 10) for _ in range(n)]


def gradient(xy : Vecteur) -> Vecteur:
    """Calcule le gradient de la fonction f(x,y)"""
    x, y = xy[0], xy[1]
    df_dx = 2*(x**2/10 - x + np.sin(y))*(x/5 - 1) - 2*(y**2/10 - y + np.cos(x))*(np.sin(x))
    df_dy = 2*(x**2/10 - x + np.sin(y))*(np.cos(y)) + 2*(y**2/10 - y + np.cos(x))*(y/5 - 1)
    return Vecteur([df_dx, df_dy])


def descente_gradient() -> Vecteur : 
    "Applique l'algorithme de descente de gradient pour minimiser la fonction f(x,y)"
    point_initial = Vecteur(point_aleatoire(2))
    iteration = 0
    point_courant = point_initial
    trajet = [point_courant]
    grad_courant = gradient(point_courant)
    while abs(grad_courant) > prescision:
        point_courant = point_courant - lam_bda * grad_courant
        trajet.append(point_courant)
        grad_courant = gradient(point_courant)
        iteration += 1
        #print(f"Iteration {iteration}: point courant = {point_courant}, gradient = {grad_courant}")
        if iteration > nbr_limite_iterations:
            print("Nombre d'iterations limite atteint")
            break
    print(f"Point final: {point_courant} où la fonction est minimale, gradient final: {grad_courant} avec {iteration} iterations")
    return (np.array(trajet))


def afficher_courbe_avec_min(fonction):
    """Affiche la courbe de la fonction f(x,y) sous différents angles"""
    #Minimisation de la fonction
    trajet = descente_gradient() #Trajet de la descente de gradient
    point_min = trajet[-1] #Dernier point de la descente de gradient

    #Fonction de la surface
    x = np.linspace(-10,10,100)
    y = np.linspace(-10,10,100)
    X, Y = np.meshgrid(x, y)
    Z = np.array([fonction(Vecteur([x, y])) for x, y in zip(X, Y)])

    fig = plt.figure(figsize=(15, 10))

    #Vue de face (axe Y)
    ax2 = fig.add_subplot(121, projection='3d')
    ax2.plot_surface(X, Y, Z, cmap='terrain', alpha=0.7)
    ax2.scatter(point_min[0], point_min[1], fonction(point_min), color='red', s=100, label='Minimum')
    ax2.legend()
    ax2.view_init(0, 0)
    ax2.set_title("Vue de face (Y)")

    #Vue de côté (axe X)
    '''ax3 = fig.add_subplot(2, projection='3d')
    ax3.plot_surface(X, Y, Z, cmap='terrain', alpha=0.7)
    ax3.scatter(point_min[0], point_min[1], fonction(point_min), color='red', s=100, label='Minimum')
    ax3.plot(trajet[:][0], trajet[:][1], fonction(trajet), color='k',  label='Trajet')
    ax3.legend()
    ax3.view_init(0, 90)
    ax3.set_title("Vue de côté (X)")'''

    #Vue diagonale (3/4)
    ax4 = fig.add_subplot(122, projection='3d')
    ax4.plot_surface(X, Y, Z, cmap='terrain', alpha=0.7)
    ax4.scatter(point_min[0], point_min[1], fonction(point_min), color='red', s=100, label='Minimum')
    ax4.legend()
    ax4.view_init(30, 45)
    ax4.set_title("Vue 3/4")

    #Affichage
    plt.tight_layout()
    plt.show()

    
if __name__ == "__main__":
     afficher_courbe_avec_min(f)
        
    
