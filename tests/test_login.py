import pytest
import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import Config


@allure.feature("Login Module")
class TestLogin:

    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify user can login with valid credentials")
    @allure.description(
        "Verify that a registered user can successfully login "
        "using valid username and password."
    )
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login(self, driver):

        login_page = LoginPage(driver)

        with allure.step("Login using valid credentials"):
            login_page.login(
                Config.USERNAME,
                Config.PASSWORD
            )

        dashboard_page = DashboardPage(driver)

        with allure.step("Verify Dashboard page is displayed"):
            assert dashboard_page.is_dashboard_page_loaded()

    @allure.story("Invalid Login")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify error message for invalid login")
    @allure.description(
        "Verify that the application displays the correct error "
        "message when invalid credentials are used."
    )
    @pytest.mark.regression
    def test_invalid_login(self, driver):

        login_page = LoginPage(driver)

        with allure.step("Login using invalid credentials"):
            login_page.login(
                "wrong_user",
                "wrong_password"
            )

        with allure.step("Verify invalid credential error message"):
            assert login_page.get_error_message() == "Invalid credentials"

    @allure.story("Logout")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify user can logout successfully")
    @allure.description(
        "Verify that a logged-in user can successfully logout "
        "and is redirected to the login page."
    )
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self, driver):

        login_page = LoginPage(driver)

        with allure.step("Login using valid credentials"):
            login_page.login(
                Config.USERNAME,
                Config.PASSWORD
            )

        dashboard_page = DashboardPage(driver)

        with allure.step("Verify Dashboard page is displayed"):
            assert dashboard_page.is_dashboard_page_loaded()

        with allure.step("Logout from the application"):
            dashboard_page.logout()

        with allure.step("Verify user is redirected to Login page"):
            assert "login" in login_page.get_current_url().lower()