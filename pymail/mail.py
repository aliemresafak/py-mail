import re
import smtplib
import typing
from dataclasses import dataclass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@dataclass
class MailSettings:
    ip_regex = re.compile(
        "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    )
    host: str
    port: int
    sender: str
    password: str
    

    def __post_init__(self):
        if not self.check_ip(self.host):
            raise Exception("Check entered ip")

    @classmethod
    def check_ip(cls, host: str) -> bool:
        return cls.ip_regex.match(host)


class Mail:
    def __init__(self, settings: MailSettings):
        self.settings = settings

    # TODO make_zip arguman alirsa daha iyi olur
    def make_zip(self, files):
        pass

    def _list_to_string(self, value: typing.Union[str, list]) -> str:
        if isinstance(value, list):
            value = ", ".join(value)
        return value

    def send_mail(self, to: typing.Union[str, list], cc: typing.Union[str, list]=None, subject=None, message=None, files=[]):
        to = self._list_to_string(to)
        cc = self._list_to_string(cc)

        if len(files) > 0:
            mail = MIMEMultipart("alternative")
            self.make_zip(files)
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
        session.sendmail(from_addr=self.settings.sender, to_addrs=to, msg=text)
        session.close()
