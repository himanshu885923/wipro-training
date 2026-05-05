from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()
driver.maximize_window()
wait = WebDriverWait(driver,20)

driver.get("https://www.amazon.in")

search_box = wait.until(
    EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
)
search_box.send_keys("Smart Watches")

search_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "nav-search-submit-button"))
)
search_btn.click()

wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='brandsRefinements']"))
)

brand_checkbox = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Apple']/preceding-sibling::div"))
)
brand_checkbox.click()

products = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
)
print("Total products on first page:", len(products))

driver.quit()
