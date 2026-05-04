"""
code for working google homepage
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = input('what browser do you want to use ?')

match (browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service=Service('../resources/chromedriver.exe'))
    case 'edge':
        driver = webdriver.Edge(service = Service('../resources/msedgedriver.exe'))
    case _ :
        print("browser not available \n Executing with the default edge browser")
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))




driver.get("https://www.google.com")

pagetitle = driver.title

if pagetitle == 'Google':
    print("Google Homepage NOT loaded - Pass ")
else:
    print("Google Homepage NOT loaded - Fail")

driver.quit()

