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


def test_add_new_product(browser, url):
    AdminPage(browser) \
        .open(url) \
        .login(*get_admin_user()) \
        .create_default_product() \
        .show_success_alert()


def test_delete_product(browser, url):
    AdminPage(browser) \
        .open(url) \
        .login(*get_admin_user()) \
        .delete_default_product() \
        .accept_browser_alert()
    AdminPage(browser).show_success_alert()
