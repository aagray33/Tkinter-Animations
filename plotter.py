from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
from math import *

#### formula input
formula=input("Enter math formula (using x variable): ")

#input xmin,xmax,ymin,ymax and if left blank, default values at -5,5,-5,5
start = input("Enter xmin,xmax,ymin,ymax (return for default -5,5,-5,5): ")
if start == "":
    xmin,xmax,ymin,ymax = -5,5,-5,5
else:
    xmin,xmax,ymin,ymax = map(float, start.split())

#fix if mins and maxs do not match
if xmax <= xmin:
    while xmax <= xmin:
        xmin,xmax = map(float, input("Your xmax is invalid (xmax<=xmin), Re-Enter correct [xmin,xmax]: ").split())
if ymax <= ymin:
    while ymax <= ymin:
        ymin,ymax = map(float, input("Your ymax is invalid (ymax<=ymin), Re-Enter correct [ymin,ymax]: ").split())
        
m=Mapping_for_Tkinter(xmin,xmax,ymin,ymax,800)
"""to complete"""
window = Tk()
canvas = Canvas(window,width=m.get_width(),height=m.get_height(),bg="white")
canvas.pack()

#create y axis
if xmin < 0 < xmax:
    '''for i in range(m.get_width()):
        y=m.get_y(i)
        x=0
        canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="black")'''
    canvas.create_line((m.get_width())/2,0,(m.get_width())/2,m.get_height())
    
#create x axis
if ymin < 0 < ymax:
    '''for i in range(m.get_width()):
        x=m.get_x(i)
        y=0
        canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="black")'''
    y_val_x_axis = m.get_j((abs(ymin)-abs(ymin)))
    canvas.create_line((0,y_val_x_axis,m.get_width(),y_val_x_axis))

#plot equation
for i in range(m.get_width()):
    x=m.get_x(i)
    y=eval(formula)
    canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="blue")
