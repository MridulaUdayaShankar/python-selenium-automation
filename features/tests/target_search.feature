Feature: Test cases for search


  Scenario: User searches for a product
    Given Open target main page
    When Search for tea
    Then Verify that correct search results shown for {product}


