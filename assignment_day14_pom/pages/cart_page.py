from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.purchase_modal import PurchaseModal


class CartPage(BasePage):

    CART = (By.ID, "cartur")

    PLACE_ORDER = (
        By.XPATH,
        "//button[text()='Place Order']"
    )

    def open_cart(self):

        self.driver.get(
            "https://www.demoblaze.com/index.html"
        )

        self.click(self.CART)

    def click_place_order(self):

        self.click(self.PLACE_ORDER)

        return PurchaseModal(self.driver)