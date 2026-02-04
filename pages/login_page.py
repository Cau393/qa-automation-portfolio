from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='input-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-testid='input-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-testid='button-login']")
    REMEMBER_ME = (By.CSS_SELECTOR, "[data-testid='checkbox-remember']")
    REGISTER_LINK = (By.CSS_SELECTOR, "[data-testid='link-register']")
    
    # Error Messages
    EMAIL_ERROR = (By.CSS_SELECTOR, "[data-testid='text-email-error']")
    PASSWORD_ERROR = (By.CSS_SELECTOR, "[data-testid='text-password-error']")
    
    # Toast/Alert
    TOAST_TITLE = (By.CSS_SELECTOR, ".toast-title")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://localhost:5003/login"

    @allure.step("Navigate to Login Page")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Login with email: {email}")
    def login(self, email, password):
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

        login_button = self.find(self.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", login_button)

    def get_email_error(self):
        return self.get_text(self.EMAIL_ERROR)
    
    def get_password_error(self):
        return self.get_text(self.PASSWORD_ERROR)
    
    def get_toast_title(self):
        return self.get_text(self.TOAST_TITLE)
    
    def get_email_input_validation_message(self):
        """
        Retrieves the native HTML5 validation message (e.g., 'Please include an @...')
        """
        email_element = self.find(self.EMAIL_INPUT)
        return self.driver.execute_script("return arguments[0].validationMessage;", email_element)