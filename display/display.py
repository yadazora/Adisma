from tkinter import*
import os
import webbrowser
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
#import winsound
import pickle
import pygame
from pygame import mixer

#......class Adisma displays the boot up screen of the adisma player
class Adisma:
	def __init__(self, root):
		self.rightframe = Frame(root, width=150, height=300)
		self.rightframe.config(bg="black")
		self.rightframe.pack(fill=BOTH, expand=True)
		self.label = Label(self.rightframe, text="ADISMA PLAYER", bg="green", fg="white")
		self.label.config(font=("",44))
		self.label.pack(side=RIGHT,fill=BOTH, expand=True)
		self.ico = PhotoImage(file="unnamed.png")
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
		self.rightframe = Frame(self.mainframe,width=400, height=400, highlightthickness=2)
		self.rightframe.pack(side=RIGHT,fill=BOTH,expand=True)
		'''rightframe holding right side of the mainframe'''
		self.leftframe = Frame(self.mainframe, bg="red",width=400, height=400)
		self.leftframe.pack(side=LEFT,fill=BOTH,expand=True)
		'''defines left frame of the mainframe'''
		#Audacity defines the adisma welcome text to be replaced by album art
		self.audacity = Label(self.leftframe, text=" |> ADISMA",  fg="red", bg="black")
		self.audacity.config(font=("", 20))
		self.audacity.pack()
		#Motivation defines the text adisma ***none important element
		self.motivation = Label(self.rightframe, text="|> ADISMA",fg="red",bg="black")
		self.motivation.pack(fill=BOTH)# expand false
		'''Defines the album art'''
		self.ico = PhotoImage(file="unnamed.png")
		self.labek = Label(window, image=self.ico, bg="black")
		self.labek.pack(fill=BOTH)

		#Music control buttons
		self.play = Button(self.rightframe, text="PlAY" ,command=self.play, bg="black", fg="red")
		self.play.pack(fill=BOTH)
		self.pause = Button(self.rightframe, text="STOP", command=self.stop ,bg="black", fg="red")
		self.pause.pack(fill=BOTH)

		#self.play = Button(self.rightframe, text="Play", fg="red", bg="blue",  command=self.play)
		#self.play.pack(fill=BOTH)

		""" ................Menu bar .........................."""
		menu = Menu(window, bg="BLACK", fg="green")
		window.config(menu=menu)
		subMenu = Menu(menu, bg="BLACK", fg="green")

		# Menu's create
		menu.add_cascade(label="Import Songs", menu=subMenu )
		menu.add_cascade(label="Songs", command=self.openPlayList)
		menu.add_cascade(label="Albums")
		menu.add_cascade(label="Aritists")
		menu.add_cascade(label="Top Artists")

		# Submenus under subMenu
		menu.add_command(label="Find")
		subMenu.add_command(label="searchfile", background="", command=self.openFile )
		subMenu.add_command(label="Paparai")
		subMenu.add_separator()
		subMenu.add_command(label="exit")
		editMenu = Menu(menu)

# Functions to get music and control the player
	def openFile(self):
		try:
			root.songAdded = True
			root.filename = filedialog.askopenfilename(initialdir="/", title="Select your cool music track", filetypes=(
			("mp3 Music Files", "*.mp3"), ("m4a Music Files", "*.m4a")))
			root.playlist.append(root.filename)
			print(" Added " + root.filename)
			root.screenMessage.set("Good! Now Press on the Play Button")
		except:
			print("Cannot load the music")

	def openPlayList(self):
		# using pickle
		root.playListFileI = filedialog.askopenfilename(initialdir="/", title="Select your cool music track",
														#filetypes=(("Python File", ".py"), ("Text File", ".txt")))
														filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
    #window.filename = tkFileDialog.askopenfilename(initialdir = "",title = "Select file",filetypes = (("mp3 files","*.mp3"),("all files","*.*")))


		input = open(root.playListFileI, 'rb')
		root.playlist = pickle.load(input)

		input.close()

	def play(self):
		 mixer.init()
		 mixer.music.load('01 Paris_250918094501.mp3')
		 mixer.music.play()

		#if (root.songAdded == False):
		#	root.screenMessage.set("First add some Music man!")
		#else:
		#	try:
		#		if (root.pauseFlag == True):
		#			pygame.mixer.music.unpause()
		#		else:
		#			print("Playing")
		#			pygame.mixer.init()
		#			pygame.mixer.music.load(root.playlist[root.i])
		#			pygame.mixer.music.play()
		#			root.screenMessage.set("Playing " + root.playlist[root.i])
		#	except:
		#		print("Could not play the music")




	def pauseMusic():
		if (root.songAdded == False):
			root.screenMessage.set("First add some Music man!")
		else:
			try:
				pygame.mixer.music.pause()
				root.pauseFlag = True
				root.screenMessage.set("Paused")
			except:
				print("Cannot Pause the Music")

	def stop(self):
		'''if (root.songAdded == False):
			root.screenMessage.set("First add some Music man!")
		else:
			pygame.mixer.music.fadeout(600)
			root.screenMessage.set("End of Playback!")
'''
		mixer.music.stop()



root = Tk()
root.title("ADISMA 2.0 COPYRIGHT MALIBU")
c = Adisma(root)
root.after(1000, lambda: root.destroy())
root.mainloop()
root = Tk()
root.title("MALIBU'S ADISMA")
root.minsize(550,200)
d = adisma_window(root)
root.mainloop()
