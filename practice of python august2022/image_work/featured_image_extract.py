import re
import bs4
import requests
import csv
from bs4 import BeautifulSoup
url='https://www.sportzmode.com/other/how-are-the-baltimore-ravens-looking-for-this-weekends-match-up-against-the-cleveland-browns/17653/'
url_split=url.split('.com')
complete_site_name=url_split[0] + ".com"
print(complete_site_name)
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
images = soup.select('.wp-post-image')
print(images)
hello = soup.find(attrs={'class':'.b-loaded'})
print(hello)
image_link_srcset=[]
for tag in soup.findAll(): 
    # if ".jpg" in tag.get("src"):    
        image_link_srcset.append(tag)     
    # if(tag.name=="img"):   
    #     image_link_srcset.append(tag) 
        # if ".jpg" in tag.get("src"):  
        #     image_link_srcset.append(tag.get("src"))
        # if "https" not in tag.get("src"):
        #     image_link_srcset=complete_site_name+tag.get("src")[0]
            
        
img1024=[]
print(image_link_srcset)
# hello = soup.find(attrs={'class':'featured-image hero-image caption'}).get('srcset')
for img in image_link_srcset:
    if "1024w" in img:
        img1024.append(img)
        
print(img1024)    
a=(image_link_srcset[0].split(" "))
if "https" not in a:
    a=complete_site_name+a[0]
print(a)

