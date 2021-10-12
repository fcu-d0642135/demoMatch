import unittest
from main import login


class TestIdentify(unittest.TestCase):

    def test_login_success(self):
        self.assertTrue(login('company', 'company'))

    def test_login_fail(self):
        self.assertFalse(login('Company', 'Company'))

    def test_login_fail2(self):
        self.assertFalse(login('Company2', 'Company2'))


if __name__ == '__main__':
    unittest.main()
