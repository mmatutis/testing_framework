"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    # Locators
    _login_link = 'Login'
    _email_field = 'user_email'
    _pass_field = 'user_password'
    _login_button = 'commit'
    _gravatar = 'gravatar'

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def loginBase(self, email, password):
        self.navigateTo(self._baseURL)
        self.elementClick(self._login_link, locatorType='link')
        self.sendKeys(email, self._email_field)
        self.sendKeys(password, self._pass_field)
        self.elementClick(self._login_button, locatorType='name')
        result = self.isElementPresent(self._gravatar, locatorType='class')
        assert result == True