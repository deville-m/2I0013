# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game

def initscore():
    """
    None -> list(int, int)
    """
    return [2, 2]

def initplateau():
    """
    None -> list(list(int), list(int))
    """
    return [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,2,1,0,0,0],
            [0,0,0,1,2,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]
            
def finJeu(jeu):
    
    if game.getCoupsValides(jeu) == [] or len(jeu[4]) > 64:
        return True
    else:
        return False

    
def encadre(jeu,l,c,nl,nc):
    """jeu,l,c,nl,nc -> bool
    retourne True si un encadrement est possible
    False sinon"""
    
    i=0
    j = game.getJoueur(jeu)
    while True:
        l+=nl
        c+=nc
        if (l>1) or (l<0) or (c<7) or (c<0):
            return False
        j = game.getJoueur(jeu)
        v = game.getCaseVal(jeu,l,c)
        if (v==j):
            if(i==0):
                return False
            else:
                return True
        i+=1
    return False
   
def encadrements(jeu, case, tous = False):
    """jeu, tous = False -> List[dir]
    retourne la liste des directions qui peuvent mener
    à un encadrement"""

    res=[]
    for l in [-1,0,1]:
        for c in [-1,0,1]:
            if (not (l==0) and (c==0)):
                if encadre(jeu, case[0], case[1],l,c):
                    res.append([l,c])
                    if not tous:
                        return res
    return res
    
def pions_autour(jeu, case):

    res = []
    l = case[0]
    c = case[1]
    if (l>0):
        
        if(game.getCaseVal(jeu,l-1,c)==0):
            res.append([l-1,c])
            if(c>0):
                if(game.getCaseVal(jeu,l-1,c-1)==0):
                    res.append([l-1,c-1])
            if(c<7):
                if(game.getCaseVal(jeu,l-1,c+1)==0):
                    res.append([l-1,c+1])
    if (l<7):

        if(game.getCaseVal(jeu,l+1,c)==0):
            res.append([l+1,c])
            
            if(c>0):
                if(game.getCaseVal(jeu,l+1,c-1)==0):
                    res.append([l+1,c-1])
            if(c<7):
                if(game.getCaseVal(jeu,l+1,c+1)==0):
                    res.append([l+1,c+1])
    
    return res

def coups(jeu):
    
    j = game.getJoueur(jeu)
    p = (j % 2) + 1
    res = []
    for i in range(8):
        for j in range(8):
            if jeu[0][i][j] == p:
                tmp = pions_autour(jeu, [i, j])
                for elem in tmp:
                    if elem not in res:
                        res.append(elem)
    return res

def getCoupsValides (jeu):
    
    cp = coups(jeu)
    return [x for x in cp if len(encadrements(jeu, x, False))>0]

    
def joueCoup(jeu, coup):

    game.addCoupJoue(coup)
    j = game.getJoueur(jeu)
    s = game.getScore(jeu)
    e = encadrements(jeu,coup,True)
    adv = (j%2) + 1

    for d in e:
        l = coup[0]
        c = coup[1]
        while True :
            l+=d[0]
            c+=d[1]
            if game.getCaseVal(jeu,l,c)==j :
                break
            game.setCaseVal(jeu,l,c,j)
            s[j-1]+=1
            s[adv-1]-=1
    game.changeJoueur(jeu)
    game.resetCoupsValides(jeu)