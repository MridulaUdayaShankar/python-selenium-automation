Feature: Test cases for search


  Scenario: User searches for a product
    Given Open target main page
    When Search for tea
    Then Verify that correct search results shown for {product}
    Then Verify search term tea in URL
    When Search for Coca Cola
    Then Verify search results shown for Coca Cola
    Then Verify search term coca+cola in URL

Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image