# convert single image into parts
import cv2
import os
import numpy as np
# take a image with full path
full_path=r'H:\automation_scripts\learn\imag'
img_name_list=os.listdir(full_path)
for img_name in img_name_list:
    nam=full_path+'\\'+ img_name
    # print(nam)
    img=cv2.imread(nam)
    img=cv2.resize(img,(300,200))
    img_2=np.hstack((img,img))
    img_4=np.vstack((img_2,img_2))
    cv2.imshow('4 image',img_4)
    cv2.waitKeyEx(500)
cv2.destroyAllWindows()