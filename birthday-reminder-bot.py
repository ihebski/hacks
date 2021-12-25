#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

'''
Birthday reminder BOT - Send reminder to a group of coworkers one day before the actual birthday date.
You can run the script with crontab:
0 9 * * * /usr/bin/python3 birthday-bot.py
@ihebski
'''
from email.message import EmailMessage
from datetime import datetime, timedelta
import datetime
import yaml
import smtplib

# Read YAML file
with open("birthday.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)

# Get Today date
today = datetime.datetime.now().date()
# Email list of all coworkers
group = [v['email'] for k,v in data_loaded.items()]


# Function to send emails
def sendReminder(to_email, subject, message, server='smtp.example.cn',from_email='birthday.bot@example.com'):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)
    msg.set_content(message)
    server = smtplib.SMTP(server)
    server.set_debuglevel(1)
    server.login(from_email, 'password')  # user & password
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')

    
# Send reminder one day before the actual birthday date
for coworker, info in data_loaded.items():
    birthday = datetime.datetime.strptime(info['birthday'], "%d-%m-%Y").date()- timedelta(days=1)
    if today.day == birthday.day and today.month == birthday.month:
        group.remove(info['email'])
        sendReminder(to_email=group,subject=f'Birthday Reminder BOT !', message=f'Hello Team,\nTomorow is {coworker} birthday :D \nRegards.')
