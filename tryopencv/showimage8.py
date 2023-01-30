# to save the image
import cv2
import os

# take a image with full path
video_path=r'H:\automation_scripts\learn\imag\videoplayback.mp4'
os.mkdir(r"H:\automation_scripts\learn\video_to image")
cap=cv2.VideoCapture(video_path)
img_count=1
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        print("unable to read frame")
        break
    is_img_write=cv2.imwrite(r"H:\automation_scripts\learn\video_to_image\image{}.jpeg".format(img_count),frame)
    if is_img_write:
        print(f'image save at video_to_image\image{img_count}.jpeg')
    cv2.imshow("video",frame)
    cv2.waitKey(25)&0xff==ord('q')
    img_count+=1
cap.release()

cv2.destroyAllWindows()