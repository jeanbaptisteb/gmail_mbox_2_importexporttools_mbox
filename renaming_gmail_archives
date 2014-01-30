# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:12:48 2014

@author: Bertrand
"""

import os
basedir = 'path//' #indiquer ici le chemin du dossier à traiter.


for root, dirs, files in os.walk(basedir, topdown=False): #topdown=False sert à traiter les sous-dossiers -> obligatoire
    
    #ajouter une extension .sbd à tous les répertoires et sous-répertoires. 
    for name in dirs:
        dir = os.path.join(root,name)
        os.rename(dir,
                  dir+'.sbd')
        
        
    #Supprimer l'extension .mbox de tous les fichiers
    for fileName in files:
        file_ext = os.path.splitext(fileName)
        if file_ext[1] == '.mbox':
            dir = os.path.join(root,fileName)
            print dir + file_ext[0]            
            os.rename(dir,
                      os.path.join(root,file_ext[0]))
    
    #Créer des fichiers portant le même nom que chaque répertoire, sans extension .sbd, au même niveau hiérarchique que le répertoire concerné
    for name in dirs:
        file_ext = os.path.splitext(name)               
        fullPath = os.path.join(root,name)
        newFile = os.path.join(root,file_ext[0])
        open(newFile, "a")
               
