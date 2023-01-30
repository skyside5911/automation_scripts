#import modules
import requests
import time
import io
from moviepy.editor import *
import mysql.connector

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont,ImageOps,ImageFilter
from bs4 import BeautifulSoup
from io import BytesIO
mydb = mysql.connector.connect(
  host="64.227.176.243",
  user="phpmyadmin",
  password="Possibilities123.@",
  database="stories_to_shorts"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM destination_website where status = 1 ")
myresult = mycursor.fetchall()
listt=[]
for des_id in myresult:
  listt.append(des_id[0])
# print(listt)
bfw_li=[]
folder_path=r'H:\automation_scripts\web_stories\all_images'

for des in listt:
  mycursor.execute("SELECT * FROM bulk_feed_website where des_id=(%s)" %  (des))
  websites = mycursor.fetchall()
  bfw_li.extend(websites)
alll=[]
for bfw_idd in bfw_li:
  mycursor.execute("SELECT * FROM bulk_feed_content where bfw_id=(%s) and status is Null " % (bfw_idd[0]) )
  webs = mycursor.fetchall()
  alll.extend(webs)

count=0
for x in alll:
    
#web stories url to extract images and text
    page = requests.get(x[2])
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
                font = ImageFont.truetype("arial.ttf", 43)

                # Define the position and text to add
                text = text_list[count]
                textwidth, textheight = draw.textsize(text, font)
                x = (im.width - textwidth) / 2 
                y = (im.height - textheight) / 2 +400

                # Define the background color
                bgcolor = "white"
                # Add the text with background
                print('x ==',x,'y ==',y,x + textwidth, y + textheight)
                draw.rectangle([x, y, x + textwidth, y + textheight], fill=bgcolor)
                draw.text((x, y), text, font=font, fill="black")
                im.show()
                im.save(r"H:\automation_scripts\web_stories\all_images\raj{}.jpg".format(count))
                
                clips.append(ImageClip(r"H:\automation_scripts\web_stories\all_images\raj{}.jpg".format(count)).set_duration(3))
                count+=1
            else:
                continue   
        except:
            pass
    for filename in os.scandir(folder_path):
        if filename.is_file():
            os.remove(filename.path)
    video_clip=concatenate_videoclips(clips,method='compose')
    video_clip.write_videofile(r"H:\automation_scripts\web_stories\all_images\video12.mp4",fps=24,remove_temp=True,codec='libx264',audio_codec='aac')
    video11=VideoFileClip(r"H:\automation_scripts\web_stories\all_images\video12.mp4")
    song=AudioFileClip(r"H:\automation_scripts\web_stories\song.mp3")
    songg=song.subclip(0,len(clips)*3)
    final_video=video11.set_audio(songg)
    final_video.write_videofile(r'H:\automation_scripts\web_stories\newvideo2.mp4')
    for filename in os.scandir(folder_path):
        if filename.is_file():
            os.remove(filename.path)