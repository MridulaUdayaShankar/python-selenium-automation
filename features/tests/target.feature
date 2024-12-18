Feature: Verify empty cart message on Target website

 Scenario: User can see Cart Empty message
    Given Open target main page
    When Click on cart icon
    Then Verify if Cart Empty message is shown

 Scenario: User can see Sign into your Target account text is shown
    Given Open target main page
    When Click Sign in
    When From right side navigation menu, click Sign in
    Then Verify Sign In form opened
