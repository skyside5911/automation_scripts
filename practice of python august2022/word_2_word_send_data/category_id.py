import requests
import json
auth_url = "https://www.onlinecasinogames777.com/wp-json/jwt-auth/v1/token"
auth_data = {
      "username":"admin",
    "password":"pwd12345"
}
auth_responce = requests.post(auth_url , json=auth_data)
token = auth_responce.json().get('data').get('token')
print(auth_responce.json().get('data').get('token'))
source_url = "https://theleafdesk.com/wp-json/wp/v2/posts?_embed"
source_urll = "https://theleafdesk.com/wp-json/wp/v2/categories"
destination_url ="https://www.onlinecasinogames777.com/wp-json/wp/v2/posts/"
url ="https://www.onlinecasinogames777.com/wp-json/wp/v2/categories/"
count=0
data = requests.get(source_urll).json()
for p in data:
    count+=1
    id=p['id']
    name=p['name']
    slug=p['slug']
    
    post={ 'name':name,
       'slug':slug
    }
    header = {'Authorization': 'Bearer ' + token}
    responce = requests.post(url , headers=header, json=post)
    postid = str(json.loads(responce.content)['id'])
    updatepst={
      'id':postid
    }
    requests.post(url+postid, headers=header, json=updatepst)
    print(type(postid))
    print(postid)
    print(responce)
    if count==1 :
      break