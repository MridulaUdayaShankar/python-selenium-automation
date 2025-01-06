Feature: Test cases for search


  Scenario: User searches for a product
    Given Open target main page
    When Search for tea
    Then Verify that correct search results shown for {product}

Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image