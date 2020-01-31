from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time



""" to complete """
start_initials = input("Enter v,theta(0,90),strength (return for default 70,60,0.75): ")
if start_initials == "":
    v,theta,strength = 70,60,0.75
else:
    v,theta,strength = map(float, start_initials.split())

m=Mapping_for_Tkinter(0.0,1200.0,0.0,400.0,1200)
window = Tk()
canvas = Canvas(window, width=m.get_width(), height=m.get_height(), bg="white")
canvas.pack()
#create circle
circle = canvas.create_oval(m.get_i(-4),m.get_j(-4),m.get_i(4),m.get_j(4),fill="blue")

#initialize values
theta = theta*(math.pi/180)
t=0
timer = 0
x0 = 0.0
y0 = 0.0
y_prev=0.0
x_prev=0.0
rebound_counter = 0

while v > 0.01:
    x = x0+v*math.cos(theta)*t
    y = y0+(v*math.sin(theta)*t)-((9.8/2)*(t**2))
    #move circle
    canvas.move(circle,(m.get_i(x)-m.get_i(x_prev)),(m.get_j(y)-m.get_j(y_prev)))
    #create dotted path
    canvas.create_rectangle ((m.get_i(x),m.get_j(y))*2,outline="black")
    if y < 0:
        y0=y
        x0=x
        v=v*strength
        t=0
        rebound_counter = rebound_counter + 1
    if m.get_i(x) >= m.get_width():
        break
    window.update()
    time.sleep(.01)
    t=t+0.1
    timer = 0.1 + timer
    x_prev=x
    y_prev=y

canvas.itemconfig(circle,fill="red")
print("Total number of rebounds is: "+str(rebound_counter))
print("Total time is: "+str(timer)+"s")



