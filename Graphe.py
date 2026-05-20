import random


def graphe_aleatoire(N):
    grapheMatrice=[[0 for i in range (N)] for j in range (N)]
    grapheListe=[[] for j in range (N)]
    for i in range (N) :
        for j in range (i) : 
            if random.random() < 1/2 :
                grapheMatrice[i][j]=1
                grapheMatrice[j][i]=1
                grapheListe[i].append(j)
                grapheListe[j].append(i)
    return grapheMatrice,grapheListe

def fusion_graphe_poids(matrice, poids):
    for i in range (len(matrice)):
        matrice[i][i]=poids[i]

def matrice_liste(matrice):
    liste=[[]for i in range(len(matrice))]
    poids=[0 for i in range(len(matrice))]
    for i in range(len(matrice)):
        for j in range (len(matrice)):
            if matrice[i][j]==1 and i!=j :
                liste[i].append(j)
            elif i==j:
                poids[i]=matrice[i][i]
    return liste,poids

def liste_matrice(liste, poids):
    matrice=[[0 for i in range (len(liste))] for j in range (len(liste))]
    for i in range (len(liste)):
        for j in liste[i]:
            matrice[i][j]=1
        matrice[i][i]=poids[i]
    return matrice


def the_aleatoire(N):
    poids = []
    for i in range (N) :
        poids.append(random.random())
    return poids

def the_binaire(N):
    poids = [0 for i in range (N)]
    for i in range (N):
        if random.random()<1/2:
            poids[i]=1
    return poids

def the_unique(N):
    poids = [0 for i in range(N)]
    poids[random.randint(0,N-1)]=1
    return poids

import random

def arbre_aleatoire(N):
    """
    Génère un arbre aléatoire connexe à N sommets.

    Retour :
        grapheMatrice : matrice d'adjacence
        grapheListe   : liste d'adjacence
    """

    grapheMatrice = [[0 for _ in range(N)] for _ in range(N)]
    grapheListe = [[] for _ in range(N)]

    # Chaque sommet i>0 est relié à un sommet précédent
    # => garantit un arbre connexe sans cycle
    for i in range(1, N):
        parent = random.randint(0, i - 1)

        grapheMatrice[i][parent] = 1
        grapheMatrice[parent][i] = 1

        grapheListe[i].append(parent)
        grapheListe[parent].append(i)

    return grapheMatrice, grapheListe
        
def enregistrer_matrice(nom_fichier, matrice):
    """
    Enregistre une liste de matrices dans un fichier texte.
    Chaque matrice est séparée par une ligne vide.
    """
    l=len(matrice)
    with open(nom_fichier+'.txt', 'a') as f:
        for ligne in matrice:
                f.write(' '.join(map(str, ligne)) + '\n')
        f.write('\n')  # séparation entre matrices


def lire_matrices(nom_fichier):
    matrices = []
    matrice = []

    with open(nom_fichier+'.txt', 'r') as f:
        for ligne in f:
            ligne = ligne.strip()
            if ligne == "":
                if matrice:
                    matrices.append(matrice)
                    matrice = []
            else:
                matrice.append(list(map(float, ligne.split())))

    # ajouter la dernière matrice si le fichier ne finit pas par une ligne vide
    if matrice:
        matrices.append(matrice)

    return matrices
    
l=[0,1,2,3,4,5,6,7,8,9]   
    

