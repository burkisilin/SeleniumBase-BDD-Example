Feature: Scenarios for the arabam.com homepage

  Background:
    Given user is not logged in
    Given user is at "HomePage"

  Scenario: Page title is correct
    Then user should see page title is "arabam.com: 2. El ve 0 Km Satılık Araç İlanları Platformu"

  Scenario: User is not logged in
    Then user should see "Login Menu Button"

  Scenario: Login button redirects correctly
    When user clicks to the "Login Menu Button"
    Then user should see "Login Button"
    And user should see page title is "Üye Girişi"
    And user should see url is "LoginPage"

  Scenario: User is logged in
    Given user clicks to the "Login Menu Button"
    When user tries to login with "valid" credentials
    Then user should see "User Menu"
    And user should see "Messages Button"
    And user should see "Favorites Button"
    And user should see "Notifications Button"


  Scenario: Search is shown
    Then user should see "Search Input"

  Scenario: Adversite button is shown
    Then user should see "Create Adversite Button"

  Scenario: Showcase items are shown
    Then user should see "Showcase Table"

  Scenario: Top Navigation menu is shown
    Then user should see "Top Nav Menu"

  Scenario: Top Navigation menu main titles are correct
    Then user should see "Top Nav Menu" contains "7" items
    And user should see "Top Nav Menu" contains "Trink sat!" text
    And user should see "Top Nav Menu" contains "Araç Al" text
    And user should see "Top Nav Menu" contains "Araç Sat" text
    And user should see "Top Nav Menu" contains "Hizmetlerimiz" text
    And user should see "Top Nav Menu" contains "arabam Blog" text
    And user should see "Top Nav Menu" contains "Kurumsal" text
    And user should see "Top Nav Menu" contains "Garaj" text


  Scenario: Categories items main titles are correct
    Then user should see "Categories Menu" contains "16" items
    And user should see "Categories Menu" contains "Tüm İlanlar" text
    And user should see "Categories Menu" contains "Otomobil" text
    And user should see "Categories Menu" contains "Arazi, SUV, Pick-up" text
    And user should see "Categories Menu" contains "Motosiklet" text
    And user should see "Categories Menu" contains "Minivan & Panelvan" text
    And user should see "Categories Menu" contains "Ticari Araçlar" text
    And user should see "Categories Menu" contains "Kiralık Araçlar" text
    And user should see "Categories Menu" contains "Hasarlı Araçlar" text
    And user should see "Categories Menu" contains "Traktör" text
    And user should see "Categories Menu" contains "Tarım & İş Makineleri" text
    And user should see "Categories Menu" contains "Klasik Araçlar" text
    And user should see "Categories Menu" contains "Elektrikli Araçlar" text
    And user should see "Categories Menu" contains "ATV & UTV" text
    And user should see "Categories Menu" contains "Karavan" text
    And user should see "Categories Menu" contains "Engelli Araçları" text
    And user should see "Categories Menu" contains "Modifiyeli Araçlar" text




  Scenario: See "All Showcase items" button redirects correctly
  Scenario: recommended for you section is shown
  Scenario: testimonials section is shown
  Scenario: test drives section is shown
  Scenario: test drives - all drives button redirects correctly
  Scenario: news section is shown - all news button redirects correctly
  Scenario: middle footer is shown
  Scenario: bottom footer is shown
  Scenario: Facebook social link redirects correctly
  Scenario: Twitter social link redirects correctly
  Scenario: Youtube social link redirects correctly
  Scenario: Instagram social link redirects correctly
  Scenario: Google Play download link redirects correctly
  Scenario: App Store download link redirects correctly
  Scenario: App Galery download link redirects correctly

