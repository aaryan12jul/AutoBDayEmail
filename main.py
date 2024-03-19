# Imports
import pandas
import datetime as dt
import smtplib
import random

# Constant Email & Password
EMAIL = "aaryan12jul@gmail.com"
PASSWORD = "ogbn djjw lewa vfrw"

# Getting Birthday
birthday = pandas.read_csv("birthdays.csv")
bmonth = birthday.month.to_list()
bday = birthday.day.to_list()
now = dt.datetime.now()
row = birthday[(birthday.month == now.month) & (birthday.day == now.day)]

# Checking If It is Someones Birthday
if len(row) > 0:
    # Checking How Many Peoples Birthday it Is
    for i in range(len(row)):
        # Creating Updated Letter
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", 'r') as file:
            message = file.read()
            finalized_message = message.replace("[NAME]", f"{row.name[i]}")
        
        # Sending Letter
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=row.email[i], msg=f"Subject:Happy Birthday!\n\n{finalized_message}")