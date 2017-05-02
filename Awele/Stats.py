# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import time
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_agauche
import joueur_minmax
import joueur_aleatoire
import joueur_alphabeta
import joueur_humain

game.joueur1 = joueur_minmax
game.joueur2 = joueur_agauche
lg = []
for i in range(6):
    game.joueur1.prof = i
    game.joueur2.prof = 2
    g = 0
    for j in range(100):
        
        #Debut jeu
        print "Partie n ",j, "-", i
        jeu = game.initialiseJeu()
        aleatoire = 0
        while not game.finJeu(jeu):
            game.getCoupsValides(jeu)
            if aleatoire < 5:
                aleatoire += 1
                coup = joueur_aleatoire.saisieCoup(jeu)
            else:
                coup = game.saisieCoup(jeu)
            game.joueCoup(jeu, coup)
        #Fin jeu
        g = g + 1 if game.getGagnant(jeu) == 1 else g

    lg.append(g)
plt.ylim([60, 100])
plt.ylabel("Parties gagnees sur 100")
plt.xlabel("Profondeur")
plt.title("Joueur Minmax")
plt.plot(lg)
plt.show()
