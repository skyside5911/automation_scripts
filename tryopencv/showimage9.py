import numpy as np
import cv2
import os
width=1280
height=720
channel=3
fps=30
sec=15
fourcc=cv2.VideoWriter_fourcc(*'MP42')
video=cv2.VideoWriter('textT5.mp4',fourcc,float(fps),(width,height))
for frame_count in range(fps*sec):
    img=np.random.randint(0,255,(height,width,channel),dtype=np.uint8)
    video.write(img)
'''directory=r'H:\automation_scripts\learn\imag'
img_name_list=os.listdir(directory)
for frame_count in range(fps*sec):
    img_name=np.random.choice(img_name_list)
    img_path=os.path.join(directory,img_name)
    img=cv2.imread(img_path)
    img_resize=cv2.resize(img,(width,height))
    video.write(img_resize)'''
video.release()