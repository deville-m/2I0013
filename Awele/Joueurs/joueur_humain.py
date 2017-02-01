# -*- coding: utf-8 -*-

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    print "Liste des coups valides", jeu[2]
    indice = int(raw_input("Entrer la colonne du coup à jouer: "))
    return [jeu[1] - 1, indice]
