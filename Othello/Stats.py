# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import time
import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_prem_coup
import joueur_minmax
import joueur_aleatoire
import joueur_alphabeta

#game.joueur1=joueur_alphabeta
game.joueur2=joueur_prem_coup

for j in [joueur_minmax, joueur_alphabeta, joueur_aleatoire]:
    game.joueur1 = i
    for j in range(100):
        temps = time.time()
        
        #Debut jeu
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

        temps = time.time() - temps
