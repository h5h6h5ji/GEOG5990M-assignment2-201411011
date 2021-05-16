# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:00:47 2021

@author: z5490
"""

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation 
import random
import operator
import matplotlib.pyplot
import csv
import tkinter
import tkinter.filedialog
import numpy as np
import tkinter.messagebox

# convert the text into array
f = open("geology.txt")
geology = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist1 = []
    for word in parsed_line:
        rowlist1.append(float(word))
    geology.append(rowlist1)

f = open("mway.txt")
mway = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist2 = []
    for word in parsed_line:
        rowlist2.append(float(word))
    mway.append(rowlist2)
    
f = open("pop.txt")
mpop = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist3 = []
    for word in parsed_line:
        rowlist3.append(float(word))
    mpop.append(rowlist3)

fig = matplotlib.pyplot.figure(figsize=(5, 5))

a1= np.array(geology)
a2= np.array(mway)
a3= np.array(mpop)
h1 = 1
h2 = 2
h3 = 3
# load map function

def Load():
  
    matplotlib.pyplot.subplot(231)
    matplotlib.pyplot.xlim(0, 400)
    matplotlib.pyplot.ylim(0, 550)
    matplotlib.pyplot.imshow(geology)
    
    
    matplotlib.pyplot.subplot(232)
    matplotlib.pyplot.xlim(0, 400)
    matplotlib.pyplot.ylim(0, 550)
    matplotlib.pyplot.imshow(mway)
    
    
    matplotlib.pyplot.subplot(233)
    matplotlib.pyplot.xlim(0, 400)
    matplotlib.pyplot.ylim(0, 550)
    matplotlib.pyplot.imshow(mpop)
    canvas1.draw()
    
# create GUI 
from tkinter import *    
root = Tk() 
root.wm_title("Model")
root.geometry('1200x900')
canvas1 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas1._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Function", menu=model_menu)
model_menu.add_command(label="Load map", command=Load)

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()

def CallOn1(v1):
    global h1 
    h1 = s1.get()
    return h1

def CallOn2(v2):
    global h2
    h2 = s2.get()
    return h2

def CallOn3(v3):
    global h3
    h3 = s3.get()
    return h3

s1=Scale(root, label='Geology', # set label
           from_= 0,  # set minimum
           to=255, # set maximum
           orient=HORIZONTAL, # set the scale's oritation
           length=255, # set the size of scale
           variable=v1,
           showvalue=1, # display value
           tickinterval=100, # set the value range point
           resolution=1,  # set the minimum unit
           command=CallOn1)

s1.set(50)
s1.pack()

s2=Scale(root, label='way', 
           from_= 0,  
           to=255, 
           orient=HORIZONTAL, 
           length=255,
           variable=v2,
           showvalue=1, 
           tickinterval=100, 
           resolution=1, 
           command=CallOn2)

s2.set(50)
s2.pack()


s3=Scale(root, label='population', 
           from_= 0,  
           to=255, 
           orient=HORIZONTAL, 
           length=255, 
           showvalue=1,
           variable = v3, 
           tickinterval=100, 
           resolution=1,  
           command=CallOn3)

s3.set(50)
s3.pack()

q4 = h1+h2+h3
rowlist4= []
def create():
    global rowlist4
    rowlist4 = h1 / q4 *a1 + h2 / q4 *a2 +h3 / q4 *a3
    matplotlib.pyplot.subplot(235)
    matplotlib.pyplot.xlim(0, 400)
    matplotlib.pyplot.ylim(0, 550)
    matplotlib.pyplot.imshow(np.squeeze(rowlist4))
    canvas1.draw()
    return rowlist4
model_menu.add_command(label="create new map using scales", command=create)  


# save the created data as txt file 
def save():
    data1 = np.array(rowlist4)
    np.savetxt('out.txt', data1, fmt="%d", delimiter=',')
    messagebox.showinfo(title = 'hint', message = "your new map has been saved as 'out.txt' in this file's storage path")
model_menu.add_command(label="Save", command=save) 
root.mainloop()



