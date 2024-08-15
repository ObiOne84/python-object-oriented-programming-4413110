import smtplib


SENDER_EMAIL = 'SOME_EMAIL@EMAIL.COM'
SENDER_PASSWORD = 'ASDFDSASDFADSF'


def send_email(receiver_email, subject, body):
  message = f'Subject: {subject}\n\n{body}'
  with smtplib.SMPT('smpt.office365.com', 587) as server:
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, receiver_email, message)

notes = """
Keep in mind though that some services may require you to configure your account's
security settings to send an email from Python. Figuring that out is part of the fun.
Pause the video now to create your own solution, then I'll show you how I solve this
challenge. (video game noises) For my solution, I used Python's smtplib module,
which provides an interface to connect to SMTP servers and send email messages.
I'll be sending my messages from an Outlook email account and after digging down
into the account settings menus, I found this page, which shows the server name,
port, and encryption method I'll need to use to send emails with SMTP. Now, looking
at my code, I import the smtplib module, and then create two string variables with
the email address and password for the account I'll be sending the message from.
Since the password is being stored in plain text here, I don't recommend using your
primary email address. Create a secondary account to send these notification emails.
My send email function starts by formatting the subject and message body inputs into
a single message string. This is the way to format the email to have a subject line
and a simple text message. Next on line eight, I use the SMTP function to open a
connection to the Office 365 SMTP server on port 587, and I open that with a context
manager to automatically handle closing the connection when it's done. Line nine calls
the starttls method to put the SMTP connection into transport layer security, or TLS mode,
and then line 10 uses the login method of the server object to log in with the sender's
email address and password credentials. Finally, at line 11, I use the sendmail method
to send the formatted message string from the sender email address to the receiver.
Now down in the terminal, I've already started an interactive Python shell and imported
my send email function. So I'll call it. Passing the email address to send the message
to. I'll make the subject line 'Notification', and the message 'Everything is awesome!'
And then press enter to run it. Now, logged into my email account, I can see that notification
that 'Everything is awesome!' My solution is just one way to solve this challenge. I encourage
"""