def verifie(tab):
    """ Prend en paramètre un tableau non vides
    de nombre et renvoie True si le tableau est
    trié dans l'ordre croissant.
    """
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True
    
assert verifie([0, 5, 8, 8, 9]) == True, "erreur"
assert verifie([8, 12, 4]) == False, "erreur"
assert verifie([1]) == True, "erreur"
assert verifie([]) == True, "erreur"
