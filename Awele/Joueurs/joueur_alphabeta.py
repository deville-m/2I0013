# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

prof = 6

def evaluation(jeu):
    return jeu[-1][moi - 1] - jeu[-1][adv - 1]

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
