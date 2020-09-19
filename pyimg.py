

import tkinter as tk
import PIL.Image
import PIL.ImageTk
base = tk.Tk()
base.title("Dialy Dose")
im = PIL.Image.open("testplot.png")

photo = PIL.ImageTk.PhotoImage(im)
logo = tk.Label(base,image=photo,text="Logo bro lite")
logo.pack()

base.mainloop()