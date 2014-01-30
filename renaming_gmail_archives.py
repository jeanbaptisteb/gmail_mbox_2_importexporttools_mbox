# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:12:48 2014

@author: Bertrand
"""

import os
basedir = 'path//' #path of the folder to process.


for root, dirs, files in os.walk(basedir, topdown=False): #topdown=False -> to process subfolders : mandatory
    
    #Adding a .sbd extension to all folders and subfolders
    for name in dirs:
        dir = os.path.join(root,name)
        os.rename(dir,
                  dir+'.sbd')
        
        
    #Removing the .mbox extension from all files
    for fileName in files:
        file_ext = os.path.splitext(fileName)
        if file_ext[1] == '.mbox':
            dir = os.path.join(root,fileName)
            print dir + file_ext[0]            
            os.rename(dir,
                      os.path.join(root,file_ext[0]))
    
    #If they do not exist, creating files with the same name of each folder, without .sbd extension
    for name in dirs:
        file_ext = os.path.splitext(name)               
        fullPath = os.path.join(root,name)
        newFile = os.path.join(root,file_ext[0])
        open(newFile, "a")
               
