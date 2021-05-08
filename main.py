from app.ui import Adisma, adisma_window
from tkinter import Tk
import tkinter
import os
#ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

root = Tk()
root.title("ADISMA 2.0 COPYRIGHT MALIBU")
c = Adisma(root)
root.after(10000, lambda: root.destroy())
root.mainloop()
root = Tk()
root.title("MALIBU'S ADISMA")
root.minsize(550,200)
root.configure(bg='black')
d = adisma_window(root)
root.mainloop()
