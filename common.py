def launch_app(p):
    browser = p.chromium.launch(headless = False)
    return browser

def launch_browser(browser, url):
    page = browser.new_page() 
    page.goto(url)
    return page


def close_broswer(browser):
    browser.close()
    return