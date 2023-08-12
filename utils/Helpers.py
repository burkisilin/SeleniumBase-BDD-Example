from config.Config import TestData
class Helpers:
    def __init__(self):
        self.config = TestData()

    def return_page_url(self, page):
        page = page.lower().replace(" ", "")
        if page == "homepage":
            return self.config.PROD_ENV_BASE_URL
        elif page == "loginpage":
            return self.config.PROD_ENV_BASE_URL + "uyelik?returnUrl=/"
        elif page == "forgotpasswordpage":
            return self.config.PROD_ENV_BASE_URL + "sifremi-unuttum?returnUrl=/"
        elif page == "signuppage":
            return self.config.PROD_ENV_BASE_URL + "uye-ol"
        else:
            raise Exception("Unexpected page!")


    def return_selector(self, element_locator):
        return self.config.LOCATORS[element_locator.lower()]


