def nombre_de_mots(phrase:str)->int:
    """ Prend en paramètre une phrase et renvoie
    le nombre de mots présents dans cette phrase.
    """
    nb_mots = 0
    for car in phrase:
        if car == " " or car == ".":
            nb_mots += 1
            
    return nb_mots
    
assert nombre_de_mots('Cet exercice est simple.') == 4, "erreur"
assert nombre_de_mots('Le point d exclamation est séparé !') == 6, "erreur"
assert nombre_de_mots('Combien de mots y a t il dans cette phrase ?') == 10, "erreur"
assert nombre_de_mots('Fin.') == 1, "erreur"
