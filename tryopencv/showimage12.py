import os
import cv2
from PIL import Image
os.listdir(r"H:\automation_scripts\learn")
total_width=0
total_height=0
for file in os.listdir('.'):
    im=Image.open(os.path.join(r"H:\automation_scripts\learn",file))
    width,height=im.size
    total_width+=width
    total_height+=height
numofimages=len(os.listdir('.'))
mean_width=int(total_width/numofimages)  #calculating the width for each image
mean_height=int(total_height/numofimages)  #calculating the height for each image 
for file in os.listdir('.'):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        im=Image.open(os.path.join(r"H:\automation_scripts\learn",file))
        imResize=im.resize((mean_width,mean_height),Image.ANTIALIAS)
        imResize.save(file,'JPEG',quality=95)

def generate_video():
    image_folder = '.' # Use the folder
    video_name = 'mygeneratedvideo.avi'
    os.listdir(r"H:\automation_scripts\learn")
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or
             img.endswith(".jpeg") or img.endswith("png")]
   
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') 

    # Array images should only consider 
    # the image files ignoring others if any 
    
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    
    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, fourcc, 5, (width, height))

    # Appending the images to the video one by one 
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder,image)))
        
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()
    video.release()  # releasing the video generated 
    
generate_video()
