import os
import numpy as np
import cv2

width = 1280
hieght = 720
channel = 3
 
fps = 300
sec = 15

fourcc = cv2.VideoWriter_fourcc(*'MP42')
 
video = cv2.VideoWriter('image_to_video.avi', fourcc, float(fps), (width, hieght))
 
directry = r'images'
 
img_name_list = os.listdir(directry)
 
for frame_count in range(fps*sec):
    
    img_name = np.random.choice(img_name_list)
    img_path = os.path.join(directry, img_name)
    img = cv2.imread(img_path)
    img_resize = cv2.resize(img, (width, hieght))
     
    video.write(img_resize)
     
video.release()