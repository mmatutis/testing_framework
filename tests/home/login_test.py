from pages.home.login_page import LoginPage
from utilities.executestatus import ExecuteStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = ExecuteStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login('test@email.com', 'abcabc')
        self.ts.mark(self.lp.verifyLoginTitle() == True, "Title is incorect")
        self.ts.markFinal("test_valid_login", self.lp.verifyLoginSuccessful(), "Login was not successful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.logout()
        self.lp.login('test@email.com', 'aaaabcabc')
        self.ts.markFinal('test_invalid_login', self.lp.verifyLoginFail(), "Invalid login test Failed")
