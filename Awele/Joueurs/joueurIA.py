# -*- coding: utf-8 -*-
global moi
global prof=2

def Evaluation (jeu)
#retourne un score d'evaluation



def Estimation (jeu, coup)
#retourne le score d'utilite pour un coup donne
    copie = game.getCopie(jeu)
    
def Decision(jeu, coups):
    #retourne le meilleur  coup et son score
    maxi = estimation(jeu, coups[0])
    for c in coups[1:]:
        s = estimation(jeu, c)
        if s > maxi:
            maxi = s
            max_coup = c
    return max_coup

def saisieCoup(jeu):
    moi = game.getJoueur()
    coup = decision(jeu, game.getCoupsValides(jeu))
    return coup
