import smtplib
from dataclasses import dataclass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@dataclass
class MailSettings:
    host: str
    sender: str
    password: str
    port: int

    def check_ip(self):
        arr_host = []
        try:
            arr_host = [int(i) for i in self.host.split(".")]
        except Exception:
            return False

        if len(arr_host) < 3:
            return False

        for i in arr_host:
            if not isinstance(i, int):
                return False
        for i in arr_host:
            if i >= 1 and i <= 255:
                continue
            else:
                return False
        return True


class Mail:
    def __init__(self, settings: MailSettings):
        self.settings = settings

    def make_zip(self):
        pass

    def send_mail(self, to, cc=None, subject=None, message=None, files=[]):
        if isinstance(to, list):
            to = ", ".join(to)

        if isinstance(cc, list):
            cc = ", ".join(cc)

        if len(files) > 0:
            mail = MIMEMultipart("alternative")
            self.make_zip()
        else:
            mail = MIMEText(message)

        mail["From"] = self.settings.sender
        mail["to"] = to
        mail["cc"] = cc
        mail["subject"] = subject

        session = smtplib.SMTP(host=self.settings.host, port=self.settings.port)
        session.starttls()
        session.login(user=self.settings.sender, password=self.settings.password)
        text = mail.as_string()
        session.sendmail(from_addr=self.settings.sender, to_addrs=[to], msg=text)
        session.close()
