import time
import socket
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import *
import tkinter
import tkinter as tk
from tkinter import messagebox,LEFT,RIGHT
import csv
import os
import cv2
import pandas as pd
import nbc as nv
import output as op
import re
import converter as conv
import cleaner as clr
import tkop as tkp
import threading
import time
import usersentencedivert as usd
import twitterhandler as twk
from tkinter import ttk  
from tkinter import Tk, Label
import sys
from PIL import Image, ImageTk 

def maincall():

    class Splash(Toplevel):
        def __init__(self, parent):
            Toplevel.__init__(self, parent)
            self.title("Welcome")
            self.geometry("500x500+450+100")
            lblwelcome=Label(self, text ="Sentiment Analysis", font = ('arial', 20, 'bold'))
            lblwelcome1=Label(self, text =" Using ", font = ('arial', 20, 'bold'))
            lblwelcome2=Label(self, text =" Machine Learning Algorithm", font = ('arial', 20, 'bold'))
        
            lblwelcome.pack(pady = 1)
            lblwelcome1.pack(pady = 1)
            lblwelcome2.pack(pady = 1)
            
            self.update()

    class App(Tk):
        def __init__(self):
            Tk.__init__(self)
            self.withdraw()
            splash = Splash(self)
            
       
    
            self.title("Sentiment Analysis")
            self.geometry("500x500+450+100")
            import socket
            
            im = Image.open('testplot.png')
            def update_image():
                global img
                img = ImageTk.PhotoImage(Image.open('testplot.png'))
                panel.config( image = img)
                panel.after(1000, update_image)
                print ("Updated")
        
            def backout():
                outputdisplay.destroy()
                maincall()
            def exitall():
                outputdisplay.destroy()
                time.sleep(1)
                sys.exit(0)
            outputdisplay=Toplevel(self)
            outputdisplay.title("Results")
            outputdisplay.geometry("500x500+450+100")
            outputdisplay.resizable(False,False)
            outputdisplay.withdraw()
            path = "testplot.png"
            img = ImageTk.PhotoImage(Image.open(path))
            panel = Label(outputdisplay, image=img)
            print("loaded")
            panel.photo = img
            panel.pack()
            btnBack=Button(outputdisplay,text="Back",width=25,height=3,command=backout)
            btnexit=Button(outputdisplay,text="Exit",width=25,height=3,command=exitall)
            btnBack.pack(pady=20)
            btnexit.pack(pady=30)
        
        
        
            try:
                socket.create_connection(("www.google.com", 80))
                print("You are connected.")

            except OSError as e:
                print(e)
                print("You are not connected")
            def sentencescreenback():
                usersentence.withdraw()
                self.deiconify()


            def usertopicback():
                usertopic.withdraw()
                self.deiconify()
            def sentenceextraction():
                s1=entsentence.get()
                MsgBox = tk.messagebox.askquestion ('Are You Sure? ',s1,icon = 'warning')
                if MsgBox == 'yes':
                    usd.paragraghdiversion(s1)
                    conv.convertcsvtotsv()
                    conv.refurbish()
                    nv.start()
                    usersentence.destroy()
                    time.sleep(1)
                    op.filecall()
                    outputdisplay.after(1000, update_image)
                    outputdisplay.deiconify()
                    #outputdisplay.after(1000, update_image)

                else:
                    usersentence.deiconify()
                
                    entsentence.delete(0,END)
                    entsentence.focus()
            def topicextraction():
                s2=enttopic.get()
                MsgBox = tk.messagebox.askquestion ('Are You Sure? ',s2,icon = 'warning')
                if MsgBox == 'yes':
                    twk.dataextraction(s2)
                    nv.start()
                    op.filecall()
                    usertopic.destroy()
                    time.sleep(1)
                    op.filecall()
                    outputdisplay.after(1000, update_image)
                    outputdisplay.deiconify()
                    
                else:
                    usertopic.deiconify()
                    enttopic.delete(0, END)
                    enttopic.focus()
                    

            usersentence=Toplevel(self)
            usersentence.title("User Defined Sentence")
            usersentence.geometry("500x500+450+100")
            usersentence.withdraw()
            lblsentence=Label(usersentence,text="Enter the sentence",font=("arial",20,"bold"))
            entsentence=Entry(usersentence,bd=1,width=50,font=(12) )
            
            btnsentence=Button(usersentence,text="Find the Sentiment",font=("arial",15,"bold"),command=sentenceextraction)
            btnmainback=Button(usersentence,text="Back",font=("arial",15),width=20,command=sentencescreenback)
            lblsentence.pack(pady=20)
            entsentence.pack(pady=15)
            btnsentence.pack(pady=20)
            btnmainback.pack(pady=20,side=RIGHT)

            usertopic=Toplevel(self)
            usertopic.title("User Defined Topic")
            usertopic.geometry("500x500+450+100")
            usertopic.withdraw()
            lbltopic=Label(usertopic,text="Enter the Topic",font=("arial",20,"bold"))
            enttopic=Entry(usertopic,bd=1,width=50,font=(12) )
        
            btntopic=Button(usertopic,text="Find the Sentiment",font=("arial",15,"bold"),command=topicextraction)
            btnusertopicback=Button(usertopic,text="Back",font=("arial",15,"bold"),width=20,command=usertopicback)
            lbltopic.pack(pady=20)
            enttopic.pack(pady=15)
            btntopic.pack(pady=20)
            btnusertopicback.pack(pady=20,side=RIGHT)
              
            def sentencescreendisplay():
                self.withdraw()
                usersentence.deiconify()
            def topicscreendisplay():
                self.withdraw()
                usertopic.deiconify()
            def ExitApplication():
                MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
                if MsgBox == 'yes':
                    self.destroy()
                    time.sleep(1)
                    sys.exit(0)
                else:
                    self.deiconify()
            btnsentence=Button(self,text="Single Sentence",font=("arial",20,"bold"),width=20,height=2,command=sentencescreendisplay)
            btntopic=Button(self,text="Topic",font=("arial",20,"bold"),width=20,height=2,command=topicscreendisplay)
            btnexit=Button(self,text="Exit",font=("arial",20,"bold"),width=15,height=1,command=ExitApplication)
            btnsentence.pack(pady=30)
            btntopic.pack(pady=15)
            btnexit.pack(pady=130,side=RIGHT)
    
    
            time.sleep(1)
            outputdisplay.after(1000, update_image)
            splash.destroy()

            self.deiconify()

    if __name__ == "__main__":
        app = App()
        app.mainloop()
maincall()