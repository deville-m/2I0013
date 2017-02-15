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
    
    if game.getCoupsValides(jeu) == [] or len(jeu[3]) > 64:
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
        l += nl
        c += nc
        if (l < 0) or (l > 7) or (c < 0) or (c > 7):
            return False
        v = game.getCaseVal(jeu,l,c)
        if (v == j):
            if (i == 0):
                return False
            else:
                return True
        
        if (v == 0):
            return False
        i += 1
    return False

def encadrements(jeu, case, tous = False):
    """jeu, tous = False -> List[dir]
    retourne la liste des directions qui peuvent mener
    à un encadrement"""

    res=[]
    for l in [-1,0,1]:
        for c in [-1,0,1]:
            if not ((l==0) and (c==0)):
                if encadre(jeu,case[0],case[1],l,c):
                    res.append([l,c])
                    if not tous:
                        return res
    return res
                        
def entourageVide(jeu, case):
    """jeu , coup -> List[]
    retourne une liste corespondant au positions
    possibles avec la ligne et la colonne fournis
    en parametre"""
    
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
                    
    if (c < 7):
        if (game.getCaseVal(jeu, l, c + 1) == 0):
            res.append([l, c+1])
    
    if (c > 0):
        if (game.getCaseVal(jeu, l, c - 1) == 0):
            res.append([l, c-1])
            
    return res
            
                

def coups(jeu):
    j = game.getJoueur(jeu)
    j = (j%2)+1

    s = {str(x) for l in range (0,8) for c in range (0,8) for x in entourageVide(jeu,[l,c]) if game.getCaseVal(jeu,l,c) > 0}
    return [eval(x) for x in s]

def getCoupsValides (jeu):
    
    cp = coups(jeu)
    return [x for x in cp if len(encadrements(jeu, x, False)) > 0]

    
def joueCoup(jeu, coup):

    game.addCoupJoue(jeu, coup)
    j = game.getJoueur(jeu)
    s = jeu[-1]
    e = encadrements(jeu,coup,True)
    adv = (j%2) + 1
    game.setCaseVal(jeu, coup[0], coup[1], j)
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
    
    jeu[-1] = [0, 0]
    for i in range(8):
        for j in range(8):
            sc = game.getCaseVal(jeu, i, j)
            if (sc != 0):
                jeu[-1][sc - 1] += 1
    game.changeJoueur(jeu)
    game.resetCoupsValides(jeu)
