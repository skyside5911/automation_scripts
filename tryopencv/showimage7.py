# to save the image
import cv2
import os

# take a image with full path
full_path=r'H:\automation_scripts\learn\imag'
img_name_list=os.listdir(full_path)
for img_name in img_name_list:
    nam=full_path+'\\'+ img_name
    # print(nam)
    img=cv2.imread(nam)
    img=cv2.resize(img,(1280,720))
    cv2.imwrite(r'H:\automation_scripts\learn\imag\try.jpeg',img)
    # cv2.imshow('image',img)
    # cv2.waitKey(1000)
cv2.destroyAllWindows()