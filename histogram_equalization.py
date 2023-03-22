import cv2
import numpy as np
from matplotlib import pyplot as plt

# lena 이미지 grayscale로 임포트
img = cv2.imread("C:/Users/99san/Workspace/computer_vision/kakao.", cv2.IMREAD_GRAYSCALE)
# 원본 이미지 확인jpg
cv2.imshow('Original Image',img)
# 원본 히스토그램 display
hist_origin = plt.figure("Original Histogram")
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
hist_origin.show()

# lib equalization
equ = cv2.equalizeHist(img)
cv2.imshow('Equalized Image',equ)
# lib equalized 히스토그램 display
hist_equalized_lib = plt.figure("Equalized Histogram")
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
hist_equalized_lib.show()
# my equalization
G = 256
w,h = img.shape
size = w*h
hist = np.zeros(256)
# histogram 생성
for i in img.flatten():     
    hist[i] += 1
cum = np.zeros(256)
# 누적확률분포함수
cum[0] = hist[0]
for i in range(1,255):
    cum[i] = cum[i-1] + hist[i]
# 이미지 변환
equalized_img = np.zeros(size)
cum = np.round((cum / size) * 255)
for i,g in enumerate(img.flatten()):
    equalized_img[i] = cum[g]

# my equalization 히스토그램 display
hist_equalized = plt.figure("My Equalized Histogram")
plt.hist(equalized_img,256,[0,256], color = 'r')
plt.xlim([0,256])
hist_equalized.show()
# my equalized 이미지 확인
equalized_img = equalized_img.reshape((w,h)).astype(np.uint8)
cv2.imshow("My Equalized Image", equalized_img)
cv2.imwrite("new.jpg", equalized_img)
while(True):
    if cv2.waitKey(1) & 0xFF == ord('x'):
        cv2.destroyAllWindows()
        break