import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "xxx@gmail.com"  # Enter your address
receiver_email = "xxx@gmail.com"  # Enter receiver address
password = 'xxx' #Insert your app password by going into google security settings, enabling 2 factor auth, then creating an app and inserting the password here
message = """\
Subject: Hi there
This message is sent from Python."""
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


'''Comment Added by Shamoon'''