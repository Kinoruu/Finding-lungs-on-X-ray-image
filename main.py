import argparse
import cv2
import numpy as np

img = cv2.imread('00000011_000.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('00000011_000.png', cv2.IMREAD_COLOR)
img3 = cv2.imread('00000011_000.png', cv2.IMREAD_COLOR)
h, w, c = img.shape
cv2.imshow('normal', img)

mean = np.mean(img)
mean -= 24

img = cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
cv2.imshow('blur', img)

for iter1 in range(h):
    for iter2 in range(w):
        val = img[iter1,iter2,1]
        if (val < mean):
            img[iter1,iter2] = [0,0,0]

cv2.imshow('dark', img)

img = cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
cv2.imshow('blur', img)


ret, thresh1 = cv2.threshold(img, mean, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold', thresh1)

contours, hierarchy = cv2.findContours(thresh1[:,:,0], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 77,22,174
img_cont = cv2.drawContours(img, contours, -1,(60,250,74),2)
cv2.imshow('all_contours', img_cont)

contourss = []
contourss2 = []
contourss3 = []

for c in contours:
    hull = cv2.convexHull(c)
    contourss.append(hull)

img_cont_1 = cv2.drawContours(img2, contourss, -1,(200,0,200), 2)
cv2.imshow('all_contours_hulled', img_cont_1)

for c in contourss:
    if (cv2.contourArea(c) > (0.04 * h * w)) and (cv2.contourArea(c) < (0.5 * h * w)):
        contourss2.append(c)

for c in contourss2:
    temp = np.zeros_like(img3)
    cv2.drawContours(temp, [c], 0, (255, 255, 255), -1)
    if np.mean(img3[temp == 255]) < mean:
        contourss3.append(c)

contourss4 = []

# hull = cv2.convexHull(cnt)

img_cont_2 = cv2.drawContours(img3, contourss3, -1,(0,0,200), cv2.FILLED)
cv2.imshow('e', img_cont_2)

cv2.waitKey(0)
cv2.destroyAllWindows()