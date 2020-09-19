from tkinter import *
import tkinter as tk
from tkinter import messagebox,LEFT,RIGHT
import csv
import os
import pandas as pd
import nbc as nv
import output as op
import re
import converter as conv
import cleaner as clr
import tkop as tkp

import usersentencedivert as usd
import twitterhandler as twk



def mainframe():
    root=Tk()
    root.title("Sentiment Analysis")
    root.geometry("500x500+450+100")
    
    '''
    def mainscr():
        outputdisplay.destroy()
        root.deiconify()
    def allover():
        outputdisplay.destroy()
    
    
    outputdisplay=Toplevel(root)
    outputdisplay.title("Results")
    outputdisplay.geometry("500x500+450+100")
    outputdisplay.resizable(False,False)
    image = tk.PhotoImage(file="testplot.png")
    label = tk.Label(outputdisplay,image=image)
    label.pack()

    btnBack=Button(outputdisplay,text="Back",width=25,height=3,command=mainscr)
    btnexit=Button(outputdisplay,text="Exit",width=25,height=3,command=allover)
    btnBack.pack(pady=20)
    btnexit.pack(pady=30)
    '''
#usersenetnce dispay button
    def callsack1():
        root.deiconify()
    def sentencescreenback():
        usersentence.withdraw()
        root.deiconify()
#usertopic display button
    def usertopicback():
        usertopic.withdraw()
        root.deiconify()
    def output1():
        tkp.ifcalled()

#user-sentence extraction
    def sentenceextraction():
        s1=entsentence.get()
        MsgBox = tk.messagebox.askquestion ('Are You Sure? ',s1,icon = 'warning')
        if MsgBox == 'yes':
            usd.paragraghdiversion(s1)
            conv.convertcsvtotsv()
            conv.refurbish()
            nv.start()
            op.filecall()
            
            usersentence.destroy()
            output1()
        else:
            usersentence.deiconify()
            #entsentence.delete(0,tk.end)

#user-topic extraction
    def topicextraction():
        s2=enttopic.get()
        MsgBox = tk.messagebox.askquestion ('Are You Sure? ',s2,icon = 'warning')
        if MsgBox == 'yes':
            twk.dataextraction(s2)
            nv.start()
            op.filecall()
            usertopic.destroy()
            output1()
        else:
            usertopic.deiconify()
        #enttopic.delete(0,tk.end)
    
    
#usersentence display
    usersentence=Toplevel(root)
    usersentence.title("User Defined Sentence")
    usersentence.geometry("500x500+450+100")
    usersentence.withdraw()
    lblsentence=Label(usersentence,text="Enter the sentence",font=("arial",20,"bold"))
    entsentence=Entry(usersentence,bd=1,width=50,font=(12) )
#ntsentence.delete(0,tk.end)

    btnsentence=Button(usersentence,text="Find the Sentiment",font=("arial",15,"bold"),command=sentenceextraction)
    btnmainback=Button(usersentence,text="Back",font=("arial",15),width=20,command=sentencescreenback)
    lblsentence.pack(pady=20)
    entsentence.pack(pady=15)
    btnsentence.pack(pady=20)
    btnmainback.pack(pady=20,side=RIGHT)

#usertopic display
    usertopic=Toplevel(root)
    usertopic.title("User Defined Sentence")
    usertopic.geometry("500x500+450+100")
    usertopic.withdraw()
    lbltopic=Label(usertopic,text="Enter the Topic",font=("arial",20,"bold"))
    enttopic=Entry(usertopic,bd=1,width=50,font=(12) )
    #enttopic.delete(0,tk.end)

    btntopic=Button(usertopic,text="Find the Sentiment",font=("arial",15,"bold"),command=topicextraction)
    btnusertopicback=Button(usertopic,text="Back",font=("arial",15,"bold"),width=20,command=usertopicback)
    lbltopic.pack(pady=20)
    enttopic.pack(pady=15)
    btntopic.pack(pady=20)
    btnusertopicback.pack(pady=20,side=RIGHT)
    
    #Root window buttons
    def sentencescreendisplay():
        root.withdraw()
        usersentence.deiconify()
    def topicscreendisplay():
        root.withdraw()
        usertopic.deiconify()
    def ExitApplication():
        MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
            
            root.destroy()
        else:
            root.deiconify()

#mainscreen
    btnsentence=Button(root,text="Single Sentence",font=("arial",20,"bold"),width=25,height=3,command=sentencescreendisplay)
    btntopic=Button(root,text="Topic",font=("arial",20,"bold"),width=25,height=3,command=topicscreendisplay)
    btnexit=Button(root,text="exit",font=("arial",20,"bold"),width=15,height=3,command=ExitApplication)
    btnsentence.pack(pady=10)
    btntopic.pack(pady=10,)
    btnexit.pack(pady=10,side=RIGHT)
    root.mainloop()
