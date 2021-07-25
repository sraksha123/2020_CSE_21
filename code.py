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
    convnet = fully_connected(convnet, 8, activation='softmax')
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
        model_out = model.predict([data])[0]
        print(model_out)
        print('model {}'.format(np.argmax(model_out)))
        if np.argmax(model_out) == 0:
            
str_label = 'Lasya'
        elif np.argmax(model_out) == 1:
            str_label = 'Ramya'
        elif np.argmax(model_out) == 3:
            str_label = 'Rahul'
        elif np.argmax(model_out) == 2:
            str_label = 'Harish'
        elif np.argmax(model_out) == 4:
            str_label = 'Keerthi'        
        elif np.argmax(model_out) == 5:
            str_label = 'Raksha'        
        elif np.argmax(model_out) == 6:
            str_label = 'MeghaHS'        
        elif np.argmax(model_out) == 7:
            str_label = 'Meghana'
     if str_label == name:
            global status
            global res
            res="Finger Matched"
            status= name
            message = tk.Label(text='Name: '+status, background="light blue",
                           fg="black", font=("", 15,"bold"))
            message.place(x=710,y=610)
            def entry():               
                row = [ name, res]
                with open('Result\\Result.csv','a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                print("successfully updated")
                button.destroy()
                root.destroy()                
            button = tk.Button(text=res, command=entry, activebackground = 

"green",font=("", 12,"bold"))
            button.place(x=710,y=660)
            button1=tk.Button(root,text="insert",command=insert,bg="cyan",font=('italic', 15, ' bold '))
            button1.place(x=710,y=700)
        else:
            global res1
            
res1="Finger mismatched"
            #status= "mismatched"
            status=name
            message = tk.Label(text='Name: '+status, background="light blue",
                           fg="Red", font=("", 15,"bold"))
            message.place(x=710,y=610)
            def entry():             
                row = [ name, res1]
                with open('Result\\Result.csv','a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                print("successfully updated")
                button.destroy()
                root.destroy()                
            button = tk.Button(text=res1, command=entry, activebackground = "green")
            button.place(x=710,y=660)
