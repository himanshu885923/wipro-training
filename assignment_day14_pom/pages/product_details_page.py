import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

logging.basicConfig(level=logging.INFO)


class ProductDetailsPage(BasePage):

    ADD_TO_CART = (
        By.LINK_TEXT,
        "Add to cart"
    )

    def add_product_to_cart(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART
            )
        )

        self.click(self.ADD_TO_CART)

        alert = self.wait.until(
            EC.alert_is_present()
        )

        logging.info(
            "Product added to cart"
        )

        alert.accept()