Feature: Scenarios for the arabam.com

  Background:
    Given user is not logged in

  Scenario: Page title is correct
    When user is at "HomePage"
    Then user should see page title is "arabam.com: 2. El ve 0 Km Satılık Araç İlanları Platformu"

  Scenario: User is not logged in
    When user is at "HomePage"
    Then user should see "Login Menu Button"

  Scenario: Login button redirects correctly
    Given user is at "HomePage"
    When user clicks to the "Login Menu Button"
    Then user should see "Login Button"
    And user should see page title is "Üye Girişi"
    And user should see url is "LoginPage"

  Scenario: Login success
    Given user is at "LoginPage"
    When user tries to login with "valid" credentials
    Then user should see "Messages Button"
    And user should see "Favorites Button"
    And user should see "Notifications Button"
    And user should see url is "HomePage"

  Scenario: Login invalid email
    Given user is at "LoginPage"
    When user tries to login with "invalid email" credentials
    Then user should see text "Kullanıcı Bulunamadı"
    And "login email"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"


  Scenario: Login invalid password
    Given user is at "LoginPage"
    When user tries to login with "invalid password" credentials
    Then user should see text "Şifre eksik ya da hatalı"
    And "login password"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"


  Scenario: Login empty email
    Given user is at "LoginPage"
    When user tries to login with "empty email" credentials
    Then user should see text "E-posta ya da telefon numarası giriniz"
    And "login email"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"


  Scenario: Login empty password
    Given user is at "LoginPage"
    When user tries to login with "empty password" credentials
    Then user should see text "Şifre giriniz"
    And "login password"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"


  Scenario: Login empty email & empty password
    Given user is at "LoginPage"
    When user tries to login with "empty email & empty password" credentials
    Then user should see text "E-posta ya da telefon numarası giriniz"
    And user should see text "Şifre giriniz"
    And "login email"'s "class" attribute has "dirty invalid validated required"
    And "login password"'s "class" attribute has "dirty invalid validated required"
    And user should see url is "LoginPage"
    And user should see page title is "Üye Girişi"


  Scenario: Forgot password redirects correctly
    Given user is at "LoginPage"
    When user clicks to the "Forgot Password Button"
    Then user should see url is "ForgotPasswordPage"
    And user should see text " Şifremi Unuttum"
    And user should see page title is "Şifremi Unuttum"

  Scenario: Sign up button redirects correctly
    Given user is at "LoginPage"
    When user clicks to the "Login - SignUp Button"
    Then user should see url is "SignUpPage"
    And user should see "SignUp - SignUp Button"
    And user should see page title is "Üye Ol"


  #TODO login
  Scenario: Login - reCAPTCHA Google Confidentiality Agreement hyperlink redirects correctly
  Scenario: Login - reCAPTCHA Terms & Conditions hyperlink redirects correctly
  Scenario: Login - show password
  Scenario: Login - hide password
  Scenario: Login - remember me
  Scenario: Login - Facebook login success
  Scenario: Login - Google login success
  Scenario: Login - Account already linked to a facebook account
  Scenario: Login - Account already linked to a google account


  #TODO forgot password

  Scenario: Forgot password - valid phone number
  Scenario: Forgot password - invalid phone number
  Scenario: Forgot password - valid email
  Scenario: Forgot password - invalid email
  Scenario: Forgot password - switch to email
  Scenario: Forgot password - switch to phone number
  Scenario: Forgot password - email success
  Scenario: Forgot password - phone number success
  Scenario: Forgot password - back to login


  #TODO signup

  Scenario: SignUp - facebook register
  Scenario: SignUp - google register
  Scenario: SignUp - register success with phone number
  Scenario: SignUp - register success with email

  Scenario: SignUp - Name is required
  Scenario: SignUp - Surname is required
  Scenario: SignUp - Phone Number is required when phone number radiobutton is active
  Scenario: SignUp - Email is required when email radiobutton is active
  Scenario: SignUp - Password is required
  Scenario: SignUp - Personal data checkbox is required
  Scenario: SignUp - Confidentiality Agreement checkbox is required
  Scenario: SignUp - News checkbox is not required
  Scenario: SignUp - Phone Number input is not deleted when switched to Email
  Scenario: SignUp - Email input is not deleted when switched to Phone Number
  Scenario: SignUp - Show password
  Scenario: SignUp - Hide password
  Scenario: SignUp - Password is less than 6 chars
  Scenario: SignUp - Password does not include 1 alphabetical char
  Scenario: SignUp - Password does not include 1 numeric char
  Scenario: SignUp - Corporate membership button redirects correctly
  Scenario: SignUp - User Agreement hyperlink redirects correctly
  Scenario: SignUp - Confidentiality Agreement hyperlink redirects correctly
  Scenario: SignUp - reCAPTCHA Google Confidentiality Agreement hyperlink redirects correctly
  Scenario: SignUp - reCAPTCHA Terms & Conditions hyperlink redirects correctly


  #TODO Corporate membership

  Scenario: Corporate membership - register success
  Scenario: Corporate membership - Name is required
  Scenario: Corporate membership - Surname is required
  Scenario: Corporate membership - Phone Number is required
  Scenario: Corporate membership - Company Name is required
  Scenario: Corporate membership - City is required
  Scenario: Corporate membership - District is required
  Scenario: Corporate membership - Open address is not required
  Scenario: Corporate membership - Tax Administration is shown when Company Type is chosen as "Anonymous or Limited"
  Scenario: Corporate membership - Tax No is shown when Company Type is chosen as "Anonymous or Limited"
  Scenario: Corporate membership - ID Number is not shown when Company Type is chosen as "Anonymous or Limited"
  Scenario: Corporate membership - ID Number is shown when Company Type is chosen as "Sole Proprietorship "
  Scenario: Corporate membership - Tax Administration is not shown when Company Type is chosen as "Sole Proprietorship"
  Scenario: Corporate membership - Tax No is not shown when Company Type is chosen as "Sole Proprietorship"
  Scenario: Corporate membership - Personal data checkbox is required
  Scenario: Corporate membership - Confidentiality Agreement checkbox is required
  Scenario: Corporate membership - Login button redirects correctly
  Scenario: Corporate membership - User Agreement hyperlink redirects correctly
  Scenario: Corporate membership - Confidentiality Agreement hyperlink redirects correctly
  Scenario: Corporate membership - reCAPTCHA Google Confidentiality Agreement hyperlink redirects correctly
  Scenario: Corporate membership - reCAPTCHA Terms & Conditions hyperlink redirects correctly








