import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

jeu = game.initialiseJeu()

while not game.finJeu(jeu):
    game.getCoupsValides(jeu)
    coup = game.saisieCoup(jeu)
    game.joueCoup(jeu, coup)

g = game.getGagnant(jeu)
game.affiche(jeu)

print "Le gagant est : %d" %  g



