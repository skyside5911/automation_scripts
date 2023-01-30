#import modules
import requests
import time
import io
from moviepy.editor import *
import cv2
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont,ImageOps,ImageFilter
from bs4 import BeautifulSoup
from io import BytesIO

#web stories url to extract images and text
page = requests.get("https://nypost.com/web-stories/scooby-doo-reboot-velma-under-fire-for-sexualizing-teens/")
ff = BeautifulSoup(page.content,"html.parser")
image_first=ff.find_all(class_="page-fullbleed-area")
#extract images and text from the web stories
count=0

clips=[]

for i in image_first:
    my_text=i.text
    # time.sleep(1)
    # print(i.text)
    count+=1
    try:
        bb=(i.find('amp-img').get('src'))
        if ".jpg" in bb:
            image_path=bb
        else:
            continue   
    except:
        pass
def break_long_title(my_txt):
    with open("texta.txt",'w') as ff:
        ff.write(my_txt)
    ff.close()
    rr1 = open('texta.txt','r')
    rr2 = rr1.read()
    ff3 = rr2.split(' ')
    for i in range(8,len(ff3),8):
        ffa =  open("texta.txt",'r')
        new_ff = ffa.read()
        add_new = new_ff.replace(ff3[i]+' ',ff3[i]+"\n")
        with open("texta.txt",'w') as final_f:
            final_f.write(add_new)
def add_box_on_image(img_path):
    image = cv2.imread(img_path)
    overlay = image.copy()
    # Rectangle parameters
    x, y, w, h = 0, 470, 1200, 300
    # A filled rectangle
    cv2.rectangle(overlay, (x, y), (x+w, y+h), (0,0,0), -1)
    alpha = 0.7 # Transparency factor.
    # Following line overlays transparent rectangle
    # over the image
    image_new = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 1)
    cv2.imwrite(r"H:\automation_scripts\web_stories\out_image{}.jpg".format(count), image_new)
    add_text_on_image(r"H:\automation_scripts\web_stories\out_image{}.jpg".format(count))
def img_resize(img_path):
    image = Image.open(img_path)
    new_image = image.resize((1160, 630))
    new_image.save(r"H:\automation_scripts\web_stories\out_image{}.jpg".format(count))
    add_box_on_image(r"H:\automation_scripts\web_stories\out_image{}.jpg".format(count))
def add_text_on_image(img_path):
    bg = Image.open(img_path).convert('RGB')
    x = bg.width//2
    y = bg.height//2
    # The text we want to add
    rr1 = open('texta.txt','r')
    rr2 = rr1.read()
    # Create font
    font = ImageFont.truetype(r'C:\Windows\Fonts\ARLRDBD.TTF', 40)
    # Create piece of canvas to draw text on and blur
    blurred = Image.new('RGBA', bg.size)
    draw = ImageDraw.Draw(blurred)
    draw.text(xy=(572,552), text=rr2, fill='blue', font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(1))
    # Paste soft text onto background
    bg.paste(blurred,blurred)
    bg = bg.resize((1080, 1920))
    
    # Draw on sharp text
    draw = ImageDraw.Draw(bg)
    draw.text(xy=(570, 550), text=rr2, fill='white',font=font, anchor='mm')
    bg.save(r"H:\automation_scripts\web_stories\out_image{}.jpg".format(count))
if "__main__"==__name__:
    print("name")
    
    break_long_title(my_text)
    img_resize(image_path)
