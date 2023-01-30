#import modules
import requests
import time
import io
from moviepy.editor import *

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont,ImageOps,ImageFilter
from bs4 import BeautifulSoup
from io import BytesIO

#web stories url to extract images and text
page = requests.get("https://nypost.com/web-stories/scooby-doo-reboot-velma-under-fire-for-sexualizing-teens/")
ff = BeautifulSoup(page.content,"html.parser")
image_first=ff.find_all(class_="page-safe-area")
#extract images and text from the web stories

clips=[]
text_list=[]
for i in image_first:
    if len(i.text) ==0:
        continue
    words = (i.text).split()

    for i in range(len(words)):
        if (i+1) % 6 == 0:
            words.insert(i+1, "\n")

    # join the words list back into a single string
    new_paragraph = " ".join(words)
    text_list.append(new_paragraph)

count=0
for ii in image_first:
    try:
        bb=(ii.find('amp-img').get('src'))
        if ".jpg" in bb:
            print('img ==',bb)
            se = requests. get(bb)
            im = Image. open(BytesIO(se. content))
            im = im.resize((1080, 1920))
            draw = ImageDraw.Draw(im)

            # Define the coordinates of the box
            box = (100, 100, 200, 200)

            # Draw the box on the image
            draw.rectangle(box, fill=None, outline="green")
            myFont = ImageFont.truetype(r'C:\Windows\Fonts\ALGER.TTF', 40)
            f = ImageFont.load_default()
            txt=Image.new('L', (2874,1700))
            d = ImageDraw.Draw(txt)
            d.text( (200, 200),text=text_list[count],  font=myFont, fill=255)
            w=txt.rotate(0,  expand=50)
            im.paste( ImageOps.colorize(w, (0,0,0), (255,255,84)), (10,1260),  w)
            im.show()
            im.save(r"H:\automation_scripts\web_stories\raj{}.jpg".format(count))
            '''img_byte_arr = io.BytesIO()
            im.save(img_byte_arr, format='PNG')
            img_byte_aarrr = img_byte_arr.getvalue()
            
            im_string = img_byte_aarrr.decode()
            print(type(img_byte_aarrr))
            im.show()'''
            clips.append(ImageClip(r"H:\automation_scripts\web_stories\raj{}.jpg".format(count)).set_duration(3))
            count+=1
        else:
            continue   
    except:
        pass
video_clip=concatenate_videoclips(clips,method='compose')
video_clip.write_videofile(r"H:\automation_scripts\web_stories\video12.mp4",fps=24,remove_temp=True,codec='libx264',audio_codec='aac')
video11=VideoFileClip(r"H:\automation_scripts\web_stories\video12.mp4")
song=AudioFileClip(r"H:\automation_scripts\web_stories\song.mp3")
songg=song.subclip(0,len(clips)*3)
final_video=video11.set_audio(songg)
final_video.write_videofile(r'H:\automation_scripts\web_stories\newvideo2.mp4')