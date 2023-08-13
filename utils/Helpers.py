from config.Config import TestData
from datetime import datetime


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

    def return_int_from_string(self, string):
        return int(''.join(filter(str.isdigit, string.replace(".", ""))))

    def reformat_turkish_date(self, date):
        date = date.lower()
        if "ocak" in date:
            date = date.replace("ocak", ".01.")
        elif "şubat" in date:
            date = date.replace("şubat", ".02.")
        elif "mart" in date:
            date = date.replace("mart", ".03.")
        elif "nisan" in date:
            date = date.replace("nisan", ".04.")
        elif "mayıs" in date:
            date = date.replace("mayıs", ".05.")
        elif "haziran" in date:
            date = date.replace("haziran", ".06.")
        elif "temmuz" in date:
            date = date.replace("temmuz", ".07.")
        elif "ağustos" in date:
            date = date.replace("ağustos", ".08.")
        elif "eylül" in date:
            date = date.replace("eylül", ".09.")
        elif "ekim" in date:
            date = date.replace("ekim", ".10.")
        elif "kasım" in date:
            date = date.replace("kasım", ".11.")
        elif "aralık" in date:
            date = date.replace("aralık", ".12.")
        return date

    def items_are_ordered(self, items_list, items_type, order_type):
        if items_type == "date":
            sorted_timestamps = sorted(items_list, key=lambda x: datetime.strptime(x, "%d.%m.%Y").strftime("%Y.%m.%d"))
            if order_type == "ascending":
                sorted_timestamps = sorted_timestamps[::-1]  # reverse the sorted list to match the order type
            if sorted_timestamps == items_list:
                return True
            else:
                return False
        elif items_type == "numeric":
            if order_type == "ascending":
                return all(items_list[i] <= items_list[i + 1] for i in range(len(items_list) - 1))
            elif order_type == "descending":
                return all(items_list[i] >= items_list[i + 1] for i in range(len(items_list) - 1))
            elif order_type == "not ordered":
                return not all(items_list[i] <= items_list[i + 1] for i in range(len(items_list) - 1))
            else:
                raise Exception("Invalid order provided at cucumber file!")
        else:
            raise Exception("Unexpected item type!")

    def convert_rgb_to_hex(self, rgb_color):
        color_tuple = eval(rgb_color.replace("rgb",""))
        hex_color = '#' + ''.join(f'{i:02X}' for i in color_tuple)
        return hex_color.lower()

