from base.selenium_driver import SeleniumDriver
from pages.home.navigation_page import NavigationPage
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time

class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = 'Login'
    _logout_link = "//div[@id='navbar']//li[@class='dropdown open']//a[@href='/sign_out']"
    _email_field = 'user_email'
    _pass_field = 'user_password'
    _login_button = 'commit'
    _gravatar = 'gravatar'
    _login_fail_alert = '//div[contains(text(), "Invalid email or password")]'

    # Actions

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType='link')

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._pass_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='name')

    # Scenarios

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._gravatar, locatorType='class')
        return result

    def verifyLoginFail(self):
        result = self.isElementPresent(self._login_fail_alert, locatorType='xpath')
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        self.nav.navigateToUserSettings()
        time.sleep(0.3)
        logoutLinkElement = self.waitForElement(locator=self._logout_link,
                          locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
        # self.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']",
        #                   locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._pass_field)
        passwordField.clear()