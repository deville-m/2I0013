# -*- coding: utf-8 -*-
import puissance
import sys
sys.path.append("..")
import game
game.game=puissance
sys.path.append("./Joueurs")
import joueur_prem_coup
import joueur_minmax
import joueur_aleatoire
import joueur_alphabeta
import joueur_humain
game.joueur1=joueur_alphabeta
game.joueur2=joueur_humain

for i in range(1):
    jeu = game.initialiseJeu()

    while not game.finJeu(jeu):
        game.getCoupsValides(jeu)
        coup = game.saisieCoup(jeu)
        game.joueCoup(jeu, coup)

    g = game.getGagnant(jeu)
    print "fin de partie"
#game.affiche(jeu)

    print "Le gagant est : %d" %  g
