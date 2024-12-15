Feature: Test cases for Target cart

Scenario: 'Your cart is empty message is shown'
    Given Open target main page
    When Click on cart icon
    Then Verify cart empty message is shown

Scenario: User can add a product to cart
    Given Open target main page
    When Search for tea
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product