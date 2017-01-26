def initscore():
    """
    None -> list(int, int)
    """
    return [2, 2]

def initplateau():
    """
    None -> list(list(int), list(int))
    """
    return [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,2,1,0,0,0],
            [0,0,0,1,2,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]

def finJeu(jeu):
    
    if game.getCoupsValides(jeu) == [] or len(jeu[4]) > 64:
        return True
    else:
        return False

def joueCoup(jeu, coup):
    game.setCaseVal(jeu, coup[0], coup[1], jeu[1])
    convertis(jeu, coup[0], coup[1])
    game.addCoupJoue(jeu, coup)
    game.changeJoueur(jeu)
    game.resetCoupsValides(jeu)