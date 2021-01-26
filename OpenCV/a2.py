import cv2
import numpy as np

img = cv2.imread("a2.jpeg")
row, col, z = img.shape
r1 = cv2.getRotationMatrix2D((col/2,row/2),90,1)
r2 = cv2.getRotationMatrix2D((col/2,row/2),180,1)
r3 = cv2.getRotationMatrix2D((col/2,row/2),270,1)
r4 = cv2.getRotationMatrix2D((col/3,row/3),60,1)
m1 = np.array([[1,0,100],[0,1,100]],dtype="float32")
m2 = np.array([[1,0,10],[0,1,100]],dtype="float32")
m3 = np.array([[1,0,-100],[0,1,100]],dtype="float32")
m4 = np.array([[1,0,100],[0,1,-100]],dtype="float32")
img_blur = cv2.blur(img,(5,5))
img_gblur = cv2.GaussianBlur(img, (7,7),0)
img_r1 = cv2.warpAffine(img, r1, (col,row))
img_r2 = cv2.warpAffine(img, r2, (col,row))
img_r3 = cv2.warpAffine(img, r3, (col,row))
img_r4 = cv2.warpAffine(img, r4, (col,row))
img_m1 = cv2.warpAffine(img,m1,(col,row))
img_m2 = cv2.warpAffine(img,m2,(col,row))
img_m3 = cv2.warpAffine(img,m3,(col,row))
img_m4 = cv2.warpAffine(img,m4,(col,row))


cv2.imshow("Main image", img)
cv2.imshow("Blur", img_blur)
cv2.imshow("Gaussian Blur", img_gblur)
cv2.imshow("Rotation by 90", img_r1)
cv2.imshow("Rotation by 180", img_r2)
cv2.imshow("Rotation by 270", img_r3)
cv2.imshow("Rotation by 60 about ", img_r4)
cv2.imshow("Translation 1", img_m1)
cv2.imshow("Translation 2", img_m2)
cv2.imshow("Translation 3", img_m3)
cv2.imshow("Translation 4", img_m4)

cv2.waitKey(0)