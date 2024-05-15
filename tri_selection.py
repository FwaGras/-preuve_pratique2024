# Créé par kpajarito, le 15/05/2024 en Python 3.7
def echange(tab:list, i:int, j:int):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab:list):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(imin, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab, k, imin)

assert tri_selection([41, 55, 21, 18, 12, 6, 25]) != [6, 12, 18, 21, 25, 41, 55], "erreur"

