from pages.login_page import LoginPage

def test_valid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    login = LoginPage(driver)
    login.login("tomsmith", "SuperSecretPassword!")

    assert "Secure Area" in driver.page_source
