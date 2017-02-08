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
    ligne = int(raw_input("Entrer la ligne du coup à jouer: "))
    colonne = int(raw_input("Entrer la colonne du coup à jouer: "))
    return [ligne, colonne]
