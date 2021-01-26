import cv2

img = cv2.imread("image1.jpeg")
img = cv2.resize(img,(400,300))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
img_edge = cv2.Canny(img_gray_blur,150,20)
img_gray_t = img_gray.copy()
for i in range (0,300):
    for j in range (0,400):
        if img_gray_t[i,j] > 30 and img_gray_t[i,j] < 60:
            img_gray_t[i,j] = 100

img_gray_t = cv2.GaussianBlur(img_gray_t, (3,3), 0)

for i in range (0,300):
    for j in range (0,400):
        img_gray_t[i,j] = int(((2.0/3.0)*img_gray[i,j] +(1.0/3.0)*img_gray_t[i,j]))

for i in range (0,300):
    for j in range (0,400):
        if img_edge[i,j] > 0:
            img_gray_t[i,j] = 10
        

cv2.imshow("Sketch", img_gray_t)
cv2.waitKey(0)