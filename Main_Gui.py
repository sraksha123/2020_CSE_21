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
import pandas as pd
import numpy as np
global root
root = Tk()

root.title("FingerVein Prediction")
root.geometry("1100x750")
##root.geometry("1280x990")
#root.configure(background ="LightCyan3")
BG = PhotoImage(file = 'bg3.png')
label = ttk.Label(root, image = BG ,bd=0)

lbl = tk.Label(root, text="FINGER VEIN RECOGNITION",width=30  ,height=1  ,fg="Black"  ,bg="light blue" ,font=('Arial', 30, ' bold ') ) 
lbl.place(x=200, y=2)

lbl2 = tk.Label(root, text="Enter  Name",width=15  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold ')) 
lbl2.place(x=300, y=150)

txt2 = tk.Entry(root,width=15  ,bg="White"  ,fg="Black", font=('Arial', 15, ' bold ')  )
txt2.place(x=500, y=150)
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
    import cv2  
    import numpy as np  
    import os  
    import matplotlib.pyplot as plt
    from random import shuffle 
    from tqdm import \
        tqdm  
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
            median = cv2.medianBlur(img,5)
            edges = cv2.Canny(img,200,300)
            plt.subplot(121),plt.imshow(img,cmap = 'gray')
            plt.subplot(122),plt.imshow(edges,cmap = 'gray')
            #edges = cv2.Canny(img,200,300)
            #plt.subplot(121),plt.imshow(img,cmap = 'gray')
            #plt.subplot(122),plt.imshow(edges,cmap = 'gray')
            
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
            str_label = 'Meghana H S'
        elif np.argmax(model_out) == 1:
            str_label = 'Keerthi'
        elif np.argmax(model_out) == 2:
            str_label = 'Raksha'
        elif np.argmax(model_out) == 3:
            str_label = 'Meghana G R'
        
        
   
        if str_label == name:
            global status
            global res
            res="Finger Matched"
            status= name
            message = tk.Label(text='Name: '+status, background="light blue",
                           fg="black", font=("", 15,"bold"))
            message.place(x=500,y=380)
            def entry():
                #row = [Id , name, res]
                row = [ name, res]
                with open('Result\\Result.csv','a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                print("successfully updated")
                button.destroy()
                root.destroy()
                
            button = tk.Button(text=res, command=entry, activebackground = "green",font=("", 12,"bold"))
            button.place(x=500,y=430)


        else:# str_label == name:
           # global status
            global res1
            res1="Finger mismatched"
            status= "mismatched"
            message = tk.Label(text='Name: '+status, background="light blue",
                           fg="Red", font=("", 15,"bold"))
            message.place(x=500,y=380)
            def entry():
                #row = [Id , name, res1]
                row = [ name, res1]
                with open('Result\\Result.csv','a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                print("successfully updated")
                button.destroy()
                root.destroy()
                
            button = tk.Button(text=res1, command=entry, activebackground = "green")
            button.place(x=500,y=430)
            
def openphoto():
    global Id
    global name
    #Id=txt.get()
    name=txt2.get()
    dirPath = "testpicture"
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        os.remove(dirPath + "/" + fileName)
    # C:/Users/sagpa/Downloads/images is the location of the image which you want to test..... you can change it according to the image location you have  
    fileName = askopenfilename(initialdir='C:\\Users\\Ravish Reddy\\Desktop\\PROJECT\\finger_vein_detection - Copy\\test', title='Select image for analysis ',
                           filetypes=[('image files', '.jpg')])
    dst = "testpicture"
    print(fileName)
    print (os.path.split(fileName)[-1])
    if os.path.split(fileName)[-1].split('.') == 'h (1)':
        print('dfdffffffffffffff')
    shutil.copy(fileName, dst)
    load = Image.open(fileName)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(image=render, height="250", width="500",bg="Lightblue")   
    img.image = render
    img.place(x=300, y=100)

    #plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    #img.grid(column=0, row=1, padx=10, pady = 10)
    #title.destroy()
    button1.destroy()
    global button2
    button2 = tk.Button(text="Submit", command=analysis,bg="cyan",font=('Arial', 15, ' bold '))
    #button2 = tk.Button(text="Submit", command=analysis)
    button2.place(x=500,y=400)
    #button2.grid(column=0, row=20, padx=10, pady = 10)
button1 = tk.Button(text="Fetch", command = openphoto,bg="cyan",font=('Arial', 15, ' bold '))
button1.place(x=500,y=200)
#button1.grid(column=0, row=1, padx=10, pady = 10)

##root.mainloop()

label.pack()
#root.bind('<congigure>',resizer)
root.mainloop()


















