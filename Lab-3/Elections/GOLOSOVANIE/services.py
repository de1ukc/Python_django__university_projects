import smtplib
import threading
from . import config as config


def path_to_directory(instance, filename):
    return 'photos/Elections/{0}/{1}/{2}'.format(instance.last_name, instance.first_name, filename)


def user_path_to_directory(instance, filename):
    return 'photos/users/{0}/{1}'.format(instance.nick_name, filename)


class MyThread(threading.Thread):
    def __init__(self, send_to, subject, msg):
        threading.Thread.__init__(self)
        self.send_to = send_to
        self.subject = subject
        self.msg = msg

    def run(self) -> None:
        send_mail(self.send_to, self.subject, self.msg)


def send_mail(send_to, subject, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(config.USER_EMAIL, config.USER_PASSWORD)

    message = 'Subject: {}\n\n{}'.format(subject, msg)

    server.sendmail(config.USER_EMAIL, send_to, message)
    server.quit()
    return

