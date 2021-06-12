from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk, Image
import cv2
import os
import sys
from tkinter import *
import tkinter as ttk
from tkinter.filedialog import askopenfilename
import numpy as np 
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
global status
import shutil

window = tk.Tk()

window.title("Finger vein_detection")
#BG = PhotoImage(file = 'bg3.png')
#label = ttk.Label(window, image = BG)

window.geometry("1380x1000")
window.configure(background ="lightblue")
lbl = tk.Label(window, text="FINGER VEIN RECOGNITION",width=30  ,height=1  ,fg="Black"  ,bg="light blue" ,font=('Arial', 30, ' bold ') ) 
lbl.place(x=350, y=10)
title = tk.Label(text="", background = "light blue", fg="black", font=("times", 15))
title.place(x=550,y=100)


def analysis():
    import cv2  # working with, mainly resizing, images
    import numpy as np  # dealing with arrays
    import os  # dealing with directories
    from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
    from tqdm import \
        tqdm  # a nice pretty percentage bar for tasks. Thanks to viewer Daniel BA1/4hler for this suggestion
    verify_dir = 'testpicture'
    IMG_SIZE = 50
    LR = 1e-3
    MODEL_NAME = 'finger_vein_detection-{}-{}.model'.format(LR, '2conv-basic')

    def process_verify_data():
        verifying_data = []
        for img in tqdm(os.listdir(verify_dir)):
            path = os.path.join(verify_dir, img)
            img_num = img.split('.')[0]
            img = cv2.imread(path, cv2.IMREAD_COLOR)
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            verifying_data.append([np.array(img), img_num])
        np.save('verify_data.npy', verifying_data)
        return verifying_data
##    def Send():
##        data.write(str.encode('C'))
##        print('Sent the Character')

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

    convnet = fully_connected(convnet, 5, activation='softmax')
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
            str_label = 'Megha'
        elif np.argmax(model_out) == 1:
            str_label = 'Keerthi'
        elif np.argmax(model_out) == 2:
            str_label = 'Raksha'
        elif np.argmax(model_out) == 3:
            str_label = 'MehaHS'
        elif np.argmax(model_out) == 4:
            str_label='Not Matched'
        #elif np.argmax(model_out) == 4:
            #str_label = 'Mismatch'
        


        global b
        if str_label == 'Megha':
            Name = "Megha"
            message = tk.Label(text='Name: ' + Name, background="blue",
                               fg="Black", font=("", 15))
            message.place(x=650,y=380)
            button = tk.Button(text="Finger matched", command=exit, activebackground = "green")
            button.place(x=650,y=430)
            
        elif str_label == 'Keerthi':
            Name = "Keerthi"    
            message = tk.Label(text='Name: ' + Name, background="blue",
                               fg="Black", font=("", 15))
            message.place(x=650,y=380)
            button = tk.Button(text="Finger matched", command=exit, activebackground = "green")
            button.place(x=650,y=430)
            

        elif str_label == 'Raksha':
            Name = "Raksha"      
            message = tk.Label(text='Name: ' + Name, background="blue",
                               fg="Black", font=("", 15))
            message.place(x=650,y=380)
            button = tk.Button(text="Finger matched", command=exit, activebackground = "green")
            button.place(x=650,y=430)
            

        elif str_label == 'MehaHS':
            Name = "MehaHS"  
            message = tk.Label(text='Name: ' + Name, background="blue",
                               fg="Black", font=("", 15))
            message.place(x=650,y=380)
            button = tk.Button(text="Finger matched", command=exit, activebackground = "green")
            button.place(x=650,y=430)

        elif str_label == 'Not Matched':
            Name = "Not Matched"  
            message = tk.Label(text='Name: ' + Name, background="blue",
                               fg="Black", font=("", 15))
            message.place(x=650,y=380)
            button = tk.Button(text="Finger Mis-matched", command=exit, activebackground = "green")
            button.place(x=650,y=430)


def openphoto():
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
    img.place(x=470, y=100)
    title.destroy()
    button1.destroy()
    button2 = tk.Button(text="Detect", command=analysis)
    button2.place(x=670,y=380)
button1 = tk.Button(text="Upload Photo", command = openphoto)
button1.place(x=700,y=150)


label.pack()
window.mainloop()
