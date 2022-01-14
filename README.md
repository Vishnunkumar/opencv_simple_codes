# opencv_simple_codes
Simple use cases that can be solved by leveraging OpenCV Python

## Skew Correction
image = cv2.imread('images/skew.png')
angle, rotated = correct_skew(image, 0.3, 5)
cv2.imwrite('results/rotated.png', rotated)
cv2.waitKey()
