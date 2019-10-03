import yagmail

sender_email = '0583254409a@gmail.com'
receiver_email = 'shayeulman@gmail.com'
subject = "Sent from the terminal!!!"
sender_password = raw_input('Please, enter the password:')

yag = yagmail.SMTP(user=sender_email, password=sender_password)

contents = [
  "This E-Mail is sent from  the terminal!",
  "using a Python library",
  "called Yagmail, It's so easy, just a few lines of code!!!",
]

yag.send(receiver_email, subject, contents)