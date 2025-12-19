from pages.login_page import LoginPage

def test_invalid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    login = LoginPage(driver)
    login.login("wronguser", "wrongpass")

    message = login.get_message()
    assert "Your username is invalid!" in message
