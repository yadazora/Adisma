import os
import webbrowser
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from display.display import Adisma
from display.display import adisma_window


import winsound
import pickle
import pygame





def savePlaylist():
    
    #Attempt 1: But this makes a temporary .txt file, We want something more complex
    thefile = open('playlist.txt', 'w')

    for song in root.playlist:
        thefile.write("%s\n" % song)

    thefile.close()
    

    #Attempt 2
    #using import pickle
    #using Tkinter too
'''
    
'''

root.playListFileO = filedialog.asksaveasfilename(title="Give a name to your playlist",filetypes=(("Python File",".py"),("Text File",".txt")),initialdir = "/")
    output = open(root.playListFileO,'wb')
    pickle.dump(root.playlist,output,-1)

    output.close()
