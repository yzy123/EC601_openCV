# Author Zhiyi Yang
import cv2

image = cv2.imread('/Users/yangzhiyi/Desktop/openCV/Test_images/Lenna.png',1)

gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

cv2.imshow('Input Image',image)
  
threshold_type = 2
threshold_value = 128

ret,dst = cv2.threshold(gray,threshold_value,255,threshold_type)

cv2.imshow('Thresholded image',dst)

current_threshold = 128
max_threshold = 255


ret,thresholded = cv2.threshold(gray,current_threshold,max_threshold,cv2.THRESH_BINARY)

cv2.imshow('Binary threshold',thresholded)

# band thresholding
threshold1 = 27
threshold2 = 125

ret, binary_image1 = cv2.threshold(gray,threshold1,max_threshold,cv2.THRESH_BINARY)
ret , binary_image2 = cv2.threshold(gray,threshold2,max_threshold,cv2.THRESH_BINARY_INV)

band_thresholded_image = binary_image1 & binary_image2

cv2.imshow('Band Thresholding',band_thresholded_image)

# Semi thresholding
ret, semi_thresholded_image = cv2.threshold(gray,current_threshold,max_threshold,cv2.THRESH_BINARY_INV)
semi_thresholded_image = semi_thresholded_image & gray
cv2.imshow('Semi Thresholding', semi_thresholded_image)

# Adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,10)
cv2.imshow('Adaptive Thresholding', adaptive_thresh)

cv2.waitKey(0)