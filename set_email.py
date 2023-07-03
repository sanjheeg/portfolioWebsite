import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "sanjheeg30@gmail.com"
password = "xrddlkavgpuedycb"
receiver = "sanjheeg30@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: test
hi!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
