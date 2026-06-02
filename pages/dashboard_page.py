from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):

    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    PROFILE_DROPDOWN = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Logout']")

    def __init__(self,driver):
        super().__init__(driver)

    def is_dashboard_page_loaded(self):
        element = self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_HEADER))

        return element.is_displayed()

    def logout(self):
        self.click_element(self.PROFILE_DROPDOWN)
        self.click_element(self.LOGOUT_BUTTON)