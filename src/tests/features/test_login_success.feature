Feature: Login 

  Scenario: Check if the user can log in
    Given the user is on the login page
    When the user enters correct login credentials
    Then the user is logged in successfully