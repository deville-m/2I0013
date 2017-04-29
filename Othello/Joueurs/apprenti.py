# -*- coding: utf-8 -*-
# A optimisé au max
# Il semble y avoir un pb lors du changement de joueur
import sys
import copy
sys.path.append("../..")
import game
import random
"""
	coeff1=>attaque
	coeff2=>preparation attaque
	coeff3=>defense
	prof=>horizon max d'anticipation

	/!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!
	on a viré toutes les occurences de moi/autre
	car cela foutais le bordel, de plus on est parti
	du principe que l'oracle et l'élève sont toujours
	en joueur 1
	/!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!\ /!
"""
prof = 1
global params
params=[6,-1,3]

#	----------------------	METTRE VOS FONCTIONS DE BASE ----------------------
#	----------------------	METTRE VOS FONCTIONS DE BASE ----------------------
#	----------------------	METTRE VOS FONCTIONS DE BASE ----------------------

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

#	----------------------	METTRE VOS FONCTIONS DE BASE ----------------------
#	----------------------	METTRE VOS FONCTIONS DE BASE ----------------------
#	----------------------	METTRE VOS FONCTIONS DE BASE ----------------------



#	----------------------	METTRE VOS FONCTIONS ----------------------
#	----------------------	METTRE VOS FONCTIONS ----------------------
#	----------------------	METTRE VOS FONCTIONS ----------------------

def f1(jeu):
	"""
		jeu*jeu -> float
		Retourne un nombre compris entre [0,1] qui evalue l'effacite d'un coup joue par rapport au score
	"""
	return float(game.getScore(jeu,1)-game.getScore(jeu,2))/18


def f3(jeu):
	"""
		jeu*jeu -> float
		pas de cases qui se suive
	"""
	l=[]
	# if moi==1:
	i=5
	while i>0:
		nbCases = 0
		case = [0,i]
		while game.getCaseVal(jeu,0,case[1])<3 and case!=[1,0]:
			nbCases+=1
			case = caseSuivante(jeu,case)
		if nbCases>1: i-=nbCases
		else: i-=1
		l.append(nbCases)
	return 1-float(max(l))/6

def f2(jeu):
	"""
		jeu*jeu -> float
		cases qui se suive chez l'autre
	"""
	l=[]
	i=0
	while i<6:
		nbCases = 0
		case = [1,i]
		while game.getCaseVal(jeu,1,case[1])<3 and case!=[0,5]:
			nbCases+=1
			case = caseSuivante(jeu,case)
		if nbCases>1: i+=nbCases
		else: i+=1
		l.append(nbCases)

	return float(max(l))/6

def caseSuivante(jeu, case):
	"""
		jeu*case -> case
		Renvoie la case situee apres celle entree en parametre
	"""
	if case == [0,0] : return [1,0]
	elif case == [1,5] : return [0,5]
	elif case[0] == 0 : return [0,case[1] - 1]
	return [1,case[1] + 1]

#	----------------------	METTRE VOS FONCTIONS ----------------------
#	----------------------	METTRE VOS FONCTIONS ----------------------
#	----------------------	METTRE VOS FONCTIONS ----------------------

def evaluation(jeu):
	"""
	jeu -> float
	Retourne un nombre compris entre [0,1] qui evalue l'effacite d'un coup joue par rapport au nombre de cases à 0 , 1 ou 2 graines chez le joueur
	"""
	# on fait un produit matriciel entre les parametres et les fonctions
	global params
	return dot(params,[f1(jeu),f2(jeu),f3(jeu)])

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
