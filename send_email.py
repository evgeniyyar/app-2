import smtplib
import ssl

host = "smtp.gmail.com"
port = 465
username = "evgeniyyar18@gmail.com"
password = "wiffyeggirzaqfkk"

receiver = "evgeniyyar18@gmail.com"

context = ssl.create_default_context()

message = "111"

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
















#wiff yegg irza qfkk