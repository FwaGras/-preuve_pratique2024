def correspond(mot:str, mot_à_trous:str)->bool:
    """ prend en paramètres deux chaînes de caractères mot et mot_à_trous
    Renvoie : True si on peut obtenir mot en remplaçant convenablement les caractères '*' de mot_a_trous.
    Sinon False.
    """
    temp = list(mot_à_trous) #on transtype mot_à_troues en liste pour pouvoir modifier les caractères

    for i in range(len(temp)):
        if temp[i] == '*': # on échange l'astérisque
            temp[i] = mot[i] # avec le caractère correspond
    
    temp2 = ''
    for car in temp:
        temp2 += car #on concatène les éléments de temp
    
    if temp2 == mot:
        return True
    else:
        return False
    
assert correspond('INFORMATIQUE', 'INFO*MA*IQUE') == True, "erreur"
assert correspond('STOP', 'S*') == False, "erreur"
assert correspond('AUTO', '*UT*') == True, "erreur"
