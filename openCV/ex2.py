# Author Zhiyi Yang
import cv2


imageRGB=cv2.imread('/Users/yangzhiyi/Desktop/openCV/Test_images/Lenna.png')
cv2.namedWindow("Original_Image")

blue,green,red=cv2.split(imageRGB)
cv2.namedWindow("Red")
cv2.namedWindow("Green")
cv2.namedWindow("Blue")

imageYIQ=cv2.cvtColor(imageRGB,cv2.COLOR_BGR2YCrCb)
Y,Cb,Cr=cv2.split(imageYIQ)
cv2.namedWindow("Y")
cv2.namedWindow("Cb")
cv2.namedWindow("Cr")

imageHSV=cv2.cvtColor(imageRGB,cv2.COLOR_BGR2HSV)
hu,sat,val=cv2.split(imageHSV)
cv2.namedWindow("Hue")
cv2.namedWindow("Saturation")
cv2.namedWindow("Value")

cv2.imshow("Original_Image",imageRGB)
cv2.imshow("Red",red)
cv2.imshow("Blue",blue)
cv2.imshow("Green",green)
cv2.imshow("Y",Y)
cv2.imshow("Cb",Cb)
cv2.imshow("Cr",Cr)
cv2.imshow("Hue",hu)
cv2.imshow("Saturation",sat)
cv2.imshow("Value",val)

print('RGB_pixel_value_range',imageRGB[20,25])
print('YIQ_pixel_value_range',imageYIQ[20,25])
print('HSV_pixel_value_range',imageHSV[20,25])
cv2.waitKey(0)
