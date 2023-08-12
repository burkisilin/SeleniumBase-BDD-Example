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
    LOCATORS = {
        "search input": "input.input[placeholder='Kelime, galeri adı veya ilan no ile ara']",
        "login menu button": "a[aria-label='Giriş Yap']",
        "login button": "button.btn-form-submit",
        "signup - signup button": "button.btn-form-submit",
        "login email": "#emailOrPhone",
        "login password": "#password",
        "forgot password button": "a[href='/sifremi-unuttum?returnUrl=/']",
        "login - signup button": "a[href='/uye-ol']",
        "messages button": "//div[@class='messages-wrapper']",
        "favorites button": "//div[@class='favorites-wrapper']",
        "notifications button": "//div[@class='notifications-wrapper']"
    }


