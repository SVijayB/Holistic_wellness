import smtplib
from random import randint
import re

def update_pass(email):
    gmailaddress="Holistic.wellness.help@gmail.com"
    gmailpass="abcd321@"
    mailto=email
    code=str(randint(100000,999999))
    mes=("Your new verification code is " + code)
    mailServer=smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(gmailaddress,gmailpass)
    mailServer.sendmail(gmailaddress,mailto,mes)
    print("\n sent")
    mailServer.quit()
    return code

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
	if(re.match(regex, email)):
		return True

	else:
		return False