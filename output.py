import matplotlib.pyplot as plt
import tkinter as tk
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import csv
list1=[]
list2=[]
filename="mytestdataresults.csv"
def plotting():
    positive=0
    negative=0
    for i in range(len(list2)):
        if list2[i]==1:
            positive=positive+1
        else:
            negative =negative+1
    #print(positive)
    #print(negative)
    labels = 'Positive', 'Negative'
    sizes = [positive,negative]
    colors = ['gold' ,'lightskyblue']
    explode = (0, 0.1,)  # explode 1st slice


    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.savefig('testplot.png')

    plt.show()
    
def showpositive():
    labels = 'Positive', 'Negative'
    sizes = [1,0]
    colors = ['gold' ,'lightskyblue']
    explode = (0, 0.1,)  # explode 1st slice


    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.savefig('testplot.png')

    plt.show()

def shownegative():
    labels = 'Positive', 'Negative'
    sizes = [0,1]
    colors = ['gold' ,'lightskyblue']
    explode = (0, 0.1,)  # explode 1st slice


    plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.savefig('testplot.png')

    plt.show()

def filecall():    
    filename="mytestdataresults.csv"

    with open(filename,"r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)
        totalrow=row_count+1
    if (row_count==2):
        def read_cell(x, y):
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                y_count = 0
                for n in reader:
                    if y_count == y:
                        cell = n[x]
                        return cell
                    y_count += 1
        k=(read_cell(1, 1))#(column,row)
    #print(k)
        if (int(k)==1):
        #print("positive")
            showpositive()
        else:
        #print("negative")
            shownegative()
    else:
        with open(filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for lines in csv_reader:
                list1.append(lines[1])
            for i in range(1,row_count):
                list2.append(int(list1[i]))
    #print(list2)
        plotting()
