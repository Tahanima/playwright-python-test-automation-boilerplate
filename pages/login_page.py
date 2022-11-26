from helper.configuration_manager import ConfigurationManager
from pages.base_page import BasePage


class LoginPage(BasePage):
    def goto(self):
        self.page.goto(ConfigurationManager.base_url())

        return self

    def enter_username(self, username: str):
        self.page.fill('id=user-name', '')
        self.page.fill('id=user-name', username.strip())

        return self

    def enter_password(self, password: str):
        self.page.fill('id=password', '')
        self.page.fill('id=password', password.strip())

        return self

    def click_login(self):
        self.page.click('id=login-button')

    def fetch_error_message_locator(self):
        return self.page.locator('.error-message-container h3')
