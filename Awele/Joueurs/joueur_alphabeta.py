# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

prof = 5

def evaluation(jeu):
    return jeu[-1][moi - 1] - jeu[-1][adv - 1]

# Generique

def estimation (jeu, coup, alpha, beta, p):
    #retourne le score d'utilite pour un coup donne
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
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

    for c in coups:
        s = estimation(copie, c, alpha, beta, p+1)
        if p % 2 == 0:
            if s >= beta:
                return beta
            if s > alpha:
                alpha = s

        if p % 2 != 0:
            if s <= alpha:
                return alpha
            if s < beta:
                beta = s

    return alpha if p % 2 == 0 else beta

def decision(jeu, coups):
    #retourne le meilleur  coup et son score
    alpha = -100000
    beta = 100000
    alpha = estimation(jeu, coups[0], alpha, beta, 1)
    max_coup = coups[0]

    for c in coups:
        s = estimation(jeu, c, alpha, beta, 1)
	if s >= beta:
            break
    	if s > alpha:
    	    alpha = s
	    max_coup = c

    return max_coup

def saisieCoup(jeu):
    global moi, adv
    moi = game.getJoueur(jeu)
    adv = moi % 2 + 1
    coup = decision(jeu, game.getCoupsValides(jeu))
    return coup
