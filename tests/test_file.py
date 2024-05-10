
def test_page_title(browser):
    browser.get("http://192.168.1.109:8081/")
    assert browser.title == "Your Store"
