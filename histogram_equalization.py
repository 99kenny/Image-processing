import cv2
import numpy as np
from matplotlib import pyplot as plt

PATH = "under_lena.png"
# import lena image to grayscale
img = cv2.imread("PATH", cv2.IMREAD_GRAYSCALE)
# 원본 이미지 확인jpg
cv2.imshow('Original Image',img)
# original histogram display
hist_origin = plt.figure("Original Histogram")
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
hist_origin.show()

# lib equalization
equ = cv2.equalizeHist(img)
cv2.imshow('Equalized Image',equ)
# lib equalized histogram display
hist_equalized_lib = plt.figure("Equalized Histogram")
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
hist_equalized_lib.show()
# my equalization
G = 256
w,h = img.shape
size = w*h
hist = np.zeros(256)
# make histogram 
for i in img.flatten():     
    hist[i] += 1
cum = np.zeros(256)
# to cumulative
cum[0] = hist[0]
for i in range(1,255):
    cum[i] = cum[i-1] + hist[i]
# image transfromation
equalized_img = np.zeros(size)
cum = np.round((cum / size) * 255)
for i,g in enumerate(img.flatten()):
    equalized_img[i] = cum[g]

# my equalization histrogram 
hist_equalized = plt.figure("My Equalized Histogram")
plt.hist(equalized_img,256,[0,256], color = 'r')
plt.xlim([0,256])
hist_equalized.show()
# check my equalized image
equalized_img = equalized_img.reshape((w,h)).astype(np.uint8)
cv2.imshow("My Equalized Image", equalized_img)
cv2.imwrite("new.jpg", equalized_img)
while(True):
    if cv2.waitKey(1) & 0xFF == ord('x'):
        cv2.destroyAllWindows()
        break