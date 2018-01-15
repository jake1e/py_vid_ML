import cv2
import numpy as np

#capture the webcam for video
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    #converting color frame from BGR to HSV
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #HSV hue sat value
    lower_red = np.array([130, 87, 111], np.uint8)
    upper_red = np.array([180,255,255], np.uint8)

    #find the color red in video
    red = cv2.inRange(HSV, lower_red, upper_red)

    #transformation, Dilation
    kernel = np.ones((5, 5), "uint8")

    red = cv2.dilate(red, kernel)
    res = cv2.bitwise_and(img, img, mask = red)

    #tracking of red
    (_,contour,hierarch)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contour):
        area = cv2.contourArea(contour)
        if area > 300:
            x,y,w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
            cv2.putText(img, "red apple", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255))

    #show videos - before/after
    cv2.imshow('frame', img)

    #close all with Esc
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        cap.release()
        cv2.destroyAllWindows()
        break
