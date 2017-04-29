# -*- coding: utf-8 -*-

import awele
import sys
sys.path.append("..")
import game
game.game = awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_aleatoire
game.joueur1 = joueur_IA
game.joueur2 = joueur_prem_coup
oracle = alphabeta
eleve = game.joueur1
"""
Pas d'apprentissage a
"""
a=0.1
while True:
	jeu = game.initialiseJeu()
	while not game.finJeu(jeu):
		if game.getJoueur(jeu)==1:
			coups_valides=game.getCoupsValides(jeu)
			ls=[oracle.estimation(game.getCopieJeu(jeu),x,-1000000,1000000,1) for x in coups_valides]
			coup_optimal=coups_valides[ls.index(max(ls))]
			sopt=game.getCopieJeu(jeu)
			game.joueCoup(sopt,coup_optimal)
			# sopt=game.joueCoup(game.getCopieJeu(jeu),opt)
			# m=max(ls)
			# print cp
			ls=[x for x in coups_valides if x!=coup_optimal]
			for c in ls:
				# print "in"
				copie = game.getCopieJeu(jeu)
				coups_valides=game.joueCoup(game.getCopieJeu(jeu),c)
				# print jeu
				o=eleve.evaluation(sopt)
				s=eleve.evaluation(copie)
				# print o,s
				if (o - s) < 1:
					for j in range(eleve.getNbParams()):
						scjc=eleve.evalj(copie)
						scjo=eleve.evalj(sopt)
						eleve.addParam(j,-a*(scjc-scjo))
				# print "out"

			c=game.saisieCoup(jeu)
			game.joueCoup(jeu,c)
		else :
			c=game.saisieCoup(jeu)
			game.joueCoup(jeu,c)
	a-=0.01
	print eleve.getParams()
	print game.getScores(jeu)
