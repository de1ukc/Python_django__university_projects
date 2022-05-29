import smtplib


def send(subject, msh):
    gmail_user = 'col.jabka@gmail.com'
    gmail_password = 'jculrbcakeajhgjn'
    sent_from = gmail_user
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    message = 'Subject: {}\n\n{}'.format(subject, msh)
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, 'trapper.md@mail.ru', message)
    server.quit()
    return

print('ho')
send('Test', 'Hello')
print('hi')