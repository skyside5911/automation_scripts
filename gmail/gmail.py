import smtplib
myemail = "arunpandit5911@gmail.com"
mypassword = "Karnal@123"
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login("arunpandit5911@gmail.com", "Karnal@123")
smtpserver.sendmail(from_addr=myemail,to_addrs="shushantrana096@gmail.com",msg="this is first mail")
smtpserver.close()
print("done")