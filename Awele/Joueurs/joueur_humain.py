import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    print "Liste des coups valides", jeu[3]
    indice = int(raw_input("Entrer l'indice du coup a jouer parmis ceux disponibles: "))
    return jeu[3][indice]

