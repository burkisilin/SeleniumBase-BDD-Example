# Created by Burak at 12.08.2023
Feature: # Enter feature name here
  # Enter feature description here

  Background:
    Given user is not logged in
    Given user is at "HomePage"

  Scenario: Search results are shown
    When user searches "bmw" item
    Then user should see results are "shown"

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
    Then user should see results are from "İzmir"

  Scenario: Apply filter
  Scenario: Remove applied filter
  Scenario: Apply multiple filter
  Scenario: Remove all filters
  Scenario: List view
  Scenario: Bigger List view
  Scenario: Table view
  Scenario: Order by price low to high
  Scenario: Order by price high to low
  Scenario: Order by year new to old
  Scenario: Order by year old to new
  Scenario: Order by date new to old
  Scenario: Order by date old to new
  Scenario: Reset order
  Scenario: Add product to favorites
  Scenario: Hide product
  Scenario: Show product
  Scenario: Open product
  Scenario: Add product to compare list
  Scenario: Remove product from compare list
  Scenario: Remove all products from compare list
  Scenario: Compare 2 product
  Scenario: Compare 3 product
  Scenario: Compare product items are remains after the compare box is closed and opened again
  Scenario: Try to add more than 3 product to compare list
  Scenario: Switch tabpanel
  Scenario: Switch tabpanel does not change filter applied
  Scenario: Pagination works
  Scenario: 20 item per page
  Scenario: 50 item per page
  Scenario: All results are shown
  Scenario: Hovered item color is pink


