#send a basic email

import smtplib

#connect to SMTP server and create SMTP object. google is smtp.gmail.com. port is 587
smtpObj = smtplib.SMTP('smtp.example.com', 587)

#say hello to server. it returns a tuple that starts with 250
smtpObj.elho()

#enables encryption. 
smtpObj.starttls()

#login to the SMTP server. email address and password
#gmail requires application-specific passwords http://nostarch.com/automatestuff/ 
smtpObj.login('bobexample.com', ' MY_SECRET_PASSWORD')

#you can send an email. takes your email address. takes recipient email. takes email body starting with Subject and the \n goes to the body
#returns an empty string if successful
smtpObj.sendmail('bobexample.com', 'alice@example.com', 'Subject: So Long.\n Dear Alice, so long and thanks for all the fish. Sincereley, Bob')

#disconnects from the SMTP server
smtpObj.quit()