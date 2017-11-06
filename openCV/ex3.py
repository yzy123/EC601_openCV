# Author Zhiyi Yang
import cv2
from numpy import*




def add_gaussian_noise(imag,mean,sigma):
    noise_array = imag.copy()
    noise_array = random.normal(mean,sigma,imag.shape)
   
    add(imag,noise_array,imag,casting="unsafe")
    
    return;

def add_salt_pepper_noise(imag,pa,pb):
    len1 = (int)(imag.size * pa)
    len2 = (int)(imag.size * pb)
    
    for counter in range (0,len1):
        imag[(int)(random.uniform(0,imag.shape[0]))][(int)(random.uniform(0,imag.shape[1]))] = 0

    for counter in range (0,len2):
        imag[(int)(random.uniform(0,imag.shape[0]))][(int)(random.uniform(0,imag.shape[1]))] = 255

 
 
image = cv2.imread('/Users/yangzhiyi/Desktop/openCV/Test_images/Lenna.png',0)

cv2.imwrite('Original_Image.jpg',image)


kernel = [(3,3),(5,5),(7,7)]

mean = [0,5,10,20]
sigma = [0,20,50,100]

for k in range(0,3):
    for i in range(0,4):
        for j in range(0,4):
            nimage = image.copy()
            name = 'Gaussian_Noise mean: %d, sigma: %d_.jpg' % (mean[i],sigma[j])
            add_gaussian_noise(nimage,mean[i],sigma[j])
            cv2.imwrite(str(name),nimage)

            
            imageaf = nimage.copy()
            name = 'Box_filter mean: %d, sigma: %d, kernel_size: %dx%d_.jpg' % (mean[i],sigma[j],kernel[k][0],kernel[k][0])
            cv2.blur(imageaf,kernel[k],imageaf)
            cv2.imwrite(str(name),imageaf)

            

            imageaf1 = nimage.copy()    
            name = 'Gaussian_filter mean: %d, sigma: %d, kernel_size: %dx%d_.jpg' % (mean[i],sigma[j],kernel[k][0],kernel[k][0])
            cv2.GaussianBlur(nimage,kernel[k],1.5,imageaf1)
            cv2.imwrite(str(name),imageaf1)

            

            imageaf2 = nimage.copy()        
            name = 'Median_filter mean: %d, sigma: %d, kernel_size: %dx%d_.jpg' % (mean[i],sigma[j],kernel[k][0],kernel[k][0])
            cv2.medianBlur(nimage,kernel[k][0],imageaf2)
            cv2.imwrite(str(name),imageaf2)

            




pa = [0.01,0.03,0.05,0.4]
pb = [0.01,0.03,0.05,0.4]
for k in range (0,3):
    for i in range(0,4):
        for j in range(0,4):
            nimage2 = image.copy()
            name = 'Salt and Pepper Noise, pa: %f, pb: %f_.jpg' % (pa[i],pb[j])
            add_salt_pepper_noise(nimage2,pa[i],pb[j])
            cv2.imwrite(str(name),nimage2)

        

            imageaf3 = nimage2.copy()
            name = 'Box filter, pa: %f, pb: %f, kernel_size: %dx%d_.jpg' % (pa[i],pb[j],kernel[k][0],kernel[k][0])
            cv2.blur(imageaf3,kernel[k],imageaf3)
            cv2.imwrite(str(name),imageaf3,)


            imageaf4 = nimage2.copy()
            name = 'Gaussian filter, pa: %f, pb: %f, kernel_size: %dx%d_.jpg' % (pa[i],pb[j],kernel[k][0],kernel[k][0])
            cv2.GaussianBlur(imageaf4,kernel[k],1.5,imageaf4)
            cv2.imwrite(str(name),imageaf4)


            imageaf5 = nimage2.copy()
            name = 'Median filter, pa: %f, pb: %f, kernel_size: %dx%d_.jpg' % (pa[i],pb[j],kernel[k][0],kernel[k][0])
            cv2.medianBlur(imageaf5,kernel[k][0],imageaf5)
            cv2.imwrite(str(name),imageaf5,)

cv2.waitKey(0)
