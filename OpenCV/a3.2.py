import cv2

cam = cv2.VideoCapture(0)

while True:
    _ , img = cam.read()
    img = cv2.resize(img,(400,300))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray_blur = cv2.GaussianBlur(img_gray, (7,7), 0)
    img_edge = cv2.Canny(img_gray_blur,70,10)

    for i in range (0,300):
        for j in range (0,400):
            if img_edge[i,j] > 0:
                img_gray_blur[i,j] = 40


    cv2.imshow("Webcam", img_gray_blur)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break