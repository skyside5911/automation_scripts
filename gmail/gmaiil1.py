import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "aman.grimbyte@gmail.com"
receiver_email = ["amanonline864@gmail.com","akrha777@gmail.com.com"]
#receiver_email = "rachit@grimbyte.com, rajan@grimbyte.com"
Password = "your pass word"
# instance of MIMEMultipart
msg = MIMEMultipart()
# storing the senders email address
msg['From'] = smtp_server
# storing the receivers email address
# msg['To'] = receiver_email
# storing the subject
msg['Subject'] = "domain file"
# string to store the body of the mail
body = "output file"
# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))
# open the file to be sent
filename = r"email\131022news_silo.csv"
attachment = open(filename, "rb")
# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')
# To change the payload into encoded form
p.set_payload((attachment).read())
# encode into base64
encoders.encode_base64(p)
fa ="aman.csv"
p.add_header('Content-Disposition', "attachment; filename= %s" % fa)
# attach the instance 'p' to instance 'msg'
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, Password)
    for rec in receiver_email:
        msg['To'] = rec
        msg.attach(p)
        text = msg.as_string()
        # # sending the mail
        server.sendmail(smtp_server,rec, text)
    # terminating the session
    server.quit()