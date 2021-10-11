import argparse
import cv2
import numpy as np

img = cv2.imread('00000010_000.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('00000010_000.png', cv2.IMREAD_COLOR)
img3 = cv2.imread('00000010_000.png', cv2.IMREAD_COLOR)
h, w, c= img.shape
#cv2.imshow('a', img)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gb = cv2.GaussianBlur(img,(15,15),cv2.BORDER_DEFAULT)
#cv2.imshow('b', img_gb)
ret, thresh1 = cv2.threshold(img_gb, 100, 255, cv2.THRESH_BINARY)
#cv2.imshow('c', thresh1)

contours, hierarchy = cv2.findContours(thresh1[:,:,0], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#77,22,174
img_cont = cv2.drawContours(img, contours, -1,(60,250,74),2)
#cv2.imshow('d', img_cont)

contourss = []
contourss2 = []
contourss3 = []

for c in contours:
    #epsilon = 0.001 * cv2.arcLength(c, True)
    #approx = cv2.approxPolyDP(c, epsilon, True)
    hull = cv2.convexHull(c)
    contourss.append(hull)

for c in contourss:
    if (cv2.contourArea(c) > 10000) and (cv2.contourArea(c) < (0.5 * h * w)):
        contourss2.append(c)

print(len(contours))
print(len(contourss))
print(len(contourss2))

for c in contourss2:
    temp = np.zeros_like(img3)
    cv2.drawContours(temp, [c], 0, (255, 255, 255), -1)
    if np.mean(img3[temp == 255]) < 120:
        contourss3.append(c)

print(len(contourss3))

contourss4 = []

#hull = cv2.convexHull(cnt)

img_cont_2 = cv2.drawContours(img2, contourss3, -1,(0,0,200), cv2.FILLED)
cv2.imshow('e', img_cont_2)

cv2.waitKey(0)
cv2.destroyAllWindows()