from tkinter import *
from PIL import Image,ImageTk
from PIL import ImageTk, Image
from tkinter import filedialog
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
        #lb2=Label(window,text='',bg='lightpink',fg='white',font=('times',15,'bold'))
        #lb2.place(x=300,y=150)
        
        #self.btn_img=ImageTk.PhotoImage(file="C:\\Users\\Ravish Reddy\\Desktop\\PROJECT\\r1.png")
        #btn=Button(frame1,image=self.btn_img).place(x=50,y=350,width=350,height=60)
        #btn = Button(frame1, text ='open image', command = open_img).grid(row = 1, columnspan = 4)
        btn=Button(frame1,text="Upload",command = open_img,font=("times new roman",15,"bold"),bg="blue",fg="white").place(x=50,y=100,width=250)
        btn=Button(frame1,text="QUIT!",command=self.root.destroy,font=("times new roman",15,"bold"),bg="blue",fg="white").place(x=200,y=450,width=250)

        
        btn=Button(frame1,text="Capture",command=capture,font=("times new roman",15,"bold"),bg="blue",fg="white").place(x=370,y=100,width=250)
        btn=Button(frame1,text="Pre-processing",command=processing,font=("times new roman",15,"bold"),bg="blue",fg="white").place(x=50,y=400,width=250)
        btn=Button(frame1,text="Feature Extraction",command=capture,font=("times new roman",15,"bold"),bg="blue",fg="white").place(x=370,y=400,width=250)
def capture():
    cam=cv2.VideoCapture(0)
    while (True):
        ret, frame1=cam.read()
        #cv2.imshow('photo',frame1)
        gray = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        cv2.imwrite('image.png',gray)
        cv2.imshow('image.png',gray)
        frame1.place(x=700,y=250)
        cam.release()

def open_img():
    # Select the Imagename  from a folder 
    x = openfilename()
  
    # opens the image
    img = Image.open(x)
      
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)
  
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
   
    # create a label
    panel = Label(root, image = img)
      
    # set the image as img 
    panel.image = img
    panel.place(x=700,y=245)


def openfilename():
  
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title ='fingerimage')
    return filename

def processing():
    import cv2 as cv
    import numpy as np
    from matplotlib import pyplot as plt
    e1 = cv.getTickCount()
    img = cv.imread('crop.jpeg')

    median = cv.medianBlur(img,5) 
    e2 = cv.getTickCount()
    t = (e2-e1)/cv.getTickFrequency()
    print ("median time:",t)
    #plt.subplot(121),plt.imshow(img),plt.title('Original')
    #plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(median),plt.title('filtered')
    plt.xticks([]), plt.yticks([])
    plt.show().place(x=900,y=250)
    cv.waitKey(0)
    cv.destroyAllWindows()

    

        
root=Tk()
obj=Register(root)
root.mainloop() 
