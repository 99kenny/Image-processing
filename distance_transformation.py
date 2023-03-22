import cv2
import numpy as np
from matplotlib import pyplot as plt

# distance metric
def euclidean_d(a,b):
    return ((a[0]-b[0])**2 + (a[1] - b[1])**2)**0.5
def d4(a,b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])
def d8(a,b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1]))
def distance(d_type):
    result = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            result[i,j] = d_type([i,j],[1,1])
    return result
# 이미지 업로드
img = cv2.imread('C:/Users/99san/Workspace/computer_vision/distance_transformation.jpg', cv2.IMREAD_GRAYSCALE)
# binary 이미지로 변환
_,img = cv2.threshold(img, 123, 255, cv2.THRESH_BINARY)
dist_transformation = cv2.distanceTransform(img, cv2.DIST_L2, 3).astype(np.uint8)
# My Transformation
M, N = img.shape
transformed = np.zeros_like(img, dtype='float64')
transformed[np.where(img == 255)] = N + M

al = np.array([[1,1,1],
               [1,0,0],
               [0,0,0]])
br = np.array([[0,0,0],
               [0,0,1],
               [1,1,1]])

# distance metric 설정
dm = euclidean_d
# 이미지 padding
transformed = cv2.copyMakeBorder(transformed, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=M*N)
while(True):
    flag = False
    # top to bottom, left to right
    for r in range(1, M+1):
        for c in range(1, N+1):
            if transformed[r,c] != 0:
               df = (distance(dm)+transformed[r-1:r+2,c-1:c+2])*al
               df[1,1] = transformed[r,c]
               transformed[r,c] = np.min(df[np.nonzero(df)])
    # bottom to top, right to left
    for r in reversed(range(1,M+1)):
        for c in reversed(range(1,N+1)):
            if transformed[r,c] != 0:
               df = (distance(dm) + transformed[r-1:r+2,c-1:c+2])*br
               df[1,1] = transformed[r,c]
               transformed[r,c] = np.min(df[np.nonzero(df)])
    if np.any(transformed != N+M):
        break

transformed = transformed[1:M+1,1:N+1].astype(np.uint8)
# transformation 비교
transformed = ((transformed / np.max(transformed)) * 255)
dist_transformation = ((dist_transformation/np.max(dist_transformation))*255).astype(np.uint8)

cv2.imshow('Original Image',img)
cv2.imshow("my_dist_transformation",transformed.astype(np.uint8))
cv2.imshow("dist_transformation",dist_transformation)
cv2.waitKey()