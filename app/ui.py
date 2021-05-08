import os
import webbrowser
from tkinter import *
import tkinter as tk
#from tkinter import filedialog
from tkinter.filedialog import askdirectory
from pygame import mixer
import pygame
from coprate.in4 import sasuke
import pygame

class Adisma:
	def __init__(self, root):
		self.rightframe = Frame(root, width=150, height=300)
		self.rightframe.config(bg="black")
		self.rightframe.pack(fill=BOTH, expand=True)
		self.label = Label(self.rightframe, text="ADISMA PLAYER", bg="green", fg="white")
		self.label.config(font=("",44))
		self.label.pack(side=RIGHT,fill=BOTH, expand=True)
		self.ico = PhotoImage(file="app/resources/unnamed.png")
		self.labek = Label(self.rightframe, image=self.ico, bg="green")
		self.labek.pack(side=LEFT)
#.................Defines the player window
class adisma_window:
	def __init__(self, window):
		'''main frame to hold the right frame and the left frame'''
		self.mainframe = Frame(window, highlightbackground="black", highlightthickness=2)
		self.mainframe.config(bg="black")
		self.mainframe.pack(fill=BOTH)
		'''Top mainframe holding other frames'''
		self.rightframe = Frame(window,width=400, height=400, highlightthickness=2,bg="black")
		self.rightframe.pack(side=RIGHT,fill=BOTH,expand=True)
		'''rightframe holding right side of the mainframe'''
		self.leftframe = Frame(window, bg="red",width=400, height=400)
		self.leftframe.pack(side=LEFT,fill=BOTH,expand=True)
		'''defines left frame of the mainframe'''
		self.audacity = Label(self.leftframe, text=" |> ADISMA",  fg="red", bg="black")
		self.audacity.config(font=("", 20))
		self.audacity.pack()
		self.ico1 = PhotoImage(file="app/resources/unnamed.png")
		self.piri = Label(self.leftframe, image=self.ico1,bg="red")
		self.piri.pack(fill=BOTH)
		#Motivation defines the text adisma ***none important element
		self.motivation = Label(self.rightframe, text="|> ADISMA",fg="red",bg="black")
		self.motivation.pack(fill=BOTH)# expand false
		'''Defines the album art'''
		self.ico = PhotoImage(file="app/resources/unnamed.png")	
		self.labek = Label(window, image=self.ico, bg="black")
		self.labek.pack(fill=BOTH)
		#Music control buttons
		self.play = Button(window, text=">" ,command=self.play, bg="black", fg="red")
		self.play.pack(fill=X)
		self.pause = Button(window, text="||", command=self.pause ,bg="black", fg="red")
		self.pause.pack()
		self.unpause = Button(window, text="|>", command=self.unpause, bg="black", fg="red")
		self.unpause.pack()
		self.stop = Button(window, text="[-]" ,command=self.stop ,bg="black" ,fg="red")
		self.stop.pack(fill=Y)
		self.in4 = Button(window, text="!", command=self.in4, bg="black", fg="red")
		self.in4.pack()
		#self.play = Button(self.rightframe, text="Play", fg="red", bg="blue",  command=self.play)
		#self.play.pack(fill=BOTH)

		""" ................Menu bar .........................."""
		menu = Menu(window, bg="BLACK", fg="green")
		window.config(menu=menu)
		subMenu = Menu(menu, bg="BLACK", fg="green")

		# Menu's create
		menu.add_cascade(label="Import Songs", menu=subMenu )

		# Submenus under subMenu
		subMenu.add_command(label="locate music", background="", command=self.openFile )
		editMenu = Menu(menu)
# PROGRAM LOGIC IMPLEMENTATION
	#from program_logic.logic import sasuke, pirana
	def openFile(self):
		directory = askdirectory()
		os.chdir(directory)
		song_list = os.listdir()
		global play_list
		play_list = tk.Listbox(self.rightframe,font="Helvetica 12 bold", bg="black", fg="red", selectmode=tk.SINGLE)
		play_list.pack(fill=BOTH)
		#print(c.song_list)
		for item in song_list:
			pos = 0
			play_list.insert(pos, item)
			pos += 1	
	def play(self):
		pygame.init()
		pygame.mixer.init()
		print(play_list)
		var = tk.StringVar()
		pygame.mixer.music.load(play_list.get(tk.ACTIVE))#
		var.set(play_list.get(tk.ACTIVE))#
		pygame.mixer.music.play()	
	def pause(self):
		pygame.mixer.music.pause()
	def unpause(self):
		pygame.mixer.music.unpause()
	def stop(self):
		pygame.mixer.music.stop()
	def in4(self):
		c = sasuke
		c.seek()

	