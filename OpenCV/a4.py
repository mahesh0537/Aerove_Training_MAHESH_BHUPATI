import cv2
import numpy as np
img = cv2.imread("a4.png", 0)
img_real = cv2.imread("a4.png")
img = cv2.GaussianBlur(img, (5,5),0)
a, thresh = cv2.threshold(img, 150,225,0)
contour,hierarchy = cv2.findContours(thresh, 1, 2)
found = 0



for i in range (0, len(contour)):
    if cv2.arcLength(contour[i],True) > 20:
        arc = cv2.arcLength(contour[i],True)
        (x,y), r = cv2.minEnclosingCircle(contour[i])
        center = (int(x), int(y))
        r = int(r)
        center_store = [0,0]
        if center_store != center:
            epslon = 0.01*arc
            aprox = cv2.approxPolyDP(contour[i],epslon,True)
            if len(aprox) > 4 and i < 20:
                if found == 0: 
                    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=30,minRadius=64,maxRadius=70)
                    
                    if (circles is not None) and found == 0:
                        found +=1
                        circles = np.uint16(np.around(circles))
                        for i in circles[0,:]:
                            # draw the outer circle
                            if int(i[2]) < float(1.1*r) or int(i[2]) > float(0.9*r):
                                cv2.putText(img_real,"Circle", (center[0], center[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
                                circle_found = True
                else:
                    cv2.putText(img_real,"Oval", center, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
            if len(aprox) == 3:
                cv2.putText(img_real,"Triangle", center, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
            if len(aprox) == 4 and i < 20:
                #print(str(i)+' '+ str(len(aprox)) + ' '+ str(aprox))
                x1, y1, l, w = cv2.boundingRect(aprox)
                ratio = float(l/w)
                val_x = (aprox[0,0,0] - aprox[1,0,0])*(aprox[3,0,0] - aprox[0,0,0])
                val_y = (aprox[0,0,1] - aprox[1,0,1])*(aprox[0,0,1] - aprox[3,0,1])
                if ratio >= 0.90 and ratio <= 1.1:
                    cv2.putText(img_real,"Square", center, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
                #else:
                #    cv2.putText(img_real,"Rectangle", center, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
                elif val_x <= 1.1*val_y and val_x >= 0.9*val_y:
                    cv2.putText(img_real,"Rectangle", center, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
                else:
                    cv2.putText(img_real,"Rhombus", center, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

                

            center_store = center





cv2.imshow("Img", img_real)
cv2.waitKey(0)
cv2.destroyAllWindows()