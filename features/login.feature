Feature: Scenarios for the arabam.com login page

  Background:
    Given user is not logged in
    Given user is at "LoginPage"

  Scenario: Login - Success
    When user tries to login with "valid" credentials
    Then user should see "Messages Button"
    And user should see "Favorites Button"
    And user should see "Notifications Button"
    And user should see url is "HomePage"

  Scenario: Login - invalid email
    When user tries to login with "invalid email" credentials
    Then user should see text "Kullanıcı Bulunamadı"
    And "login email"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"

  Scenario: Login - invalid password
    When user tries to login with "invalid password" credentials
    Then user should see text "Şifre eksik ya da hatalı"
    And "login password"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"

  Scenario: Login - empty email
    When user tries to login with "empty email" credentials
    Then user should see text "E-posta ya da telefon numarası giriniz"
    And "login email"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"

  Scenario: Login - empty password
    When user tries to login with "empty password" credentials
    Then user should see text "Şifre giriniz"
    And "login password"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"

  Scenario: Login - empty email & empty password
    When user tries to login with "empty email & empty password" credentials
    Then user should see text "E-posta ya da telefon numarası giriniz"
    And user should see text "Şifre giriniz"
    And "login email"'s "class" attribute has "dirty invalid validated required"
    And "login password"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"

  Scenario: Login - Forgot password redirects correctly
    When user clicks to the "Forgot Password Button"
    Then user should see url is "ForgotPasswordPage"
    And user should see text " Şifremi Unuttum"
    And user should see page title is "Şifremi Unuttum"

  Scenario: Login - Sign up button redirects correctly
    When user clicks to the "Login - SignUp Button"
    Then user should see url is "SignUpPage"
    And user should see "SignUp - SignUp Button"
    And user should see page title is "Üye Ol"

  Scenario: Login - reCAPTCHA Google Confidentiality Agreement hyperlink redirects correctly
    When user clicks to the "Google Confidentiality Agreement Link"
    Then user should see url is "https://policies.google.com/privacy?hl=tr"
    And user should see page title is "Gizlilik Politikası – Gizlilik ve Şartlar – Google"

  Scenario: Login - reCAPTCHA Terms & Conditions hyperlink redirects correctly
    When user clicks to the "Google Terms & Conditions Link"
    Then user should see url is "https://policies.google.com/terms?hl=tr"
    And user should see page title is "Google Hizmet Şartları – Gizlilik ve Şartlar – Google"

  Scenario: Login - show password
    Given "Login Password" is entered as "123456."
    Given password is "hidden"
    When user clicks to the "Hide / Show Password Icon"
    Then "Login Password"'s "type" attribute has "text"

  Scenario: Login - hide password
    Given "Login Password" is entered as "123456."
    Given password is "shown"
    When user clicks to the "Hide / Show Password Icon"
    Then "Login Password"'s "type" attribute has "password"



















