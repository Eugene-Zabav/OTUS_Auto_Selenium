from pages.user_register_page import UserRegisterPage
from test_data.opencart_user import NewUserData


def test_user_register_page_elements(browser, url):
    userdata = NewUserData()
    UserRegisterPage(browser) \
        .open(url) \
        .register_new_user(
            userdata.random_string(),
            userdata.random_string(),
            userdata.random_email(),
            userdata.random_phone(),
            userdata.random_password(),
            userdata.password,
        ) \
        .title_is_success()
