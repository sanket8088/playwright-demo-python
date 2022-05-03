from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    #Web Elements
    header: str = 'h1'
    more_info_link: str = 'text=More information'

    def verify_title(self):
        print("---------")
        assert self.page.title() == 'Fast and reliable end-to-end testing for modern web apps | Playwright'
        print("Success")

    def select_more_information_link(self):
        with self.page.expect_navigation():
            self.page.click(self.more_info_link)