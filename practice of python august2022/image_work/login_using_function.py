import mysql.connector
import requests
# driver=webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver")
mydb = mysql.connector.connect(
  host="64.227.176.243",
  user="phpmyadmin",
  password="Possibilities123.@",
  database="automation"
)
def login_site():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM destination_website where status = 1 ")
    myresult = mycursor.fetchall()
    for dir in myresult:
        domain=dir[1]
        auth_url = "https://"+domain+"/wp-json/jwt-auth/v1/token"
        
        
    
        wp_user = dir[2]
        wp_pwd = dir[3]


        auth_data = {
                "username":wp_user,
                "password":wp_pwd
            }
        auth_responce = requests.post(auth_url , json=auth_data)
        token = auth_responce.json().get('data').get('token')
        print(auth_responce.json().get('data').get('token'))
login_site()