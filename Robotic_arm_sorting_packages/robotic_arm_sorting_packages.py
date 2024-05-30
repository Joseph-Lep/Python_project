# On a 3 tapis roulants sur lequels transitent des colis de poid - Lourd - Moyen - Leger
# On a un bras robotique qui doit trier 1 par 1 les colis par poids : du plus lourd au plus leger
# La fonction = solve(weight0, weight1, weight2)
# weight 0 1 & 2 repesentent les tapis.
# Lire l'index 0 des 3 tableaux, comparer et retourner la valeur la + haute.
# Effacer l'entrée et l'index retournée (index 1 devient 0), effacer compare
# Si poids identique enre 2 ou 3 tableaux : random le choix du tableau a choisir
# garder en mémoire le conflit et retourner ensuite le/les autres résultat non choisi
# Quand conflit résolut : effacer les entrées et index des tableaux résolus.
# Repeat

# Pour le moment les tableaux sont de longeur égale
# Prévoir quand un tableau est vide. Il faudra poursuivre l'instru
# weight2 est le tapis le + leger (moins susceptible d'être vide le 1er)
def solve(weight0, weight1, weight2):
    for i in range(len(weight0)): 
        compare = max(weight0[i], weight1[i], weight2[i])
        return(compare)

weight0 = [1, 3, 5, 8]
weight1 = [4, 2, 4, 7]
weight2 = [7, 3, 9, 9]
resultat = solve(weight0, weight1, weight2)
print (resultat)

