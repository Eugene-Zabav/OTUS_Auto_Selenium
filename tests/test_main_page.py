from pages.main_page import MainPage


def test_change_currency(browser, url):
    MainPage(browser).open(url)
    default_usd_currency = MainPage(browser).currency_price().text
    MainPage(browser).change_currency()
    changed_eur_currency = MainPage(browser).currency_price().text
    assert default_usd_currency != changed_eur_currency


def test_add_item_to_cart(browser, url):
    # browser.get(url)
    MainPage(browser) \
        .open(url) \
        .add_to_cart()

    assert MainPage(browser).element(MainPage.CART).text.startswith("1 item(s) - ")

    featured_item_name = MainPage(browser).featured_item_name()

    MainPage(browser).click_cart_button()

    item_in_cart_name = MainPage(browser).item_in_cart_name()
    items_in_cart = MainPage(browser).item_in_cart()

    assert featured_item_name.text == item_in_cart_name.text
    assert items_in_cart.text == "x 1"
