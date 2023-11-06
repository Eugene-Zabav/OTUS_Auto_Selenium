from pages.user_register_page import UserRegisterPage
from test_data.opencart_user import RandomUserData


def test_create_new_user(browser, url):
    userdata = RandomUserData()
    UserRegisterPage(browser) \
        .open(url) \
        .fill_register_new_user_form(
            userdata.random_string(),
            userdata.random_string(),
            userdata.random_email(),
            userdata.random_phone(),
            userdata.random_password(),
            userdata.password_confirm(),
        ) \
        .click_policy_confirm_checkbox() \
        .click_confirm_registry_button() \
        .title_is_success()
