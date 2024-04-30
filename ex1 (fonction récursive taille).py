def taille(arbre:dict, lettre:str)->int:
    """ Prend en paramètre un arbre binaire
    non vide et un caractère, et renvoie la 
    taille de l'arbre, soit le nombre total 
    de noeuds selon la racine choisis.
    """ 
    if lettre == '':
        return 0
    else:
        print(arbre[lettre][0], arbre[lettre][1])
        return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])
        
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 
'H':['','']}

print(taille(a, 'B'))