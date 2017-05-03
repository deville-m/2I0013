# -*- coding: utf-8 -*-
from random import choice

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    return choice(jeu[2])