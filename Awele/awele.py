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

def advaff(jeu):
    """Jeu -> bool
    Retourne si l'adversaire est affame
    """
    if jeu[1] == 1:
        j = 1
    elif jeu[1] == 2:
        j = 0
    aff = True
    for nbgraines in jeu[0][j]:
        if nbgraines > 0:
            aff = False
    return aff

def coups(jeu):
    cases = [[jeu[1] - 1, x] for i in range(6)]
    return [coup for coup in cases if game.getCaseVal(jeu, coup[0], coup[1])]

def getCoupsValides(jeu, coups):
    a = advaff(jeu)
    cp = coups(jeu)

    if (!a):
        return cp:
    v = []

    for coup in cp:
        c = coup[1]
        p = coup[0]
        g = game.getCaseVal(jeu, l, c)
        if p = 0:
            if g > c:
                v.append(coup)
        else:
            if g >= (6 - c)
                v.append(coup)
    return v

def joueCoup(jeu, coup):
    v = game.getCaseVal(jeu, coup[0], coup[1])
    game.setCaseVal(jeu, coup[0], coup[1], 0)
    distribue(jeu, coup, v)
    game.addCoupJoue(jeu, coup)
    game.changeJoueur(jeu)
    game.resetCoupsValides(jeu)
