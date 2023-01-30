import numpy as np
import cv2
import os
directory=r'H:\automation_scripts\learn\imag\im.jpg'
imag=cv2.imread(directory)
imag=cv2.resize(imag,(720,1280))
text='this is first image'
org=(100,200)
font=cv2.FONT_HERSHEY_COMPLEX
fontScale=6
color=(0,0,255)
thickness=3
lineType=cv2.LINE_AA
#to down the text use bottomLeftOrigin  true instead of false
bottomLeftOrigin=False
# imgg=cv2.putText(imag,text,org,font,fontScale,color,thickness,lineType,bottomLeftOrigin=True)
imgg=cv2.putText(imag,text,org,font,fontScale,color,thickness,lineType,bottomLeftOrigin)
cv2.imshow('text image',imgg)
cv2.waitKey()
cv2.destroyAllWindows()