# Project: Final Project
# Purpose Details: Sends an email to psu account
# Course: IST 411
# Author: Ian Roach
# Date Developed: 11/26/17
# Last Date Changed: 11/26/17
# Rev: 1.0.1

import smtplib
from email.mime.text import MIMEText

class Email:

    def __init__(self, subject, fromAdd, toAdd):
        self.connection = smtplib.SMTP_SSL('authsmtp.psu.edu', 465)
        self.subject = subject
        self.fromAdd = fromAdd
        self.toAdd = toAdd

    def sendMail(self):
        try:
            msg = MIMEText("This is an email from team4s' final project.")
            msg['Subject'] = self.subject
            msg['From'] = self.fromAdd
            msg['To'] = self.toAdd
            self.connection.sendmail(self.fromAdd, self.toAdd, msg.as_string())
        except Exception as e:
            print("Error {}".format(e.args[0]))
