import Graphe, OperationGraphe

def GLA(liste,poids):
    l=len(liste)
    # Tous les sous-ensembles contenant 0
    resultat = []
    
    # Génération de tous les sous-ensembles
    sous_ensembles = [[0]]
    for v in range(1,l):
        nouveaux = []
        for s in sous_ensembles:
            nouveaux.append(s + [v])
        sous_ensembles.extend(nouveaux)
    
    # On ajoute 0 à chaque sous-ensemble
    for s in sous_ensembles:
        candidat = s
        
        # Test de connexité
        if OperationGraphe.est_connexe(liste, candidat):
            resultat.append(candidat)
            
    max=0
    meilleur=[]
    for element in resultat :
        npoids=OperationGraphe.equilibrage(liste,poids,element)
        if npoids[0] > max :
            max=npoids[0]
            meilleur=element
    return meilleur, OperationGraphe.equilibrage(liste,poids,meilleur)

def goulot(v, sommets, liste, poids):
    reste=[]
    for i in range(len(liste)) :
        if i not in sommets :
            reste.append(i)
    # Tous les sous-ensembles contenant 0
    resultat = []
    
    # Génération de tous les sous-ensembles
    sous_ensembles = [[v]]
    for t in reste:
        nouveaux = []
        for s in sous_ensembles:
            nouveaux.append(s + [t])
        sous_ensembles.extend(nouveaux)
    
    # On ajoute 0 à chaque sous-ensemble
    for s in sous_ensembles:
        candidat = s
        
        # Test de connexité
        if OperationGraphe.est_connexe(liste, candidat):
            resultat.append(candidat)
            
    max=0
    meilleur=[]
    for element in resultat :
        npoids=OperationGraphe.equilibrage(liste,poids,element)
        if npoids[0] > max :
            max=npoids[0]
            meilleur=element
    return meilleur, OperationGraphe.equilibrage(liste,poids,meilleur)
    



def heuristique(liste,poids):
    sommets, estim=GLA(liste,poids)
    goulots=[]
    ops=[]
    npoids=poids
    for i in sommets :
        if poids[i] < estim[0] :
            goulots.append(i)
    for i in goulots :
        result=goulot(i,sommets,liste,npoids)
        ops.append(result[0])
        npoids=result[1]
    ops.append(sommets)
    return ops, OperationGraphe.equilibrage(liste,npoids,sommets)


def chemins_depuis_racine(graphe):
    """
    Parcours un arbre depuis le sommet 0 et construit,
    pour chaque sommet, le chemin qui le relie à 0.

    Paramètre :
        graphe : graphe sous forme de liste d'adjacence

    Retour :
        chemins[i] = liste des sommets du chemin 0 -> i
    """

    N = len(graphe)

    # chemins[i] contiendra le chemin de 0 jusqu'à i
    chemins = [[] for _ in range(N)]

    visites = [False for _ in range(N)]

    def dfs(sommet, chemin_actuel):

        visites[sommet] = True

        # on enregistre le chemin courant
        chemins[sommet] = chemin_actuel + [sommet]

        # exploration des voisins
        for voisin in graphe[sommet]:
            if not visites[voisin]:
                dfs(voisin, chemins[sommet])

    # départ depuis 0
    dfs(0, [])

    return chemins

def heuristique_arbres(liste,poids):
    v=poids[0]
    chemins=chemins_depuis_racine(liste)
    moyenne=[]
    for i in range (len(chemins)) :
        moyenne.append(OperationGraphe.equilibrage(liste,poids,chemins[i])[0])
    liste_sommet=[i for i in range(len(liste))]
    liste_sommet_2=[i for i in range(len(liste))]
    for i in liste_sommet_2 :
        for j in chemins[i]:
            if moyenne[j]<moyenne[i] :
                if j in liste_sommet :
                    liste_sommet.remove(j)
            elif i!=j :
                if i in liste_sommet :
                    liste_sommet.remove(i)
    liste_sommet_trié=tri_fusion(liste_sommet,moyenne)
    # print(liste_sommet_trié)
    # for k in liste_sommet_trié :
    #     poids = OperationGraphe.equilibrage(liste,poids,chemins[k])
        #print(poids[0])
    poids = OperationGraphe.equilibrage(liste,poids,chemins[liste_sommet_trié[0]])
    if poids[0] != v :
        poids=heuristique_arbres(liste, poids)
    return poids

def tri_fusion(liste, poids):

    # Cas de base
    if len(liste) <= 1:
        return liste

    # Découpage
    milieu = len(liste) // 2
    gauche = tri_fusion(liste[:milieu], poids)
    droite = tri_fusion(liste[milieu:], poids)

    # Fusion
    resultat = []

    i = 0
    j = 0

    while i < len(gauche) and j < len(droite):

        if poids[gauche[i]] <= poids[droite[j]]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    # Ajout des éléments restants
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])

    return resultat


 




