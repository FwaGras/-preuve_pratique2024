def max_et_indice(tab:list)->tuple:
    """ Prend en paramètre une liste non vide de nombre
    et renvoie le plus grand nombre et l'indice de sa première
    occurence.
    """
    maxi = tab[0]
    indice_maxi = 0
    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            indice_maxi = i
    
    return (maxi, indice_maxi)
    
assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3), "erreur"
assert max_et_indice([-2]) == (-2, 0), "erreur"
assert max_et_indice([-1, -1, 3, 3, 3]) == (3, 2), "erreur"
assert max_et_indice([1, 1, 1, 1]) == (1, 0), "erreur"
