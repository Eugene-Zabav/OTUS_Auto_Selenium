from selenium.webdriver.common.by import By


class CatalogPage:
    BREADCRUMB = (By.XPATH, "//*[@class='breadcrumb']")
    PRODUCTS_GROUP = (By.XPATH, "//*[@class='list-group']")
    CATEGORY_DESCRIPTION = (By.XPATH, "(//*[contains(@class, 'row')])[3]")
    POSITIONS_SORTING_DROPDOWN = (By.XPATH, "//*[@id='input-sort']")
    POSITIONS_SHOW_LIMIT_DROPDOWN = (By.XPATH, "//*[@id='input-limit']")
    CURRENCY_DROP_DOWN = (By.XPATH, "//*[@class='btn btn-link dropdown-toggle']")
    CURRENCY_EUR = (By.XPATH, "//*[@name='EUR']")
    ITEM_PRICE = (By.XPATH, "//p[@class='price']")
