# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("hmsglory6318@gmail.com", "2020100169")

# message to be sent
message = "hi we are from  hotel glory jgmm "

# sending the mail
s.sendmail("hmsglory6318@gmail.com", "priyankgupta292@gmail.com", message)

# terminating the session
s.quit()
