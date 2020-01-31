from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time

""" to complete """
start_min_max = input("Enter xmin,xmax,ymin,ymax (return for default -300,300,-300,300): ")
if start_min_max == "":
    xmin,xmax,ymin,ymax = -300,300,-300,300
else:
    xmin,xmax,ymin,ymax = map(float, start_min_max.split())
    
start_initials = input("Enter x0,y0,v,theta (return for default 0,0,70,30): ")
if start_initials == "":
    x0,y0,v,theta = 0,0,70,30
else:
    x0,y0,v,theta = map(float, start_initials.split())

m=Mapping_for_Tkinter(xmin,xmax,ymin,ymax,600)
window = Tk()
canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white")
canvas.pack()
#create circle
circle = canvas.create_oval(m.get_i(x0-4),m.get_j(y0-4),m.get_i(x0+4),m.get_j(y0+4),fill="blue")
t=0
rebound_counter=0
theta = theta * (math.pi/180)
x_old = x0
y_old = y0

#start movement
for i in range(1500):
    #get new x,y
    x=x0+v*math.cos(theta)*t
    y=y0+v*math.sin(theta)*t
    #move circle
    canvas.move(circle,(m.get_i(x)-m.get_i(x_old)),(m.get_j(y)-m.get_j(y_old)))#subtract the tkinter new x,y coordinate from old x,y coordinate to get # of pixels
    #create rectangle dotted line to show path
    canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="black")
    #if hits left or right side change direction:
    if m.get_i(x) >= m.get_width() or m.get_i(x) <= 0:
        theta = math.pi - theta
        x0=x
        y0=y
        t = 0
        rebound_counter = rebound_counter + 1
    if m.get_j(y) >= m.get_height() or m.get_j(y) <= 0:
        theta = -1*theta
        x0=x
        y0=y
        t = 0
        rebound_counter = rebound_counter + 1
    #update values
    window.update()
    time.sleep(.01)
    t=t+0.1
    x_old = x
    y_old = y
    
canvas.itemconfig(circle,fill="red")
print("Total number of rebounds is: "+str(rebound_counter))
    
