from pages.base_page import BasePage


class ProductsPage(BasePage):
    def fetch_section_title_locator(self):
        return self.page.locator('.title')
