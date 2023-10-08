def test_page_title(browser, url):
    browser.maximize_window()
    browser.get(url)
    assert browser.title == "Your Store"
