# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

prof = 2

def evaluation (jeu, score):
    #retourne un score d'evaluation
    return jeu[4][moi] - score[moi]


def estimation (jeu, coup, p):
    #retourne le score d'utilite pour un coup donne
    copie = game.getCopieJeu(jeu)
    score_avant = copie[4]
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
        return evaluation(copie, score_avant)
    
    if p < prof:
        coups = game.getCoupsValides(copie)
        max_min = estimation(copie, coups[0], p+1)
        for c in coups[1:]:
            s = estimation(copie, c, p+1)
            if p % 2 == 0 and s > max_min:
                max_min = s
            if p % 2 != 0 and s < max_min:
                max_min = s
        return max_min
    
    
def decision(jeu, coups):
    #retourne le meilleur  coup et son score
    maxi = estimation(jeu, coups[0], 1)
    max_coup = coups[0]
    for c in coups[1:]:
        s = estimation(jeu, c, 1)
        if s > maxi:
            maxi = s
            max_coup = c
    return max_coup

def saisieCoup(jeu):
    global moi
    moi = game.getJoueur(jeu) - 1
    coup = decision(jeu, game.getCoupsValides(jeu))
    return coup
