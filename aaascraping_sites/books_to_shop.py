import requests
from bs4 import BeautifulSoup
import pandas as pd
book_stock=[]
for i in range(1,4):
    url=f'https://books.toscrape.com/catalogue/page-{i}.html'
    r= requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    article=soup.find_all('article',class_='product_pod')

    for book in article:
        title=book.find_all('a')[1]['title']
        price=book.find('p',class_='price_color').text[2:]
        statuss=book.find('p',class_='instock availability').text.strip()
        books={
            'title':title,
            'price':price,'status':statuss
        }
        book_stock.append(books)
df=pd.DataFrame(book_stock)
# df.to_csv(r'H:\automation_scripts\a_extracting_using_bs4_req\book_stock.csv')
df.to_excel(r'H:\automation_scripts\a_extracting_using_bs4_req\book_stock.xlsx')