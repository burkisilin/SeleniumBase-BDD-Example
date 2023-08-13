class TestData:
    PROD_ENV_BASE_URL = "https://www.arabam.com/"
    TEST_ENV_BASE_URL = "https://www.test.arabam.com/"

    LOGIN_CREDENTIALS = {
        "valid":
            {
                "email": "burakotomasyon@gmail.com",
                "password": "Burak1234."
            },
        "invalid email":
            {
                "email": "invalidemail@gminv.com",
                "password": "Burak1234."
            },
        "invalid password":
            {
                "email": "burakotomasyon@gmail.com",
                "password": "inv@lid123!."
            },
        "empty email":
            {
                "email": "",
                "password": "Burak1234."
            },
        "empty password":
            {
                "email": "burakotomasyon@gmail.com",
                "password": ""
            },
        "empty email & empty password":
            {
                "email": "",
                "password": ""
            }
    }

    # Locators must be lower case letters
    LOCATORS = {
        "search input": "input.input[placeholder='Kelime, galeri adı veya ilan no ile ara']",
        "search button": "button.search-button",
        "create adversite button": "button.btn-create-advert",
        "login menu button": "a[aria-label='Giriş Yap']",
        "login button": "button.btn-form-submit",
        "signup - signup button": "button.btn-form-submit",
        "login email": "#emailOrPhone",
        "login password": "#password",
        "forgot password button": "a[href='/sifremi-unuttum?returnUrl=/']",
        "login - signup button": "a[href='/uye-ol']",
        "messages button": "//div[@class='messages-wrapper']",
        "favorites button": "//div[@class='favorites-wrapper']",
        "notifications button": "//div[@class='notifications-wrapper']",
        "user menu": "div.user-menu-wrapper",
        "google confidentiality agreement link": "//a[text()='Google Gizlilik Politikası']",
        "google terms & conditions link": "//a[text()='Kullanım Koşulları']",
        "hide / show password icon": "//button[contains(@class,'btn-togglePassword')]",
        "showcase table": "div.showcase.row",
        "top nav menu": "ul.navigation-list",
        "categories menu": "ul.category-section",
        "all showcase button": "a.all-showcase.fr",
        "active search filters": "div.selected-filters",
        "recommended for you section": "#collect-suggestion-wrapper",
        "testimonials section": "#testimonials",
        "test drives section": "div.test-wrapper",
        "all drives button": "div.all-tests-btn",
        "news section": "div.news-wrapper",
        "all news button": "div.all-news-btn",
        "middle footer": "section.footer-middle",
        "bottom footer": "div.footer-bottom",
        "facebook social button": "//a[contains(@href,'facebook')]",
        "twitter social button": "//a[contains(@href,'twitter')]",
        "youtube social button": "//a[contains(@href,'youtube')]",
        "instagram social button": "//a[contains(@href,'instagram')]",
        "google play app button": "//a[contains(@href,'play.google')]",
        "app store app button": "//a[contains(@href,'itunes.apple')]",
        "app gallery app button": "//a[contains(@href,'appgallery7.huawei')]",
        "accept cookie button": "button.cookie-policy-banner-button",

        "search result amount": "//span[contains(@id,'advert-count')]",
        "search result items": "//tr[contains(@class,'listing-list-item')]",
        "search result categories": "//div[@class='category-facet']//ul[@class='inner-list']",
        "search selected category": "li.selected-list-item > a",
        "search page search button": "//button[text()='Ara']",
        "search page clear filters button": "button.clear-all",
        "search page order dropdown": "select.listing-order-dropdown-select",
        "search result prices": "//span[contains(@class,'listing-price')]",
        "search result years": "//tr[contains(@class,'listing-list-item')]/td[4]",
        "search result dates": "//tr[contains(@class,'listing-list-item')]/td[6]",
        "search result add / remove fav": "//span[contains(@onclick,'Favorite')]",
        "favorite list": "div.list-name",
        "hide item": "//span[contains(@onclick,'toggleHide')]",
        "show item": "//span[@class='toolbox-item']",
        "item titles": "//div[contains(@class,'listing-title')]",
        "item detail title": "p.advert-detail-title",
    }


