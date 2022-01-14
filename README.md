# opencv_simple_codes
Simple use cases that can be solved by leveraging OpenCV Python

## Skew Correction

[Projection Profile Method](https://stackoverflow.com/questions/59660933/how-to-de-skew-a-text-image-also-retrieve-the-new-bounding-box-of-that-image). This method is done by rotating images at different angles and computing the histogram of pixels for each angle. Skew angle is determined by the maximum difference between the peaks of the pixels.
```python
image = cv2.imread('images/skew.png')
angle, rotated = correct_skew(image, 0.3, 5)
cv2.imwrite('results/rotated.png', rotated)
cv2.waitKey()
```
