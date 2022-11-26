from helper.configuration_manager import ConfigurationManager
from playwright.sync_api import Playwright, Browser, BrowserType


class BrowserManager:
    @staticmethod
    def __get_browser_type(playwright: Playwright) -> BrowserType:
        browser = ConfigurationManager.browser()

        if browser == 'chromium':
            return playwright.chromium

        if browser == 'firefox':
            return playwright.firefox

        if browser == 'webkit':
            return playwright.webkit

    @staticmethod
    def initialize(playwright: Playwright) -> Browser:
        return BrowserManager.__get_browser_type(playwright).launch(headless=ConfigurationManager.headless(),
                                                                    slow_mo=ConfigurationManager.slow_motion())
