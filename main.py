import cv2
import numpy as np

img_path = r"000027.jpg"

image = cv2.imread(img_path)
image = cv2.resize(image, (1280, 720))

pt1 = (450, 40)
pt2 = (800, 420)

img_rect = cv2.rectangle(image, pt1, pt2, (0, 255, 0), 2, cv2.LINE_4)

cv2.imshow('Rect', img_rect)

cv2.waitKey(0)
cv2.destroyAllWindows()