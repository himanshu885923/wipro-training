from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
wait = WebDriverWait(driver,15)

driver.get("https://www.amazon.in")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

about = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='about']"))
)
about.click()

heading = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME,"h1"))
).text

print("Heading", heading)
driver.quit()
