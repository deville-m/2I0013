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

    
def encadre(jeu, l,c, ml, mc):
    i = 0
    j = game.getJoueur(jeu)
    while True:
        l+= ml
        c+= mc
        if ( l > 7 ) or (l<0) or (c>7) or (c<0):
            return False
         v= game.getCaseVal( jeu, l, c )
         if ( v == j):
             if (i == 0):
                 return False
            else:
                return True
        if (v == 0):
            return False
        i+=1
        return False
    
def pions_autour(jeu, ligne, colonne):
    return [[x, y] for x in range(ligne - 3, ligne + 3) for y in range(colonnes - 3, colonnes + 3) if x != ligne and 0 <= x < 8 and y != colonne and 0 <= y < 8 and jeu[0][x][y] == 0]

def coups(jeu):
    p = game.getJoueur(jeu)
    p = (j % 2) + 1
    res = []
    for i in range(8):
        for j in range(8):
            if jeu[0][i][j] == p:
                tmp = pions_autour(jeu, i, j)
                for elem in tmp:
                    if elem not in res:
                        res.append(elem)
    return res

def getCoupsValides (jeu):
    cp = coups(jeu)
    return [ x for x in cp if len(encadrements(jeu, x, False))>0]

    
def joueCoup(jeu, coup):

     game.getCoupsJoue(jeu).append(coup)
     j = game.getJoueur(jeu)
     s = game.getScores(jeu)
     e= encadrements(jeu, coup, True)
     
     

    
