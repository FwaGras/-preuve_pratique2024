def gb_vers_entier(tab:list)->int:
    """ Prend en paramètre une liste de booleen et renvoie une
    un nombre en décimal selon sa forme binaire (False est 0 et
    True 1).
    """
    somme = 0
    for i in range(len(tab)):
        if tab[i] == True:
            somme += 2**(len(tab)-1-i)
    return somme
    
assert gb_vers_entier([]) == 0, "erreur"
assert gb_vers_entier([True, False, False, False, False, False, True, False]) == 130, "erreur"
