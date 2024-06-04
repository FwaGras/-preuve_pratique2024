def effectif_notes(notes_eval:list)->list:
    """ Prend en paramètre une liste et renvoie
    un tableau de longueur 11 tel que la valeur d'indice
    i soit le nombre de notes valant i dans le tableau
    notes_eval.
    """
    tab = [0] * 11
    for note in notes_eval :
        tab[note] += 1
    return tab

def notes_triees(effectif:list)->list:
    """ Prend en paramètre la liste des effectifs et 
    renvoie un tableau avec les mêmes valeurs de
    notes_eval mais triées dans l'ordre croissant.
    """
    triees = []
    for i in range(11):
        triees += [i]*effectif[i]
    return triees


    
notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
eff = effectif_notes(notes_eval)
assert eff == [2, 0, 1, 0, 1, 4, 2, 1, 0, 5, 1], "erreur"
print(notes_triees(eff))
