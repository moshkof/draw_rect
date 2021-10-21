import cv2
import numpy as np

img_path = r"000027.jpg"

image = cv2.imread(img_path)
image = cv2.resize(image, (1280, 720))

pt1 = (450, 40)
pt2 = (800, 420)

img_rect = cv2.rectangle(image, pt1, pt2, (0, 255, 0), 1, cv2.LINE_4)

text = 'Vouuu...'
org = (455, 70)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (0, 255, 14)
linType = cv2.LINE_4

img_text = cv2.putText(img_rect, text, org, fontFace, fontScale, color, linType)

cv2.imshow('Rect', img_rect)

cv2.waitKey(0)
cv2.destroyAllWindows()