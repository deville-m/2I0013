# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game

def initscore():
    """
    None -> list(int, int)
    """
    return [0, 0]

def initplateau():
    """
    None -> list(list(int), list(int))
    """
    return [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]]
            
def alignes(jeu):

    for i in range(6):
    	for j in range(4):
            valprem = game.getCaseVal(jeu, i, j)
	    if (game.getCaseVal(jeu, i, j + 1) == valprem and game.getCaseVal(jeu, i, j + 2) == valprem and game.getCaseVal(jeu, i, j + 3) == valprem and valprem != 0):
		return valprem
	
    for i in range(7):
	for j in range(3):
	    valprem = game.getCaseVal(jeu, j, i)
	    if (game.getCaseVal(jeu, j + 1, i) == valprem and game.getCaseVal(jeu, j + 2, i) == valprem and game.getCaseVal(jeu, j + 3, i) == valprem and valprem != 0):
		return valprem

    for i in range(3):
        for j in range(4):
            valprem = game.getCaseVal(jeu, i, j)
            if (game.getCaseVal(jeu, i + 1, j + 1) == valprem and game.getCaseVal(jeu, i + 2, j + 2) == valprem and game.getCaseVal(jeu, i + 3, j + 3) == valprem and valprem != 0):
                return valprem
            
    for i in range(3):
        for j in range(3,7):
            valprem = game.getCaseVal(jeu, i, j)
            if (game.getCaseVal(jeu, i + 1, j - 1) == valprem and game.getCaseVal(jeu, i + 2, j - 2) == valprem and game.getCaseVal(jeu, i + 3, j - 3) == valprem and valprem != 0):
                return valprem
    return 0
    
def finJeu(jeu):
    
    res = alignes(jeu)
    if game.getCoupsValides(jeu) == [] or res != 0:
    	jeu[-1][res - 1] = 10000000
        return True
    else:
        return False                      
        
def getCoupsValides (jeu):
    
    coups = []
    for i in range(7):
        j = 0
        while j < 6 and game.getCaseVal(jeu, j, i) == 0:
            j += 1
        if j != 0:
            coups.append([j-1, i])
    return coups

    
def joueCoup(jeu, coup):

    game.addCoupJoue(jeu, coup)
    j = game.getJoueur(jeu)
    i = 0
    while i < 6 and game.getCaseVal(jeu, i, coup[1]) == 0:
    	i += 1
    game.setCaseVal(jeu, i - 1, coup[1], j)
    game.changeJoueur(jeu)
    game.resetCoupsValides(jeu)
