import allure
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

load_dotenv()

@allure.feature("Authentication")
@allure.story("Login")
class TestLogin:

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Successful Login with Valid Credentials")
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        
        email = os.getenv("TEST_USER_EMAIL")
        password = os.getenv("TEST_USER_PASSWORD")
        
        login_page.login(email, password)

        try:
            WebDriverWait(driver, 10).until(
                lambda d: d.current_url == "http://localhost:5003/" 
            )
        except TimeoutException:
            print(f"[DEBUG] ⏳ Timed out! Still on: {driver.current_url}")

            try:
                btn = driver.find_element(By.CSS_SELECTOR, "[data-testid='button-login']")
                print(f"[DEBUG] Button Text is currently: '{btn.text}'")
            except NoSuchElementException:
                pass
                
        assert driver.current_url == "http://localhost:5003/", \
            f"Login failed. Current URL: {driver.current_url}"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Fail Login with Invalid Email Format")
    def test_invalid_email_format(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("not-an-email", "123456")
        
        validation_msg = login_page.get_email_input_validation_message()
        assert validation_msg != "", "Expected a browser validation message, but got none."