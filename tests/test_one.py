import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pages import main_page
from common import (launch_app, launch_browser, close_broswer)
from constant import (BASE_URL,DIVVY_BOARD)


from playwright.sync_api import sync_playwright


test_records = {}

with sync_playwright() as p:
    try:
        browser = launch_app(p)
        page = launch_browser(browser, DIVVY_BOARD)
        main_page_test = main_page.MainPage(page)
        main_page_test.verify_title()
        print(page.title())
        # add new test cases
        close_broswer(browser)
        test_records["test_one"] = "success"
    except Exception as e:
        print(e)
        test_records["test_one"] = "failed"

    