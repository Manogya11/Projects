import smtplib


fromaddr = 'hmsglory6318@gmail.com'  
toaddrs  = 'priyankgupta292@gmail.com'  
msg = 'Spam email Test'  

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login('hmsglory6318@gmail.com', '2020100169')
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()


