def recherche(elt:int, tab:list)->int:
    """ Prend en paramètre un tableau non vide
    de nombres et renvoie l'indice de la première
    occurence de l'élément qu'on recherche.
    """
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    
    return None
    
assert recherche(3, [1,2,3]) == 2, "erreur"
assert recherche(5, [5,5,5,5,5]) == 0, "erreur"
assert recherche(0, [1,2,4,8,16,32,64,128,255]) == None, "erreur"
