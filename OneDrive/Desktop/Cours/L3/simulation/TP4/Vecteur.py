#poutou
import numpy as np


class Vecteur() :
    def __init__(self,*elts) :
        self.composants = list(elts if len(elts) > 1 else elts[0])

    def __len__(self):
        return len(self.composants)
    
    def __iter__(self):
        for comp in self.composants :
            yield comp
    
    def __getitem__(self,i):
        return self.composants[i]
    
    def __setitem__(self,i,val):
        if(i<len(self) and i>=0):
            self.composants[i] = val
        else:
            self.composants.append(val)
    
    def __contains__(self,element):
        return element in self.composants
    
    def __str__(self):
        return "("+",".join(map(str,self.composants))+")"
    
    def __repr__(self):
        return "Vecteur"+"("+",".join(map(str,self.composants))+")"

    
    def __eq__(self, autreVecteur):
        epsilon=10e-6
        if(isinstance(autreVecteur, Vecteur)):
            if(len(self) != len(autreVecteur)):
                return False
            else:
                return all([abs(x1-x2)<epsilon for x1,x2 in zip(self,autreVecteur)])
            
    def __ne__(self, autreVecteur):
        return not (self == autreVecteur)

    def __add__(self,autreVecteur) :
        if not isinstance(autreVecteur,Vecteur) :
            raise ValueError("Addition entre vecteurs seulement")
        if len(self) != len(autreVecteur) :
            raise ValueError("Les deux vecteurs n'ont pas la même dimension")
        else :
            return Vecteur([x1+x2 for x1,x2 in zip(self,autreVecteur)])
            
    def __mul__(self,num):
        return Vecteur([num*x for x in self])
    
    def __rmul__(self,num):
        return self.__mul__(num)
    
    def __matmul__(self, autreVecteur):
        if not isinstance(autreVecteur, Vecteur):
            raise ValueError("Produit scalaire entre vecteurs seulement")
        if (len(self) != len(autreVecteur)):
            raise ValueError("Les deux vecteurs n'ont pas la même dimension")
        else:
            return sum([x1*x2 for x1,x2 in zip(self,autreVecteur)])
    
    def __abs__(self):
        return (self@self)**(1/2)
    
    def __truediv__(self, num):
       return Vecteur([x/num for x in self])
    
    def __floordiv__(self, num):
        return Vecteur([x//num for x in self])
    
    def __pow__(self, num):
        return Vecteur([x**num for x in self])
    
    def __sub__(self, autreVecteur):
        if not isinstance(autreVecteur,Vecteur) :
            raise ValueError("Soustraction entre vecteurs seulement")
        if len(self) != len(autreVecteur) :
            raise ValueError("Les deux vecteurs n'ont pas la même dimension")
        else : 
            return Vecteur([x1-x2 for x1,x2 in zip(self,autreVecteur)])
    
    def normaliser(self):
        self.composants = [x/abs(self) for x in self]

    def produit_vectoriel(self,autreVecteur):
        if not isinstance(autreVecteur,Vecteur):
            raise ValueError("Produit vectoriel entre vecteurs seulement")
        if len(self) != 3 or len(autreVecteur) != 3 :
            raise ValueError("Les deux vecteurs doivent être de dimension 3")
        else :
            x1,y1,z1 = self
            x2,y2,z2 = autreVecteur
            return Vecteur(y1*z2 -z1*y2,z1*x2-x1*z2,x1*y2-y1*x2)
    
    def est_base_orthonormee(listeVecteurs : list):
        epsilon = 1e-6 #tolerance, on peut se rapprocher de 0
        if not (Vecteur.est_base_orthogonale(listeVecteurs)):
            return False         
        for i,v1 in enumerate(listeVecteurs):
            if abs(abs(v1)-1) > epsilon or abs(v1) < epsilon: #on rejette les vecteurs de norme differente de 1 ou nulle
                return False
        return True

    def est_base_orthogonale(listeVecteurs : list):
        if(len(listeVecteurs)!= len(listeVecteurs[0])):
            return False
        epsilon = 10e-6
        for i in range(len(listeVecteurs)):
            for j in range(i+1,len(listeVecteurs)):
                if abs(listeVecteurs[i]@listeVecteurs[j]) > epsilon : #on rejette les vecteurs non orthogonaux
                    return False
        return True
        
        
def ieme_canonique(dim_espace : int, postion : int):
    l=[]
    for i in range(dim_espace):
        if(i==(postion-1)):
            l.append(1)
        else : 
            l.append(0)
    return Vecteur(l)

def construire_base_canonique(dim_espace):
    l=[]
    for i in range(dim_espace): 
        l.append(ieme_canonique(dim_espace, i+1))
    return l 
    
    
   
if __name__== "__main__":

    "__call__  --> pour que la matrice agit comme une fonction qui prend un vecteur " 
    print("HELLLLO")
    v1 = Vecteur([1,1,1,-1,1,1])
    v2 = Vecteur(1,1,1,1,-1,1)
    v3 = Vecteur([Vecteur([1,2,3]),Vecteur(4,5,6),Vecteur(7,8,9)])
    print(abs(v1))
    print(v3)
    print(v1+v2)
    print(3*v1)
    print(v1@v2)
    print(v1[1])
    print(len(v1))
    print(v1==v1, v1 == v2)
    v1[1] = 5
    print(v1[1:3])
    print(30 in v1)
    print(v1!=v2, v1 != v1)
    print((v1/3)**2)
    print(v2)
    print(abs(v2))
    v2.normaliser()
    print(v2)
    print(abs(v2))
    print(Vecteur.est_base_orthonormee([Vecteur(1,0,0),Vecteur(0,1,0),Vecteur(0,0,1)]))
    print(Vecteur.est_base_orthonormee([Vecteur(1,1,0),Vecteur(0,1,0),Vecteur(0,0,1)]))
    print(ieme_canonique(23,7))
    print(construire_base_canonique(10))
    vt= Vecteur([])
    print(vt)
    vt[0] = 3
    print(vt)
    vt[1] = 5
    V6 = np.array([Vecteur([1,2,3,4,5,6]), Vecteur([7,8,9,10,11,12]), Vecteur([13,14,15,16,17,18])])
    print(V6[0][4])
    print([V6[x][0] for x in range(len(V6))])
