def moyenne(notes:list)->float:
    """ Prend en paramètre une liste notes non vide de tuples
    à deux éléments entiers de la forme (note, coefficient) (int ou float)
    positifs ou nuls.
    Renvoie : la moyenne pondérée des notes de la liste sous forme de flottant
    si la somme des coefficients est non nulle
    """
    numerateur = 0
    denominateur = 0
    for note in notes :
        numerateur += note[0] * note[1]
        denominateur += note[1]
    
    if denominateur == 0:
        return None
    else:
        return numerateur / denominateur
        
assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142, "erreur"
assert moyenne([(3, 0), (5, 0)]) == None, "erreur"
