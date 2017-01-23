import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
game.joueur1=joueur_humain
game.joueur2=joueur_humain

jeu = game.initialiseJeu()

while not game.finJeu(jeu):
    game.afficherJeu(jeu)
    coup = game.saisieCoup(jeu)
    game.joueCoup(jeu, coup)

g = game.getGagant(jeu)
game.afficherJeu(jeu)
