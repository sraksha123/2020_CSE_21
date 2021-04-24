from tkinter import *
import tkinter as tk
import cv2  
import time
import sys
import os
window=tk.Tk()
window.title('Fingervein')
window.geometry('600x600')
window.configure(background='blue')
lb1=Label(window,text='Fingervein',width=15,height=2,bg='black',fg='white',font=('times',30,'bold'))
lb1.place(x=100,y=10)
lb2=Label(window,text='enter you name',width=15,bg='black',fg='white',font=('times',15,'bold'))
lb2.place(x=100,y=150)
lb2=Label(window,text='',width=15,bg='black',fg='white',font=('times',15,'bold'))
lb2.place(x=300,y=150)

def text():
    #cam=cv2.VideoCapture(0)
    #while True:
        #ret, frame=cam.read()
        img=cv2.imread('C:\\Users\\Ravish Reddy\\Desktop\\finger.jpeg')
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow('photo',gray)
        cv2.imwrite('image.png',gray)
        #cv2.imshow('photo',img)
        #cv2.imshow('photo',frame)
        #cv2.imwrite('image.png',frame)
        #time.sleep(2)
        #cam.release()
btn1=Button(window,text='click here',command=text,width=10,height=2,bg='black',fg='white',font=('times',15,'bold'))
btn1.place(x=100,y=200)


btn2=Button(window,text='QUIT',command=window.destroy,width=10,height=2,bg='black',fg='white',font=('times',15,'bold'))
btn2.place(x=350,y=200)
