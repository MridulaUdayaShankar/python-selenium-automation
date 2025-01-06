Feature: Test for cart functionality
    Then Verify cart Empty message shown


Scenario: User can add a product to cart
  Scenario: User can add a product to cart
    Given Open target main page
    When Search for tea
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    And Store product name
    Then Verify cart has 1 item(s)
    And Verify cart has correct product