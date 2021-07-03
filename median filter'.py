import cv2
import numpy as np
from matplotlib import pyplot as plt
e1 = cv2.getTickCount()
img = cv2.imread('img2.bmp')
median = cv2.medianBlur(img,5) 
e2 = cv2.getTickCount()
t = (e2-e1)/cv2.getTickFrequency()
print ("median time:",t)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
