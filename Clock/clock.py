import imp
from tkinter import*
from turtle import title
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*

class Clock:
    def __init__(self,root):
        self.root=root
        self.root.title("Clock | Made By Ansh")
        self.root.geometry("1530x790+0+0")
        self.root.config(bg="#021e2f")
        
        title=Label(self.root,text="Clock | Made By Ansh",font=("times new roman",50,"bold"),bg="#04444a",fg="white").place(x=0,y=50,relwidth=1)
        
        self.lbl=Label(self.root,bg="white",bd=10,relief=RAISED)
        self.lbl.place(x=600,y=150,height=400,width=400)
        
        self.working()
        
    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        
        #==========For Clock Image=================
        
        bg=Image.open("cl.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        #==Formula To Rotate the AntiClock
        # angle_in_radians = angle_in_degress * math.pi/160
        # line_length =100
        #centry_x=250
        #centry_y=250
        #end_x = center_x - line_length * math.cos(angle_in_radians)
        #end_y = center_y - line_length * math.cos(angle_in_radians)
        
        #============Hour Line Image==============
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        
        #============Min Line Image==============
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)
        
        #============Sec Line Image==============
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=4)
        
        #=============Circle==================
        draw.ellipse((195,195,210,210),fill="black")
        
        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec=(s/60)*360
        self.clock_image(hr,min_,sec)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root=Tk()
obj=Clock(root)
root.mainloop()