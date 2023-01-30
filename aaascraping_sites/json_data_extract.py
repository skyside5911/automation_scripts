import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
#data from shopify
product_list=[]
url='https://helmboots.com/products.json?limit=250&page=1'
r=requests.get(url)
data=r.json()
'''soup=BeautifulSoup(r.content,'html.parser')
script=soup.find_all('script')[4].text.strip()
data=json.loads(script)'''
for item in (data['products']):
    
    title=(item['title'])
    handle=(item['handle'])
    created=(item['created_at'])
    product_type=(item['product_type'])
    for image in item['images']:
        try:
            imagesrc=image['src']
        except:
            imagesrc="None"
    for varient in item['variants']:
        price=varient['price']
        sku=varient['sku']
        available=varient['available']
        product={
            'title':title,
            'handle':handle,
            'product_type':product_type,
            'created':created,
            'price':price,
            'sku':sku,
            'available':available,
            'image':imagesrc
        }
        product_list.append(product)
df=pd.DataFrame(product_list)
df.to_csv('shopifydata.csv')
    # print(title,handle,created,product_type)