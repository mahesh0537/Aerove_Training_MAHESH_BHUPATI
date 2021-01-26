import cv2
import numpy as np

img = cv2.imread("image1.jpeg")
img = cv2.resize(img,(400,300))
cv2.imshow("Initial image", img)
img_blue = img.copy()
img_blue[:,:,:1] = 180
img_blue[:,:,1:] = 0
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([10,100,100])
upper_red = np.array([180,225,225])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
blue_mask = cv2.bitwise_and(img,img_blue,mask=mask1)
img[:,:,2:] = 0
for i in range(0,300):
    for j in range (0,400):
        if blue_mask[i,j,:1] > 0:
            #img[i,j] = [0,0,0]
            img[i,j] = blue_mask[i,j]




#cv2.imshow("mask", mask1)
#cv2.imshow("Final image", blue_mask)
cv2.imshow("Final",img)
cv2.waitKey(0)