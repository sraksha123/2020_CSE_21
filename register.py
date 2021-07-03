from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk, Image
import cv2
import os
import sys
from tkinter import *
import tkinter as ttk
#import random
import csv
#import pandas as pd
import numpy as np
from tkinter import *
from PIL import Image,ImageTk
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2  
import time
import sys
import os
#import firebase
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightblue")
        sidebar = tk.Frame(root, width=250, bg='gray', height=500, relief='sunken', borderwidth=2)
        btn=Button(root,text="Upload",command = nextPage,font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=1,y=1,width=250)
        btn=Button(root,text="Real time Capture",command=capture,font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=1,y=40,width=250)
        sidebar.pack(expand=False, fill='both', side='left', anchor='nw')
        #firebase = firebase.FirebaseApplication('https://fingervein-f27bc-default-rtdb.firebaseio.com/', None)
    
        #fingervein=firebase.get("","fingervein")
        lbl = tk.Label(root, text="FINGER VEIN RECOGNITION",width=30  ,height=1  ,fg="Black"  ,bg="light blue" ,font=('Arial', 30, ' bold ') ) 
        lbl.place(x=350, y=2)
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
        btn=Button(frame1,text="Upload",command = nextPage,font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=50,y=100,width=250)
        btn=Button(frame1,text="QUIT!",command=self.root.destroy,font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=200,y=450,width=250)
        lb3 = tk.Label(root, text="Finger vein recognition \n This technology uses intrinsic biometric \n traits for identification" ,width=30  ,height=1  ,fg="Blue"  ,bg="light blue" ,font=('Times New Roman', 30, ' italic ') ) 
        lb3.place(x=490, y=250,width=700,height=200)
        
        btn=Button(frame1,text="Real time Capture",command=capture,font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=370,y=100,width=250)
        
       # btn=Button(frame1,text="Pre-processing",command=processing,font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=50,y=400,width=250)
        #btn=Button(frame1,text="Feature Extraction",command=capture,font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=370,y=400,width=250)

def nextPage():
    root.destroy()
    import Main_Gui

def main():
    #from tkinter import *
    import tkinter as tk
    from PIL import Image
    from PIL import ImageTk, Image
    import cv2
    import os
    import sys
    #from tkinter import *
    import tkinter as ttk
    import random
    import csv
    import pandas as pd
    import numpy as np
    global root
    root = Tk()

    root.title("FingerVein Prediction")

    ##root.geometry("1280x990")
    #root.configure(background ="LightCyan3")
    BG = PhotoImage(file = 'bg3.png')
    label = ttk.Label(root, image = BG)
    #PhotoImage(file = 'Lotus-Flowers.png')

    lbl = tk.Label(root, text="FINGER VEIN RECOGNITION",width=30  ,height=1  ,fg="Black"  ,bg="light blue" ,font=('Arial', 30, ' bold ') ) 
    lbl.place(x=350, y=2)

    #lbl = tk.Label(root, text="Enter  ID",width=15  ,height=1  ,fg="Black"  ,bg="White" ,font=('Arial', 15, ' bold ') ) 
    #lbl.place(x=500, y=100)

    #txt = tk.Entry(root,width=15  ,bg="White" ,fg="Black",font=('Arial', 15, ' bold '))
    #txt.place(x=710, y=100)

    lbl2 = tk.Label(root, text="Enter  Name",width=15  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold ')) 
    lbl2.place(x=500, y=150)

    txt2 = tk.Entry(root,width=15  ,bg="White"  ,fg="Black", font=('Arial', 15, ' bold ')  )
    txt2.place(x=710, y=150)

    
    ##def CNN():
    ##    lbl = tk.Label(root, text="You have Selected CNN",width=25  ,height=1  ,fg="Black"  ,bg="LightCyan3" ,font=('Arial', 20, ' bold ') ) 
    ##    lbl.place(x=450, y=100)
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
    import shutil
    import os
    import sys
    import cv2
    import numpy as np 
    from PIL import Image, ImageTk
    import matplotlib.pyplot as plt
    global status
    ##sift=cv2.xfeatures2d.SIFT_create()

    ##title = tk.Label(text="Click below to choose picture ", background = "light blue", fg="Brown", font=("", 15))
    ##title.place(x=450,y=100)
    ##def submit():
        
    def analysis():
        button2.destroy()
        import cv2  # working with, mainly resizing, images
        import numpy as np  # dealing with arrays
        import os  # dealing with directories
        from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
        from tqdm import \
            tqdm  # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
        verify_dir = 'testpicture'
        IMG_SIZE = 50
        LR = 1e-3
        MODEL_NAME = 'finger_vein_detection_new-{}-{}.model'.format(LR, '2conv-basic')

        def process_verify_data():
            verifying_data = []
            for img in tqdm(os.listdir(verify_dir)):
                path = os.path.join(verify_dir, img)
                img_num = img.split('.')[0]
                img = cv2.imread(path, cv2.IMREAD_COLOR)
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            
    ##                    return func1()
                verifying_data.append([np.array(img), img_num])
            np.save('verify_data.npy', verifying_data)
            return verifying_data

        verify_data = process_verify_data()
        #verify_data = np.load('verify_data.npy')
        import tflearn
        from tflearn.layers.conv import conv_2d, max_pool_2d
        from tflearn.layers.core import input_data, dropout, fully_connected
        from tflearn.layers.estimator import regression
        import tensorflow as tf
       # tf.reset_default_graph()

        convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 3], name='input')

        convnet = conv_2d(convnet, 32, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 64, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 128, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 32, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = conv_2d(convnet, 64, 3, activation='relu')
        convnet = max_pool_2d(convnet, 3)

        convnet = fully_connected(convnet, 1024, activation='relu')
        convnet = dropout(convnet, 0.8)

        convnet = fully_connected(convnet, 4, activation='softmax')
        convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

        model = tflearn.DNN(convnet, tensorboard_dir='log')

        if os.path.exists('{}.meta'.format(MODEL_NAME)):
            model.load(MODEL_NAME)
            print('model loaded!')

        import matplotlib.pyplot as plt

        fig = plt.figure()

        for num, data in enumerate(verify_data):

            img_num = data[1]
            img_data = data[0]

            y = fig.add_subplot(3, 4, num + 1)
            orig = img_data
            data = img_data.reshape(IMG_SIZE, IMG_SIZE, 3)
            # model_out = model.predict([data])[0]
            model_out = model.predict([data])[0]
            print(model_out)
            print('model {}'.format(np.argmax(model_out)))


            if np.argmax(model_out) == 0:
                str_label = 'MeghanaHS'
            elif np.argmax(model_out) == 1:
                str_label = 'Keerthi'
            elif np.argmax(model_out) == 2:
                str_label = 'Raksha'
            elif np.argmax(model_out) == 3:
                str_label = 'Meghana'

       
            if str_label == name:
                global status
                global res
                res="Finger Matched"
                status= name
                message = tk.Label(text='Status: '+status, background="light blue",
                               fg="black", font=("", 15,"bold"))
                message.place(x=650,y=380)
                def entry():
                    row = [name, res]
                    with open('Result\\Result.csv','a+') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(row)
                    csvFile.close()
                    print("successfully updated")
                    button.destroy()
                    root.destroy()
                    
                button = tk.Button(text=res, command=entry, activebackground = "green")
                button.place(x=650,y=430)


            else:# str_label == name:
               # global status
                global res1
                res1="Finger mismatched"
                status= "mismatched"
                message = tk.Label(text='Status: '+status, background="light blue",
                               fg="Red", font=("", 15,"bold"))
                message.place(x=650,y=380)
                def entry():
                    row = [name, res1]
                    with open('Result\\Result.csv','a+') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(row)
                    csvFile.close()
                    print("successfully updated")
                    button.destroy()
                    root.destroy()
                    
                button = tk.Button(text=res1, command=entry, activebackground = "green")
                button.place(x=700,y=430)
                
    def openphoto():
        #global Id
        global name
        #Id=txt.get()
        name=txt2.get()
        dirPath = "testpicture"
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            os.remove(dirPath + "/" + fileName)
        # C:/Users/sagpa/Downloads/images is the location of the image which you want to test..... you can change it according to the image location you have  
        fileName = askopenfilename(initialdir='C:\\Users\\Ravish Reddy\\Desktop\\PROJECT\\finger_vein_detection\\test', title='Select image for analysis ',
                               filetypes=[('image files', '.jpg')])
        dst = "testpicture"
        print(fileName)
        print (os.path.split(fileName)[-1])
        if os.path.split(fileName)[-1].split('.') == 'h (1)':
            print('dfdffffffffffffff')
        shutil.copy(fileName, dst)
        load = Image.open(fileName)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(image=render, height="250", width="500")   
        img.image = render
        img.place(x=470, y=200)
        #img.grid(column=0, row=1, padx=10, pady = 10)
        #title.destroy()
        button1.destroy()
        global button2
        button2 = tk.Button(text="Submit", command=analysis)
        button2.place(x=650,y=400)
        #button2.grid(column=0, row=20, padx=10, pady = 10)
    button1 = tk.Button(text="Get Photo", command = openphoto)
    button1.place(x=650,y=200)
    #button1.grid(column=0, row=1, padx=10, pady = 10)

    ##root.mainloop()

    #os.system("python ui_Bone.py")


    ##takeImg = tk.Button(root, text="CNN", command=CNN  ,fg="Black"  ,bg="blue"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
    ##takeImg.place(x=600, y=550)

    ##trackImg = tk.Button(root, text="Quit", command=root.destroy  ,fg="Black"  ,bg="blue"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
    ##trackImg.place(x=800, y=550)

    label.pack()
    root.mainloop()


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
    x = openfilename()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image = img)
    panel.image = img
    panel.place(x=525,y=245)


def openfilename():
    filename = filedialog.askopenfilename(title ='fingerimage')
    return filename

def processing():
    import numpy as np
    import cv2 as cv
    from matplotlib import pyplot as plt
    img = cv.imread('C:\\Users\\Ravish Reddy\\Desktop\\PROJECT\\crop.jpeg',0)
    edges = cv.Canny(img,200,300)
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Database Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

        
root=Tk()
obj=Register(root)
root.mainloop()
