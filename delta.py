def delta(tab:list)->list:
    """ Prend en paramètre un tableau non vides de nombres
    et renvoie un tableau contenant les valeurs entières 
    compressées par le codage par différence.
    """
    resultat = [tab[0]]
    for i in range(1, len(tab)):
        resultat.append(tab[i] - tab[i - 1])
        
    return resultat
    
assert delta([42]) == [42], "erreur"
assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3], "erreur"
