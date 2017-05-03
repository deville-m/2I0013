# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
sys.path.append("..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    game.affiche(jeu)
    print "Liste des coups valides", jeu[2]
    colonne = int(raw_input("Entrer la colonne du coup à jouer: "))
    for i in range(len(jeu[2])):
        if jeu[2][i][1] == colonne:
            return jeu[2][i]
