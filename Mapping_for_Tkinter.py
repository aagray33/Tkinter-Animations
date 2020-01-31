""" Enter your name(s) here
Ashton Gray

"""
from tkinter import *

class Mapping_for_Tkinter:
    
    def __init__(self,xmin,xmax,ymin,ymax,width,height=None):
        self.set_xmin(xmin)
        self.set_xmax(xmax)
        self.set_ymin(ymin)
        self.set_ymax(ymax)
        self.set_width(width)
        self.__set_height(width,ymax,ymin,xmax,xmin,height)
        
    #define setter methods
    def set_xmin(self,xmin):
        self.__xmin = xmin
    def set_xmax(self,xmax):
        self.__xmax = xmax
    def set_ymin(self,ymin):
        self.__ymin = ymin
    def set_ymax(self,ymax):
        self.__ymax = ymax
    def set_width(self,width):
        self.__width = width
    def __set_height(self,width,ymax,ymin,xmax,xmin,height):
        height=width*((ymax-ymin)/(xmax-xmin))
        self.__height = int(height)

    #define getter methods
    def get_xmin(self):
        return self.__xmin
    def get_xmax(self):
        return self.__xmax
    def get_ymin(self):
        return self.__ymin
    def get_ymax(self):
        return self.__ymax
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height

    def get_x(self,i):
        if i == 0:
            x = self.__xmin
        elif i == self.__width - 1:
            x = self.__xmax
        elif i == self.__width/2:
            x = 0
        else:
            a = i/(self.__width/2)
            x = (a*self.__xmax)-self.__xmax
        return x

    def get_y(self,j):
        if j == 0:
            y = self.__ymax
        elif j == self.__height - 1:
            y = self.__ymin
        elif j == self.__height/2:
            y = 0
        else:
            a = j/(self.__height/2)
            #y = a*self.__ymax*-1
            y = (a*self.__ymax)-self.__ymax
        return y

    def get_i(self,x):
        a = (abs(self.__xmin) + x)/(abs(self.__xmin)+abs(self.__xmax))
        i = a*self.__width
        return int(i)

    def get_j(self,y):
        a = (abs(self.__ymin) + y)/(abs(self.__ymin)+abs(self.__ymax))
        j = self.__height - (a*self.__height)
        return int(j)
            
    def __str__(self):
        return "Mapping created between x=["+str(self.__xmin)+","+str(self.__xmax)+"] y=["+str(self.__ymin)+","+str(self.__ymax)+"] math => ("+str(self.__width)+","+str(self.__height)+") tkinter"

    
""" to complete"""
    

def main():
    m=Mapping_for_Tkinter(-5.0,5.0,-5.0,5.0,500) # instantiate mapping
    print(m) # print info about object
    
    window = Tk() # instantiate a tkinter window
    canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
    canvas.pack()
    # create rectangle the Tkinter way
    print("Draw rectangle using tkinter coordinates at (100,400) (400,100)")
    canvas.create_rectangle(100,400,400,100,outline="black")
    
    # create circle using the mapping
    print("Draw circle using math coordinates at center (0,0) with radius 3")
    canvas.create_oval(m.get_i(-3.0),m.get_j(-3.0),m.get_i(3.0),m.get_j(3.0),outline="blue")
    
    # create y=x line pixel by pixel using the mapping
    print("Draw line math equation y=x pixel by pixel using the mapping")
    for i in range(m.get_width()):
        x=m.get_x(i) # obtain the x coordinate
        y=x
        canvas.create_rectangle((m.get_i(x),m.get_j(y))*2,outline="green") 

    
    window.mainloop() # wait until the window is closed'''


if __name__=="__main__":
    main()
