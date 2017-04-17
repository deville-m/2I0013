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

#game.joueur1=joueur_alphabeta
game.joueur2 = joueur_agauche
game.joueur1 = joueur_minmax
tempsprof = []

for i in range(6):
    game.joueur1.prof = i
    g = 0
    ltemps = []
    for j in range(100):
        temps = time.time()
        
        #Debut jeu
        print "Partie n°", j
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
        
        temps = time.time() - temps
        ltemps.append(temps)
    tempsprof.append(sum(ltemps)/100.0)
    
plt.plot(tempsprof)
plt.ylabel("Temps moyen d'une partie")
plt.xlabel("Profondeur de Recherche")
plt.title("Minmax Awele")
plt.show()
