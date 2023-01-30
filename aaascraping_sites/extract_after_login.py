import requests
loginurl='https://the-internet.herokuapp.com/authenticate/'
secureurl='https://the-internet.herokuapp.com/secure'
payload={
    'username':'rajrana',
    'password':'thisispassword'
}
r=requests.post(loginurl,data=payload)
r2=requests.get(secureurl)
print(r2.text)