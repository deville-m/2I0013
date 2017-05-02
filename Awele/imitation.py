# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import random
import joueur_agauche
import apprenti
import enseignant
import joueur_alphabeta

game.joueur1 = apprenti
game.joueur2 = joueur_alphabeta

#	----------------------	METTRE VOTRE MEILLEUR JOUEUR ----------------------
#	----------------------	METTRE VOTRE MEILLEUR JOUEUR ----------------------
#	----------------------	METTRE VOTRE MEILLEUR JOUEUR ----------------------

oracle = enseignant

#	----------------------	METTRE VOTRE MEILLEUR JOUEUR ----------------------
#	----------------------	METTRE VOTRE MEILLEUR JOUEUR ----------------------
#	----------------------	METTRE VOTRE MEILLEUR JOUEUR ----------------------

eleve = game.joueur1
adversaire = game.joueur2
"""
Pas d'apprentissage a
"""
a=0.1
while True:
	jeu = game.initialiseJeu()
	while not game.finJeu(jeu):
		if game.getJoueur(jeu)==1:
			cp=game.getCoupsValides(jeu)
			ls=[oracle.estimation(game.getCopieJeu(jeu),x,-1000000,1000000,1) for x in cp]
			opt=cp[ls.index(max(ls))]
			sopt=game.getCopieJeu(jeu)
			game.joueCoup(sopt,opt)
			m=max(ls)
			ls=[x for x in cp if ls[cp.index(x)]<m]
			for c in ls:
				copie = game.getCopieJeu(jeu)
				game.joueCoup(game.getCopieJeu(jeu),c)
				o=eleve.evaluation(sopt)
				s=eleve.evaluation(copie)
				if (o-s)<1:
					for j in range(0,eleve.getNbParams()):
						scjc=getattr(eleve,"f"+str(j+1))(copie)
						scjo=getattr(eleve,"f"+str(j+1))(sopt)
						eleve.addParam(j,-a*(scjc-scjo))
		c=game.saisieCoup(jeu)
		game.joueCoup(jeu,c)
	a-=0.0025
	print a
	print eleve.getParams()
	print game.getScores(jeu)
