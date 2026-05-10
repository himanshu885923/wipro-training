import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class PurchaseModal(BasePage):

    NAME = (By.ID, "name")

    COUNTRY = (By.ID, "country")

    CITY = (By.ID, "city")

    CARD = (By.ID, "card")

    MONTH = (By.ID, "month")

    YEAR = (By.ID, "year")

    PURCHASE = (
        By.XPATH,
        "//button[text()='Purchase']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//h2[text()='Thank you for your purchase!']"
    )

    def fill_purchase_form(self, data):

        self.wait.until(
            EC.visibility_of_element_located(
                self.NAME
            )
        )

        with allure.step("Fill Name"):
            self.find(self.NAME).send_keys(
                data["name"]
            )

        with allure.step("Fill Country"):
            self.find(self.COUNTRY).send_keys(
                data["country"]
            )

        with allure.step("Fill City"):
            self.find(self.CITY).send_keys(
                data["city"]
            )

        with allure.step("Fill Card"):
            self.find(self.CARD).send_keys(
                data["card"]
            )

        with allure.step("Fill Month"):
            self.find(self.MONTH).send_keys(
                data["month"]
            )

        with allure.step("Fill Year"):
            self.find(self.YEAR).send_keys(
                data["year"]
            )

    def click_purchase(self):

        self.click(self.PURCHASE)

    def get_success_message(self):

        return self.get_text(
            self.SUCCESS_MESSAGE
        )