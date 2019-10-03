# -*- coding: utf-8 -*-
import yagmail

sender_email = '0583254409a@gmail.com'
receiver_email = 'c0533175399@gmail.com'
subject = "נשלח עם פייתון!!"
sender_password = raw_input(' נא הכנס את הסיסמא של' + sender_email)

yag = yagmail.SMTP(user=sender_email, password=sender_password)

contents = [
  "...האימייל הזה נשלח אליך עם פייתון",
  "ראה את הקוד כאן:",
  "https://github.com/shayaulman/simple-python-scripts/commit/f86dd0539c89b1d48d89c45edcfe97640973c3b2",
  "כדי שזה יעבוד יש  צורך להתקין ספריות מסיומות, ככה שזה לא יעבוד לך מיד..."
]

yag.send(receiver_email, subject, contents)