def meilleure_richesse_cumulee(mine:list)->int:
    hauteur, largeur = dimensions(mine)

    # Initialisation
    richesses_cumulees = [0]*largeur

    for i in range(hauteur-1, -1, -1):
        temp = [0]*largeur

        # Colonne de gauche
        temp[0] = mine[i][0] + max(richesses_cumulees[0],
                                   richesses_cumulees[1])

        # Colonnes centrales
        for j in range(1, largeur-1):
            temp[j] = mine[i][j] + max(richesses_cumulees[j-1],
                                       richesses_cumulees[j],
                                       richesses_cumulees[j+1])

        # Colonne de droite
        temp[largeur-1] = mine[i][largeur-1] + max(richesses_cumulees[largeur-2],
                                    richesses_cumulees[largeur-1])

        richesses_cumulees = temp

    return max(richesses_cumulees)


def dimensions(mine:list)->tuple:
    """Renvoie le tuple (hauteur, largeur) de la mine"""
    return len(mine), len(mine[0])

# Tests

mine = [[1, 2, 3],
        [0, 1, 0],
        [0, 1, 0],
        [4, 0, 0]]
assert meilleure_richesse_cumulee(mine) == 9


mine = [[1, 2, 5]]
assert meilleure_richesse_cumulee(mine) == 5


mine = [[7, 9, 10, 7, 10, 8,  5],
        [5, 3,  1, 7,  5, 7,  1],
        [8, 9,  7, 7,  2, 3,  2],
        [7, 7,  2, 4,  6, 5,  7],
        [6, 7,  1, 6,  6, 6,  1],
        [3, 2,  5, 3,  2, 2, 10]]
assert meilleure_richesse_cumulee(mine) == 46