import unittest

from pymail import MailSettings


class MailSettingsTestCase(unittest.TestCase):
    def test_checkip(self):
        self.assertTrue(MailSettings.check_ip("10.79.200.131"))
        self.assertFalse(MailSettings.check_ip("deneme.deneme"))
        self.assertTrue(MailSettings.check_ip("10.79.200.256"))
