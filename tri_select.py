def tri_selection(tab:list)->list:
    temp = 0
    indice_minimum = 0
    for i in range(len(tab)):
        indice_minimum = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[indice_minimum]:
                temp = tab[i]
                tab[i] = tab[j]
                tab[j] = temp
                print(tab)
    return tab
# Le programme ci-dessus est un tri par insertion /!\

def tri_selection_cor(tab):
    for i in range(len(tab)-1):
        indice_min = i
        print("correction:",tab)
        for j in range(i+1, len(tab)):
            if tab[j] < tab[indice_min]:
                indice_min = j
        tab[i], tab[indice_min] = tab[indice_min], tab[i]
    return tab
    
tab = [1, 52, 6, -9, 12]
assert tri_selection(tab) == [-9, 1, 6, 12, 52], "erreur"
assert tri_selection_cor(tab) == [-9, 1, 6, 12, 52], "erreur"




 
