import requests
from bs4 import BeautifulSoup
def download_img(img_url):
    get_nme = img_url.split("/")[-1]
    image_name = get_nme.split(".")[0]
    f = open(f'{image_name}.jpg','wb')
    f.write(requests.get(img_url).content)
    f.close()
page=requests.get("https://www.therconline.com/dating/is-pete-davidson-dating-jenna-ortega/16609/")
soup= BeautifulSoup(page.content,"html.parser")
aaa = soup.findAll(class_="aligncenter")
aaa1=soup.find(class_="cs-entry__title")
with open(r"title1.txt","w") as save1:
    save1.write(str(aaa1.text))
# print(aaa1.text)
for a in aaa:
    download_img(a['src'])