# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game

def initscore():
    """
    None -> tuple(int, int)
    """
    return [0, 0]

def initplateau():
    """
    None -> list(list(int), list(int))
    """
    return [[4,4,4,4,4,4],
            [4,4,4,4,4,4]]

def finJeu(jeu):
    
    if len(jeu[4]) > 100 or jeu[-1][0] >= 25 or jeu[-1][1] >= 25:
        return True
    else:
        return False

def case_suiv(jeu, ligne, colonne):
    if ligne == 0:
        if colonne == 0:
            return (1, 0)
        else:
            return (ligne, colonne - 1)
    else:
        if colonne == 5:
            return (0, 5)
        else:
            return (ligne, colonne + 1)

def case_prec(jeu, ligne, colonne):
    if ligne == 1:
        if colonne == 0:
            return (0, 0)
        else:
            return (ligne, colonne - 1)
    else:
        if colonne == 5:
            return (1, 5)
        else:
            return (ligne, colonne + 1)

def distribue(jeu, coup, v):
    l, c = case_suiv(jeu, coup[0], coup[1])
    
    for i in range(v):
        jeu[0][l][c] += 1
        l, c = case_suiv(jeu, l, c)
        if l == coup[0] and c == coup[1]:
            l, c = case_suiv(jeu, l, c)

    l, c = case_prec(jeu, l, c)
    
    if (jeu[0][l][c] == 2 or jeu[0][l][c] == 3) and l != jeu[1] - 1:
        jeu[-1][jeu[1] - 1] += jeu[0][l][c]
        jeu[0][l][c] = 0
        l, c = case_prec(jeu, l, c)
        for i in range(v-1):
            if jeu[0][l][c] != 2 and jeu[0][l][c] != 3:
                break
            elif l == jeu[1] - 1:
                break
            else:
                jeu[-1][jeu[1] - 1] += jeu[0][l][c]
                jeu[0][l][c] = 0
                l, c = case_prec(jeu, l, c)

def advaff(jeu):
    """Jeu -> bool
    Retourne si l'adversaire est affame
    """
    if jeu[1] == 1:
        j = 1
    elif jeu[1] == 2:
        j = 0

    for nbgraines in jeu[0][j]:
        if nbgraines > 0:
            return False
    return True

def coups(jeu):
    cases = [[jeu[1] - 1, x] for x in range(6)]
    return [coup for coup in cases if game.getCaseVal(jeu, coup[0], coup[1]) != 0]

def getCoupsValides(jeu):
    a = advaff(jeu)
    cp = coups(jeu)

    if (not a):
        return cp
    v = []

    for coup in cp:
        c = coup[1]
        l = coup[0]
        g = game.getCaseVal(jeu, l, c)
        if l == 0:
            if g > c:
                v.append(coup)
        else:
            if g >= (6 - c):
                v.append(coup)
    return v

def joueCoup(jeu, coup):
    v = game.getCaseVal(jeu, coup[0], coup[1])
    game.setCaseVal(jeu, coup[0], coup[1], 0)
    distribue(jeu, coup, v)
    game.addCoupJoue(jeu, coup)
    game.changeJoueur(jeu)
    game.resetCoupsValides(jeu)
