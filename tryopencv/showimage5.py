#code to create run video for multiple screen
import os
import cv2
import numpy as np
video_path1=r'H:\automation_scripts\learn\imag\canada1.mp4'
cap=cv2.VideoCapture(video_path1)
while cap.isOpened():
    ret,frame=cap.read()
    if ret:
        image=cv2.resize(frame,(400,300))
        img_2=np.hstack((image,image))
        img_4=np.vstack((img_2,img_2))
        cv2.imshow('video Player',img_4)
        if cv2.waitKey(25)&0xff==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
     