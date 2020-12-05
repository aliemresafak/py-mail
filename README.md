This is a project of mail client based smptlib and python version will >3.7


# pymail

Pymail is a Python library for mailing client.

## Installation

Use the clone [git](https://github.com/aliemresafak/py-mail.git) to your file system.

```bash
git clone https://github.com/aliemresafak/py-mail.git
```

## Usage

```python
import pymail

mail_settings = MailSettings(host="host_address", port=9999, sender="sender_mail", password="sender_password")
mail = Mail(settings=mail_settings)

mail.send_mail(to="reicever_mail_addresses", cc="cc_mail_addresses", subject="", message="Electronic mail message", files=[])
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.