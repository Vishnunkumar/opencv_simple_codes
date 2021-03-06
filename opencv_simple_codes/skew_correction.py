import cv2
import numpy as np
from scipy.ndimage import interpolation as inter


def determine_score(arr, angle):
   '''
   function to rotate and compute the histogram of pixels
   '''

    data = inter.rotate(arr, angle, reshape=False, order=0)
    histogram = np.sum(data, axis=1)
    score = np.sum((histogram[1:] - histogram[:-1]) ** 2)
    return histogram, score

def correct_skew(image, delta, limit):
    
    '''
    Removal of skewness in the image
    '''
    
    # binarizing the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 3)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 
    
    # rotating image at different angles 
    scores = []
    angles = np.arange(-limit, limit + delta, delta)
    for angle in angles:
        histogram, score = determine_score(thresh, angle)
        scores.append(score)

    # Finding the angle with maximum difference between hists
    best_angle = angles[scores.index(max(scores))]
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    
    # Rotating image as per the removal of skewness
    M = cv2.getRotationMatrix2D(center, best_angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, \
              borderMode=cv2.BORDER_REPLICATE)

    return best_angle, rotated
  
  
# Example
image = cv2.imread('images/skew.png')
angle, rotated = correct_skew(image, 0.3, 5)
cv2.imwrite('results/rotated.png', rotated)
cv2.waitKey()
