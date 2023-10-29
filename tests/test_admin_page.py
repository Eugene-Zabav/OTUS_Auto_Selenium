from pages.admin_page import AdminPage
from test_data.admin_user import get_admin_user


def test_login(browser, url):
    AdminPage(browser) \
        .open(url) \
        .login(*get_admin_user()) \
        .title_is_dashboard()


def test_logout(browser, url):
    AdminPage(browser) \
        .open(url) \
        .login(*get_admin_user()) \
        .logout() \
        .title_is_administration()
