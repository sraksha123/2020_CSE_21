from tkinter import *
from PIL import Image,ImageTk
import cv2  
import time
import sys
import os
class Register:
    def _init_(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightblue")


        #self.bg=ImageTk.PhotoImage(file="C:\\Users\\Ravish Reddy\\Desktop\\PROJECT\\bg1.jpg")
        #bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="C:\\Users\\Ravish Reddy\\Desktop\\PROJECT\\bg1.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        frame1=Frame(self.root,bg="lightblue")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="Register here",font=("times new roman",20,"bold"),bg="lightblue",fg="blue").place(x=50,y=30)
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="lightblue",fg="blue").place(x=50,y=100)
        txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="lightblue",fg="blue").place(x=370,y=100)
        txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=130,width=250)

        c_no=Label(frame1,text="Contact Number",font=("times new roman",15,"bold"),bg="lightblue",fg="blue").place(x=50,y=170)
        txt_cno=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=50,y=200,width=250)

        email=Label(frame1,text="Email-id",font=("times new roman",15,"bold"),bg="lightblue",fg="blue").place(x=370,y=170)
        txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=200,width=250)


        #self.btn_img=ImageTk.PhotoImage(file="C:\\Users\\Ravish Reddy\\Desktop\\PROJECT\\r1.png")
        #btn=Button(frame1,image=self.btn_img).place(x=50,y=350,width=350,height=60)
        btn=Button(frame1,text="REGISTER",font=("times new roman",15,"bold"),bg="lightblue",fg="blue").place(x=50,y=350,width=250)
        btn=Button(frame1,text="QUIT!",command=self.root.destroy,font=("times new roman",15,"bold"),bg="lightblue",fg="blue").place(x=50,y=450,width=250)
        
        btn=Button(frame1,text="click here to login with fingervein",font=("times new roman",15,"bold"),bg="lightblue",fg="blue").place(x=370,y=450,width=300)
        cam=cv2.VideoCapture(0)
        while (True):
            ret, frame=cam.read()
            cv2.imshow('photo',frame)
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imwrite('image.png',gray)
            cam.release()
           

        
        

        
root=Tk()
obj=Register(root)
root.mainloop()
