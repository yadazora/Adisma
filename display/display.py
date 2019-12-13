from tkinter import*
import os
import webbrowser
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import winsound
import pickle
import pygame

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





class adisma_window:
	def __init__(self, window):
		self.rightframe = Frame(window, highlightbackground="grey" ,width=400, height=400, highlightthickness=2)
		self.rightframe.config(bg="black")
		self.rightframe.pack(side=RIGHT,fill=BOTH)
		self.box = Frame(window, bg="red",width=200, height=400)
		self.box.pack(side=LEFT,fill=BOTH)
		self.audacity = Label(self.box, text=" |> ADISMA", width=20, height=20, fg="red", bg="black")
		self.audacity.pack()

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
														filetypes=(("Python File", ".py"), ("Text File", ".txt")))
		input = open(root.playListFileI, 'rb')
		root.playlist = pickle.load(input)

		input.close()

	def play(self):
		if (root.songAdded == False):
			root.screenMessage.set("First add some Music man!")
		else:
			try:
				if (root.pauseFlag == True):
					pygame.mixer.music.unpause()
				else:
					print("Playing")
					pygame.mixer.init()
					pygame.mixer.music.load(root.playlist[root.i])
					pygame.mixer.music.play()
					root.screenMessage.set("Playing " + root.playlist[root.i])
			except:
				print("Could not play the music")

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

	def stopMusic():
		if (root.songAdded == False):
			root.screenMessage.set("First add some Music man!")
		else:
			pygame.mixer.music.fadeout(600)
			root.screenMessage.set("End of Playback!")

	def prevMusic():
		if (root.songAdded == False):
			root.screenMessage.set("First add some Music man!")
		else:
			try:
				if (root.playlist[root.i - 1]):
					root.i -= 1
					playMusic()
				else:
					print("No previous songs")
					root.screenMessage.set("No previous songs")
			except:
				stopMusic()
				print("No previous songs")

	def nextMusic():
		if (root.songAdded == False):
			root.screenMessage.set("First add some Music man!")
		else:
			try:

				if (root.playlist[root.i]):
					root.i += 1
					playMusic()
				else:
					root.i -= 1
			except:
				root.screenMessage.set("End of Playback, Please add more songs")

	def end():
		exit()

	def help():
		webbrowser.open("www.malibuinc.dx.am")

	def contact():
		webbrowser.open("www.malibuinc.dx.am")

	def contribute():
		webbrowser.open("www.malibuinc.dx.am")


root = Tk()
root.title("ADISMA 2.0 COPYRIGHT MALIBU")
c = Adisma(root)
root.after(5000, lambda: root.destroy())
root.mainloop()
root = Tk()
root.title("MALIBU'S ADISMA")
d = adisma_window(root)
root.mainloop()