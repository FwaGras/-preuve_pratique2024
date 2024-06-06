def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
    print("début:",tab_a) # suivi des éléments de tab
    i = 0
    while i < len(tab_a) - 1 and a > tab_a[i+1]: 
        tab_a[i] = tab_a[i+1] 
        tab_a[i+1] = a
        i += 1
        print(tab_a)
    return tab_a

assert insere([1, 2, 4, 5], 3) == [1,2,3,4,5], "/!\ " 
assert insere([1, 2, 7, 12, 14, 25], 30) == [1, 2, 7, 12, 14, 25, 30], "/!\ "
assert insere([1, 533, 6677, 3003, 0], 100000) == [1, 533, 6677, 3003, 0, 100000], "/!\ "], "/!\ "