import smtplib
from random import randint
import re
from dotenv import load_dotenv
import os


def update_pass(email):
    load_dotenv()
    gmailaddress = os.getenv("gmailaddress")
    gmailpass = os.getenv("gmailpass")
    mailto = email
    code = str(randint(100000, 999999))
    mes = "Your new verification code is " + code
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(gmailaddress, gmailpass)
    mailServer.sendmail(gmailaddress, mailto, mes)
    mailServer.quit()
    return code


regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def check(email):
    if re.match(regex, email):
        return True

    else:
        return False
