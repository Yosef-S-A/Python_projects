import smtplib
import pandas
import datetime as dt
import random

my_email = "************************"
password = "******************"

file_data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in file_data.iterrows()}

today = dt.datetime.now()
today_tuple = (today.month, today.day)

if today_tuple in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path, mode="r") as letter_draft:
        letter = letter_draft.read()
        msg = letter.replace("[NAME]", birthday_dict[today_tuple]["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=file_data.to_dict("records")[0]["email"],
                                msg=f"Subject: Happy Birthday!! \n\n {msg}"
                                )
