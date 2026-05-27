# Sharing Tea on a Graph

Implémentation numérique du problème *"Sharing tea on a graph"*
([arXiv 2405.15353](https://arxiv.org/abs/2405.15353)).

> **Contexte.** On place une unité de thé en un sommet source d'un graphe.
> À chaque étape, on choisit un sous-ensemble **connexe** de sommets et on
> **égalise** la quantité de thé entre eux. L'objectif est d'étudier la
> quantité maximale de thé atteignable par un sommet à distance *d* de la source.

---

## Fichiers

### `Graphe.py` — Structures de graphes et générateurs

Fonctions de base pour représenter et générer des graphes.

| Fonction | Description |
|---|---|
| `graphe_aleatoire(N)` | Génère un graphe aléatoire à *N* sommets (chaque arête présente avec proba ½). Retourne la matrice d'adjacence et la liste d'adjacence. |
| `arbre_aleatoire(N)` | Génère un **arbre** aléatoire connexe à *N* sommets (chaque sommet *i* > 0 est relié à un parent tiré uniformément dans {0, …, i−1}). |
| `fusion_graphe_poids(matrice, poids)` | Encode les poids des sommets sur la diagonale de la matrice d'adjacence. |
| `matrice_liste(matrice)` | Convertit une matrice d'adjacence avec poids (diagonale) en liste d'adjacence + liste de poids. |
| `liste_matrice(liste, poids)` | Opération inverse : liste d'adjacence + poids → matrice. |
| `the_aleatoire(N)` | Génère *N* poids tirés uniformément dans [0, 1]. |
| `the_binaire(N)` | Génère *N* poids binaires (0 ou 1) avec proba ½. |
| `the_unique(N)` | Génère un vecteur de poids nul sauf en un sommet aléatoire (valeur 1). Modélise le problème de départ : une unité de thé en un seul sommet. |
| `enregistrer_matrice(nom, matrice)` | Sauvegarde une matrice dans un fichier `.txt` (format lignes espace-séparées, matrices séparées par une ligne vide). |
| `lire_matrices(nom)` | Lit et retourne la liste des matrices stockées dans un fichier `.txt`. |

---

### `OperationGraphe.py` — Opérations sur les graphes

Implémente l'opération centrale du problème.

| Fonction | Description |
|---|---|
| `est_connexe(graphe, sommets)` | Vérifie par DFS si le sous-graphe induit par `sommets` est **connexe**. Condition nécessaire pour pouvoir appliquer l'équilibrage. |
| `equilibrage(graphe, poids, sommets)` | **Opération principale.** Si le sous-ensemble `sommets` est connexe, remplace les poids de ces sommets par leur moyenne (partage du thé). Retourne le nouveau vecteur de poids. |

---

### `Algo.py` — Algorithmes et heuristiques

Contient différentes stratégies de recherche et heuristiques pour maximiser
la quantité de thé obtenue en un sommet donné.

| Fonction | Description |
|---|---|
| `GLA(liste, poids)` | (*Greedy Lettuce Animal*) Explore tous les sous-ensembles connexes contenant le sommet 0 et choisit celui maximisant immédiatement la quantité de thé au sommet source après équilibrage. |
| `goulot(v, sommets, liste, poids)` | Cherche un sous-ensemble connexe optimal permettant d’augmenter la quantité de thé au sommet `v`, tout en tenant compte d’un ensemble de sommets déjà sélectionnés. |
| `heuristique(liste, poids)` | Heuristique générale construisant une suite d’opérations d’équilibrage à partir des « goulots » identifiés par `GLA`. Retourne la liste des opérations appliquées ainsi que les poids finaux. |
| `chemins_depuis_racine(graphe)` | Dans un arbre enraciné en 0, calcule pour chaque sommet le chemin reliant ce sommet à la racine via un parcours DFS. |
| `heuristique_arbres(liste, poids, ops)` | Heuristique récursive spécialisée pour les arbres. Compare les moyennes obtenues le long des chemins racine-sommet et applique les équilibrages jugés les plus favorables. |
| `heuristique_arbres2(liste, poids)` | Variante expérimentale de l’heuristique précédente, intégrant des équilibrages intermédiaires sur les chemins avant la phase de sélection principale. |
| `tri_fusion(liste, poids)` | Implémentation d’un tri fusion utilisé pour ordonner les sommets selon leurs scores/moyennes associés. |

---

## Exemple d'utilisation

```python
from Graphe import arbre_aleatoire, the_unique
from OperationGraphe import equilibrage

# Créer un arbre à 10 sommets avec 1 unité de thé au sommet 0
_, liste = arbre_aleatoire(10)
poids = the_unique(10)   # [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Partager le thé entre les sommets 0, 1, 2 (sous-ensemble connexe)
nouveaux_poids = equilibrage(liste, poids, [0, 1, 2])
```

## Référence

> J. P. Gollin *et al.*, **Sharing tea on a graph**, arXiv:2405.15353 (2024).
