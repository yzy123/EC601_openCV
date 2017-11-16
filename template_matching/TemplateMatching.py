# author Zhiyi Yang 
import numpy as np
import cv2


# src: source image, temp: template image, stepsize: the step size for
# sliding the template
def TemplateMatching(src, temp, stepsize):
    mean_t = 0
    var_t = 0
    location = [0, 0]
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------
    for i in np.arange(0, temp.shape[0]):
        for j in np.arange(0, temp.shape[1]):
            mean_t = mean_t + temp[i, j]
    mean_t = mean_t / (i * j)

    for i in np.arange(0, temp.shape[0]):
        for j in np.arange(0, temp.shape[1]):
            var_t = var_t + (temp[i, j] - mean_t)**2
    var_t = var_t / (i * j)

    max_corr = 0
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0
            var_s = 0
            corr = 0
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------
            for p in np.arange(0, temp.shape[0]):
                for k in np.arange(0, temp.shape[1]):
                    mean_s = mean_s + src[p + i, k + j]
            mean_s = mean_s / (p * k)
            for p in np.arange(0, temp.shape[0]):
                for k in np.arange(0, temp.shape[1]):
                    var_s = var_s + (src[p + i, k + j] - mean_s)**2
            var_s = var_s / (p * k)
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------
            for p in np.arange(0, temp.shape[0]):
                for k in np.arange(0, temp.shape[1]):
                    corr = corr + (src[p + i, k + j] -
                                   mean_s) * (temp[p, k] - mean_t)
            corr = corr / (p * k) / (var_t * var_s)
            if corr > max_corr:
                max_corr = corr
                location = [i, j]
    return location


# load source and template images
source_img = cv2.imread('source_img.jpg', 0)  # read image in grayscale
temp = cv2.imread('template_img.jpg', 0)  # read image in grayscale
location = TemplateMatching(source_img, temp, 20)
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)
# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------
cv2.rectangle(
    match_img,
    (location[1],
     location[0]),
    (location[1] +
     temp.shape[1],
     location[0] +
     temp.shape[0]),
    (0,
     0,
     255),
    5)
# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------
cv2.imwrite('Matching result image' + '.jpg', match_img)
# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
