def min_et_max(tab:list)->dict:
    """ Prend en paramètre un liste de nombres
    et renvoie un dictionnaire contenant le plus 
    grand élément et le plus petit élement de la liste. 
    """
    maxi, mini = tab[0], tab[0]
    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
        elif tab[i] < mini:
            mini = tab[i]
            
        
    return dict([('min', mini), ('max', maxi)])
    
assert min_et_max([0,4,5,-1,999,-100000,1000, 14**6]) == {'min': -100000, 'max': 14**6}
print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))