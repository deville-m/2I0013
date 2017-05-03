# -*- coding: utf-8 -*-
# A optimisé au max
# Il semble y avoir un pb lors du changement de joueur
import sys
import copy
sys.path.append("../..")
import game
import random

prof = 1
global params
params=[0, 0, 0, 0]

def estimation (jeu, coup, a, b, p):
    #retourne le score d'utilite pour un coup donne
    copie = game.getCopieJeu(jeu)
    game.joueCoup(copie, coup)
    if game.finJeu(copie):
        g = game.getGagnant(copie)
        if g == 1:
            return 100000
        else:
            if g == 0:
                return -100
            else:
                return -100000

    elif p >= prof:
        return evaluation(copie)
    m=0
    coups = game.getCoupsValides(copie)
    for c in coups:
        s = estimation(copie, c, a, b, p+1)
        if p % 2 == 0:
            m=a
            if s >= b:
            	return b
            if s > a:
                a = s
                m = s

        else:
            m=b
            if s <= a:
                return a
            if s < b:
                b = s
                m = b
    return m

def decision(jeu, coups):
	ma = 0
	coup=coups[0]
	for c in coups:
		al = -100000
		be = 100000
		s = estimation(jeu, c, al, be, 1)
		if s >= ma:
		   ma = s
		   coup = c
	return coup

def saisieCoup(jeu):
	""" jeu -> coup
		Retourne un coup a jouer
	"""
	global moi,lautre,tours,coeff1,coeff2,coeff3
	moi = game.getJoueur(jeu)
	lautre = moi % 2 + 1
	coup = decision(jeu,game.getCoupsValides(jeu))
	return coup

# Partie liee a l'apprentissage

def f1(jeu):
	"""
		jeu*jeu -> float
		Retourne le nombre de coins apprartenant au joueur
	"""
        add = 0
        for case in [[0, 0], [0, 7], [7, 0], [7, 7]]:
            if game.getCaseVal(jeu, case[0], case[1]) == 1:
                add += 1
        return add

def f2(jeu):
        """
                Retourne le nombre de cases adjacentes appartenant au joueur
        """
        add = 0
        for case in [[0, 1], [1, 1], [1, 0], [1, 7], [0, 6], [1, 6], [6, 0], [6, 1], [7, 1], [6, 7], [6, 6], [7, 6]]:
            if game.getCaseVal(jeu, case[0], case[1]) == 1:
                add += 1
        return add

def f3(jeu):
        """
                Retourne le nombre de cases sur les côtés appartenant au joueur
        """
        return len([[x, y] for x in range(8) for y in range(8) if (x == 0 or y == 0 or x == 7 or y == 7) and game.getCaseVal(jeu, x, y) == 1])

def f4(jeu):
        """
                Retourne le nombre de cases appartenant au joueur
        """
        return len([[x, y] for x in range(8) for y in range(8) if game.getCaseVal(jeu , x, y) == 1])

def evaluation(jeu):
	"""
	jeu -> float
	Retourne un nombre compris entre [0,1] qui evalue l'effacite d'un coup joue par rapport au nombre de cases à 0 , 1 ou 2 graines chez le joueur
	"""
	# on fait un produit matriciel entre les parametres et les fonctions
	global params
	return dot(params,[f1(jeu),f2(jeu),f3(jeu), f4(jeu)])

def dot(l1,l2):
	return reduce((lambda x,y: x+l1[y]*l2[y]),range(0,len(l1)),0.0)

def setParam(i,x):
	params[i]=x

def addParam(i,x):
	params[i]+=x

def getNbParams():
	return len(params)

def getParams():
	return params
