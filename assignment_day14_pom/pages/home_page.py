from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.category_page import CategoryPage


class HomePage(BasePage):

    LAPTOPS = (By.LINK_TEXT, "Laptops")
    PHONES = (By.LINK_TEXT, "Phones")

    def open(self):

        self.driver.get(
            "https://www.demoblaze.com/index.html"
        )

    def click_laptops(self):

        self.click(self.LAPTOPS)

        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".card")
            )
        )

        return CategoryPage(self.driver)

    def click_phones(self):

        self.click(self.PHONES)

        self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".card")
            )
        )

        return CategoryPage(self.driver)