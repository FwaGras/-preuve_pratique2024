def effectif_notes(notes_eval:list)->list:
    """ Prend en paramètre une liste de longueur 11
    tel que la valeur d’indice i soit le nombre de notes valant
    i dans le tableau notes_eval.
    """
    tab = [0]*11
    for note in notes_eval:
        tab[note] += 1
        print(tab)
    return tab

def notes_triees(eff:list)->list:
    """ Prend en paramètre le tableau des effectifs des notes et renvoyant un 
    tableau contenant les mêmes valeurs que notes_eval mais triées dans l’ordre croissant.
    """
    triees = []
    for i in range(11):
        if eff[i] != 0:
            for _ in range(eff[i]):
                triees.apppend(i)
                
    return triees
notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]
eff = effectif_notes(notes_eval)
eff

assert notes_triees(eff) == [0, 0, 2, 4, 5, 5, 5, 5, 6, 6, 7, 9, 9, 9, 9, 9, 10], "erreur"
