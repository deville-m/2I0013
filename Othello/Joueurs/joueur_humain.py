# -*- coding: utf-8 -*-

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    
    print "Liste des coups valides", jeu[2]
    ligne = int(raw_input("Entrer la ligne du coup à jouer: "))
    colonne = int(raw_input("Entrer la colonne du coup à jouer: "))
    return [ligne, colonne]
