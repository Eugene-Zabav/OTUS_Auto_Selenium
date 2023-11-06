from pages.catalog_page import CatalogPage


def test_change_currency(browser, url):
    CatalogPage(browser).open(url)
    default_usd_currency = CatalogPage(browser).currency_price().text
    CatalogPage(browser).change_currency()
    changed_eur_currency = CatalogPage(browser).currency_price().text
    assert default_usd_currency != changed_eur_currency
