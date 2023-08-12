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