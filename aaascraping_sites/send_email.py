import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
total_price=''
server.login('yourmail@gmail.com','yourpassword')
subject='your upgrade price today'
body=f'this is total price to upgrade today is {total_price}'
message=f'subject: {subject}\n\n{body}'
server.sendmail('emailfrom@gmail.com','email_to@gmail.com',message)
print("email sent")
server.quit()