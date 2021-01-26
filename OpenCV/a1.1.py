import cv2

img = cv2.imread("image1.jpeg")
img = cv2.resize(img, (400,300))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t, img_bw = cv2.threshold(img_gray,80,225, cv2.THRESH_BINARY)

cv2.imshow("Image GRAY", img_gray)
cv2.imshow("Image Black and White", img_bw)
print(t)

cv2.waitKey(0)