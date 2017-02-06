# -*- coding: utf-8 -*-

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    j = jeu[1] - 1
    if j == 0:
        return jeu[2][-1]
    else:
        return jeu[2][0]
