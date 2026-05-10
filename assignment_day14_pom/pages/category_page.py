from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CategoryPage:

    PRODUCTS = (By.CLASS_NAME, "hrefch")

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    def verify_laptop_list_presence(self):

        self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCTS
            )
        )

        products = self.driver.find_elements(
            *self.PRODUCTS
        )

        assert len(products) > 0

    def get_all_product_names(self):

        self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCTS
            )
        )

        fresh_products = self.driver.find_elements(
            *self.PRODUCTS
        )

        names = []

        for product in fresh_products:
            names.append(product.text)

        return names

    def select_product(self, product_name):

        self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCTS
            )
        )

        products = self.driver.find_elements(
            *self.PRODUCTS
        )

        for i in range(len(products)):

            fresh_products = self.driver.find_elements(
                *self.PRODUCTS
            )

            current_product = fresh_products[i]

            if current_product.text.strip() == product_name:

                current_product.click()

                break