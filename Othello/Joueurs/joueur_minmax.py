# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
prof = 2

def evaluation (jeu):
    #retourne un score d'evaluation
		
	score = 0
	for x in range(8):
		for y in range(8):
			add = 1

			if (x==0 and y==1) or (x==1 and 0<=y<=1):
				if jeu[0][0][0] == moi:
					add = 5
				else:
					add = -5

			elif (x==0 and y==6) or (x==1 and 6<=y<=7):
				if jeu[0][7][0] == moi:
					add = 5
				else:
					add = -5

			elif (x==7 and y==1) or (x==6 and 0<=y<=1):
				if jeu[0][0][7] == moi:
					add = 5
				else:
					add = -5

			elif (x==7 and y==6) or (x==6 and 6<=y<=7):
				if jeu[0][7][7] == moi:
					add = 5
				else:
					add = -5

			if (x == 0 or y == 0 or x == 7 or y==7):
				add = 5

			elif (x==0 and y==0) or (x==0 and y==7) or (x==7 and y==0) or (x==7 and y==7):
				add = 25

			if (jeu[0][x][y] == moi):
				score += add
			elif (jeu[0][x][y] == adv):
				score -= add
    
	return score


def estimation (jeu, coup, p):
    #retourne le score d'utilite pour un coup donne
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    if game.finJeu(copie):
        g = game.getGagnant(copie)
        if g == moi:
            return 100000
        else:
            if g == 0:
                return -100
            else:
                return -100000

    if p == prof:
        return evaluation(copie)
    
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
	global moi, adv
	moi = game.getJoueur(jeu)
	adv = moi % 2 + 1
	coup = decision(jeu, game.getCoupsValides(jeu))
	return coup
