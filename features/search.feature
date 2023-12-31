Feature: Scenarios for the arabam.com search page

  Background:
    Given user is not logged in
    Given user is at "HomePage"
    Given user is accepted cookie popup

  Scenario: Search results are shown
    When user searches "bmw" item
    Then user should see results are "shown"
    And user should see filter "bmw" is "applied"

  Scenario: No Search result
    When user searches "qqqqqqNoResultqqqqqq" item
    Then user should see results are "not shown"

  Scenario: Select category
    Given user searches "bmw" item
    When user clicked the "Kiralık Araçlar" from "search result categories"
    Then user should see "Kiralık Araçlar" is selected

  Scenario: Correct amount of results are shown of selected category
    Given user searches "bmw" item
    When user clicked the "Kiralık Araçlar" from "search result categories"
    Then user should see item amount of "Kiralık Araçlar" category is shown

  Scenario: Select city
    Given user searches "bmw" item
    Given user select "İl" combobox as "İzmir"
    When user clicks to the "Search Page Search Button"
    Then user should see results are "shown"
    And user should see results are from "İzmir"

  Scenario: Apply filter
    Given user searches "bmw" item
    Given user click button by "Özel İlanlar" text
    Given user click button by "Ana Sayfa Vitrin" text
    When user clicks to the "Search Page Search Button"
    Then user should see filter "Ana Sayfa Vitrin" is "applied"

  Scenario: Remove applied filter
    Given user searches "bmw" item
    Given user click button by "Özel İlanlar" text
    Given user click button by "Ana Sayfa Vitrin" text
    Given user clicks to the "Search Page Search Button"
    When user remove "Ana Sayfa Vitrin" filter
    Then user should see filter "Ana Sayfa Vitrin" is "not applied"

  Scenario: Apply multiple filter
    Given user searches "bmw" item
    Given user click button by "Özel İlanlar" text
    Given user click button by "Ana Sayfa Vitrin" text
    Given user click button by "Düşük Km" text
    Given user click button by "Yeni Gibi" text
    When user clicks to the "Search Page Search Button"
    Then user should see filter "Ana Sayfa Vitrin" is "applied"
    Then user should see filter "Düşük Km" is "applied"
    Then user should see filter "Yeni Gibi" is "applied"

  Scenario: Remove all filters
    Given user searches "bmw" item
    Given user click button by "Özel İlanlar" text
    Given user click button by "Ana Sayfa Vitrin" text
    Given user click button by "Düşük Km" text
    Given user click button by "Yeni Gibi" text
    Given user clicks to the "Search Page Search Button"
    When user clicks to the "search page clear filters button"
    Then user should not see "active search filters"


  Scenario: Order by price low to high
    Given user searches "bmw" item
    When user applies order filter "Fiyat - Ucuzdan Pahalıya"
    Then user should see that "search result prices" are ordered by "ascending"

  Scenario: Order by price high to low
    Given user searches "bmw" item
    When user applies order filter "Fiyat - Pahalıdan Ucuza"
    Then user should see that "search result prices" are ordered by "descending"

  Scenario: Order by year new to old
    Given user searches "bmw" item
    When user applies order filter "Yıl - Yeniden Eskiye"
    Then user should see that "search result years" are ordered by "descending"

  Scenario: Order by year old to new
    Given user searches "bmw" item
    When user applies order filter "Yıl - Eskiden Yeniye"
    Then user should see that "search result years" are ordered by "ascending"

  Scenario: Order by date new to old
    Given user searches "bmw" item
    When user applies order filter "Tarih - Yeniden Eskiye"
    Then user should see that "search result dates" are ordered by "ascending"


  Scenario: Order by date old to new
    Given user searches "bmw" item
    When user applies order filter "Tarih - Eskiden Yeniye"
    Then user should see that "search result dates" are ordered by "descending"


  Scenario: Reset order
    Given user searches "bmw" item
    Given user applies order filter "Fiyat - Ucuzdan Pahalıya"
    When user applies order filter "Gelişmiş Sıralama"
    Then user should see that "search result prices" are ordered by "not ordered"


  Scenario: Add product to favorites
    Given user clicks to the "Login Menu Button"
    Given user tries to login with "valid" credentials
    Given user searches "bmw" item
    When user added 1. item to the favorites
    Then 1. item is at favorites

  Scenario: Hide product
    Given user searches "bmw" item
    When user click "hide item" for 1. item
    Then user should see 1. item is "hidden"


  Scenario: Show product
    Given user searches "bmw" item
    Given user click "hide item" for 1. item
    When user click "show item" for 1. item
    Then user should see 1. item is "shown"

  Scenario: Open product
    Given user searches "bmw" item
    When user open 1. product
    Then user should see item name is correct
    Then user should see page title contains item title


  Scenario: Pagination works
    Given user searches "bmw" item
    Given user got "atleast 100" result
    When user switch page to "3"
    Then user should see first item name is changed
    Then user should see "3". page is active at pagination

  Scenario: Hovered item color is pink (#ffedf1)
    Given user searches "bmw" item
    When user hover to the "search result items"
    Then "search result items"'s "background-color" property is "#ffedf1"


  Scenario: 20 item per page
    Given user searches "bmw" item
    Given user got "atleast 20" result
    When user set page size to 20
    Then user should see "search result items" returns 20 item

  Scenario: 50 item per page
    Given user searches "bmw" item
    Given user got "atleast 50" result
    When user set page size to 50
    Then user should see "search result items" returns 50 item

  Scenario: All results are shown
    When user searches "bmw" item
    Then user should see all results are shown




