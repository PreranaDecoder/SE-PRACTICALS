# PRN:-2030331245036

# importing the library
import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('charlie992002@gmail.com',password="lpgo wgxu ywce bdfl")
otp = ''.join([str(random.randint(0,9)) for i in range(4)])
msg = 'Hello,Your OTP is '+str(otp)
server.sendmail('charlie992002@gmail.com','prerana.bhandari99@gmail.com', msg)
server.quit()
print(otp)
print(msg)
print(server)