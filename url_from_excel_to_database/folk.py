import requests
domain= "fokatech.com"
auth_url = "https://"+domain+"/wp-json/jwt-auth/v1/token"
auth_data = {
            "username":'fokatech123',
            "password":'y0XlrSielh0FTg0t!K0exzsy'
        }
auth_responce = requests.post(auth_url , json=auth_data)
try:
    token = auth_responce.json().get('data').get('token')
except AttributeError:
    token = auth_responce.json().get('token')
# print(auth_responce.json().get('data').get('token'))
print(token)