import Graphe

def est_connexe(graphe, sommets):

    if not sommets:
        return True  # vide = connexe par convention

    visites = set()

    def dfs(s):
        if s not in visites:
            visites.add(s)
            for voisin in graphe[s]:
                if voisin in sommets:
                    dfs(voisin)

    # on démarre du premier sommet
    dfs(sommets[0])

    # si tous les sommets ont été visités → connexe
    return visites == set(sommets)

def equilibrage(graphe, poids, sommets) : #graphe sous forme de liste de sommet connexe
    result=[i for i in poids]
    if est_connexe(graphe,sommets) :
        somme=0
        for i in sommets :
            somme+=poids[i]
        somme=somme/len(sommets)
        for i in sommets :
            result[i]=somme
    return result



