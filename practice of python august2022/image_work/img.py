from bs4 import BeautifulSoup #Import stuff
import requests

r  = requests.get("https://www.onlykaty.com/entertainment/black-panther-2-with-tchalla/14206/") #Download website source

data = r.text  #Get the website source as text

soup = BeautifulSoup(data) #Setup a "soup" which BeautifulSoup can search

links = []

for link in soup.find_all('img'):  #Cycle through all 'img' tags
    imgSrc = link.get('src')   #Extract the 'src' from those tags
    links.append(imgSrc)    #Append the source to 'links'

print(links)