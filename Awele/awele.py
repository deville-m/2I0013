def initscore():
    """
    None -> tuple(int, int)
    """
    return (0, 0)

def initplateau():
    """
    None -> list(list(int), list(int))
    """
    return [[4,4,4,4,4,4], [4,4,4,4,4,4]]

def getCoupsValides(jeu, coups):
    res = []
    tmp = jeu[0][jeu[1] - 1]
    for i in range(len(tmp)):
        if (tmp[i] > 0):
            res.append([jeu[1] - 1, i])
    return res