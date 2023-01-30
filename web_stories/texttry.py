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
for i in range(20):
    print(i)
    print(text_list[count])
    count+=1