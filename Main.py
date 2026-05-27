import Graphe
import OperationGraphe
import Algo

Ma=Graphe.lire_matrices('ref_arbres_final')
for M in Ma :
    L,P=Graphe.matrice_liste(M)
    Vilkas=Algo.heuristique(L,P)
    Heuristique=Algo.heuristique_arbres(L,P,[])
    gla=Algo.GLA(L,P)
    opsVilkas=0
    opsHeuri=0
    for i in Vilkas[0] :
        if len(i)>1:
            opsVilkas+=1
    for i in Heuristique[1] :
        if len(i)>1:
            opsHeuri+=1
    print("Heuristique : "+str(Algo.heuristique(L,P)[1][0])+", Algo arbre : "+str(Algo.heuristique_arbres(L,P,[])[0][0])+", GLA : "+str(Algo.GLA(L,P)[1][0]))
    print(Vilkas[0],Heuristique[1])
