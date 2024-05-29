def maximum_tableau(tab:list)->int:
    """ Prend en paramètre un tableau non vide de nombres
    et renvoie le plus grand élément de ce tableau
    """
    maximum = tab[0]
    for nombre in tab:
        if nombre > maximum :
            maximum = nombre
            
    return maximum
    
assert maximum_tableau([98, 12, 104, 23, 131, 9]) == 131, "erreur"
assert maximum_tableau([-27, 24, -3, 15]) == 24, "erreur2"
