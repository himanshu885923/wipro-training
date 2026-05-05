from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
wait = WebDriverWait(driver,15)

driver.get("https://www.amazon.in")

search_box = wait.until(
    EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
)

search_box.send_keys("Wireless Headphones")

search_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
)
search_btn.click()


result_text = wait.until(
     EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'results')]"))
).text
print(result_text)

assert "results" in result_text.lower()

driver.quit()