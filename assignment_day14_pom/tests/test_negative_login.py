from pages.login_page import LoginPage

def test_invalid_login(driver):

    driver.get(
        "https://www.demoblaze.com/index.html"
    )

    login = LoginPage(driver)

    alert_text = login.login(
        "validUser",
        "wrongPassword"
    )

    assert alert_text == "Wrong password."