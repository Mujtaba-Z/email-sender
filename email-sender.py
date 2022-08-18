import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

email = input("enter your email: ")
password = input("enter your password: ")
receiver = input("what email do you want to send to: ")

server.login(email, password)

server.sendmail(email, receiver, 'Hello World!')

print('mail sent!')
