import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("sanjay.sadashivam@omaza.in","Tester@2025")
server.sendmail("sanjay.sadashivam@omaza.in","subir.singh@omaza.in","Your Test execution failed!. please check ASAP")
server.quit()