def recherche(tab:list, n:int)->int:
    """ Prend en paramètre une liste non vide de nombres et un
    entier. Renvoie l'indice de la dernière occurence de
    l'entier dans le tableau.
    """
    indice_n = None
    for i in range(len(tab)):
        if tab[i] == n:
            indice_n = i
            
    return indice_n
    
assert recherche([5, 3], 1) == None, "erreur"
assert recherche([2, 4], 2) == 0, "erreur"
assert recherche([2, 3, 5, 2, 4], 2) == 3, "erreur"
