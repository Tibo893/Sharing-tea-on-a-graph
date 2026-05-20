import Graphe
import OperationGraphe
import Algo


# s=[]
# for j in range(10):
#      s.append(j)
# i=0
# while i < 100 :
#     G,L=Graphe.arbre_aleatoire(10)
#     print(L)
#     P=Graphe.the_aleatoire(10)
#     Graphe.fusion_graphe_poids(G,P)
#     if OperationGraphe.est_connexe(L,s) :
#         Graphe.enregistrer_matrice("ref_arbres2",G)
#         i+=1

def test(liste, poids, hyper):
    for h in hyper :
        poids = OperationGraphe.equilibrage(liste,poids,h)
    return poids


# listeHyper=[[3,1],[2,1,0]]
# Ma=Graphe.lire_matrices('ref_3')
# for M in Ma :
#     L,P=Graphe.matrice_liste(M)
#     print("Heuristique : "+str(Algo.heuristique(L,P)[1][0])+", Algo arbre : "+str(Algo.heuristique_arbres(L,P)[0])+", Algo arbre 2 : "+str(Algo.heuristique_arbres2(L,P)[0])+", GLA : "+str(Algo.GLA(L,P)[1][0])+", Calcul : "+str(test(L,P,listeHyper)[0]))


Ma=Graphe.lire_matrices('ref_arbres')
for M in Ma :
    L,P=Graphe.matrice_liste(M)
    print("Heuristique : "+str(Algo.heuristique(L,P)[1][0])+", Algo arbre : "+str(Algo.heuristique_arbres(L,P)[0])+", Algo arbre 2 : "+str(Algo.heuristique_arbres2(L,P)[0])+", GLA : "+str(Algo.GLA(L,P)[1][0]))