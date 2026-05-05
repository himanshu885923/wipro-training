from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,15)

driver.get("https://www.amazon.in")

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Dell i5 laptop")
driver.find_element(By.ID, "nav-search-submit-button").click()

first_product = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]"))
)

first_product.click()
driver.quit()