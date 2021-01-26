import cv2 as cv
import numpy as np
import time

vid = cv.VideoCapture("vid.mp4")

while True:
    _ , img = vid.read()
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_gray = cv.GaussianBlur(img_gray, (3,3),0)
    circles = cv.HoughCircles(img_gray,cv.HOUGH_GRADIENT,1,10,param1=50,param2=30,minRadius=0,maxRadius=30)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(img,(i[0],i[1]),i[2],(0,255,0),2)


    cv.imshow("img",img)
    cv.imshow("grey",img_gray)
    if cv.waitKey(1) & 0xff == ord('q'):
        break
    time.sleep(0.03)