import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pages import main_page


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page() 
    page.goto("http://playwright.dev")
    main_page_test = main_page.MainPage(page)
    main_page_test.verify_title()
    print(page.title())
    browser.close()