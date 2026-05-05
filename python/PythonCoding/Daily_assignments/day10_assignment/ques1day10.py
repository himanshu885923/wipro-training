from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.maximize_window()
wait = WebDriverWait(driver,15)

driver.get("https://www.amazon.in")


print("Title:", driver.title)
assert "Amazon" in driver.title

mobiles = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Mobiles")))
mobiles.click()

driver.back()
driver.quit()