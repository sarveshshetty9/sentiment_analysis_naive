
import tkinter 
from PIL import Image, ImageTk
def did():
    def update_image():
        global tkimg1
        tkimg1 = ImageTk.PhotoImage(Image.open('testplot.png'))
        label.config( image = tkimg1)
        label.after(1000, update_image)
        print ("Updated")
    w = tkinter.Tk()
    w.geometry("500x500+450+100")

    im = Image.open('testplot.png')
    tkimg1 = ImageTk.PhotoImage(im)
    label =  tkinter.Label(w, image=tkimg1)
    print ("Loaded")
    label.pack()
    w.after(1000, update_image)
    w.mainloop()