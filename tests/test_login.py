import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config.config import Config


class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login(self, driver):
        login_page = LoginPage(driver)

        login_page.login(
            Config.USERNAME,
            Config.PASSWORD
        )

        dashboard_page = DashboardPage(driver)

        assert dashboard_page.is_dashboard_page_loaded()

    @pytest.mark.regression
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)

        login_page.login(
            "wrong_user",
            "wrong_password"
        )

        assert login_page.get_error_message() == "Invalid credentials"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout(self, driver):
        login_page = LoginPage(driver)

        login_page.login(
            Config.USERNAME,
            Config.PASSWORD
        )

        dashboard_page = DashboardPage(driver)

        assert dashboard_page.is_dashboard_page_loaded()

        dashboard_page.logout()

        assert "login" in login_page.get_current_url().lower()
