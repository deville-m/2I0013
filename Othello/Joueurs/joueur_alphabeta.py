# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

prof = 2

def trieCoups(coups):
    ordre = 0
    res = [[], [], [], []]
    for c in coups:
	x = c[0]
	y = c[1]

	if (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
	    res[0].append(c)

	elif (x == 1 and y == 1) or (x == 1 and y == 6) or (x == 6 and y == 1) or (x == 6 and y == 6):
	    res[2].append(c)

	elif (x == 0 and y == 1) or (x == 1 and y == 0) or (x == 0 and y == 6) or (x == 1 and y == 7) or (x == 7 and y == 1) or (x == 6 and y == 0) or (x == 7 and y == 6) or (x == 6 and y == 7):
	    res[1].append(c)

	else:
	    res[3].append(c)

    return res[0] + res[1] + res[2] + res[3]


def trieCoupsInverse(coups):
    ordre = 0
    res = [[], [], [], []]
    for c in coups:
	x = c[0]
	y = c[1]

	if (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
	    res[0].append(c)

	elif (x == 1 and y == 1) or (x == 1 and y == 6) or (x == 6 and y == 1) or (x == 6 and y == 6):
	    res[2].append(c)

	elif (x == 0 and y == 1) or (x == 1 and y == 0) or (x == 0 and y == 6) or (x == 1 and y == 7) or (x == 7 and y == 1) or (x == 6 and y == 0) or (x == 7 and y == 6) or (x == 6 and y == 7):
	    res[1].append(c)

	else:
	    res[3].append(c)

    return res[3] + res[2] + res[1] + res[0]

def evaluation (jeu):
    #retourne un score d'evaluation

    score = 0
    for x in range(8):
        for y in range(8):
            add = 1

            if (x == 0 and y == 1) or (x == 1 and 0 <= y <= 1):
                if jeu[0][0][0] == moi:
                    add = 5
                else:
                    add = -5

            elif (x == 0 and y == 6) or (x == 1 and 6 <= y <= 7):
                if jeu[0][7][0] == moi:
                    add = 5
                else:
                    add = -5

            elif (x == 7 and y == 1) or (x == 6 and 0 <= y <= 1):
                if jeu[0][0][7] == moi:
                    add = 5
                else:
                    add = -5

            elif (x == 7 and y == 6) or (x == 6 and 6 <= y <= 7):
                if jeu[0][7][7] == moi:
                    add = 5
                else:nautilus touche suppr
                    add = -5

            if (x == 0 or y == 0 or x == 7 or y == 7):
                add = 5

            elif (x == 0 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 0) or (x == 7 and y == 7):
                add = 25

            if (jeu[0][x][y] == moi):
                score += add
            elif (jeu[0][x][y] == adv):
                score -= add

    return score

# Generique

def estimation (jeu, coup, alpha, beta, p):
    #retourne le score d'utilite pour un coup donne
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    m = -100000 if p % 2 == 0 else 100000
    if game.finJeu(copie):
        g = game.getGagnant(copie)
        if g == moi:
            return 10000
        else:
            if g == 0:
                return -100
            else:
                return -10000

    if p == prof:
        return evaluation(copie)

    if p < prof:
	coups = game.getCoupsValides(copie)
	coups = trieCoups(coups) if p % 2 == 0 else trieCoupsInverse(coups)
	
        for c in coups:
            s = estimation(copie, c, alpha, beta, p+1)
            if p % 2 == 0:
                if s >= beta:
                    return beta+1
                if s > m:
                    alpha = max(alpha,s)
                    m = s

            if p % 2 != 0:
                if s <= alpha:
                    return alpha-1
                if s < m:
                    beta = min(beta, s)
                    m = s
                    
        return m
    
def decision(jeu, coups):
    #retourne le meilleur  coup et son score
    alpha = -10000000000
    beta = 10000000000
    trieCoups(coups)
    max_coup = coups[0]

    for c in coups:
        s = estimation(jeu, c, alpha, beta, 1)
    	if s > alpha:
    	    alpha = s
            max_coup = c
#        print "coup "+str(c)+"="+str(s)

    return max_coup

def saisieCoup(jeu):
    global moi, adv
    moi = game.getJoueur(jeu)
    adv = moi % 2 + 1
    coup = decision(jeu, game.getCoupsValides(jeu))
    return coup
