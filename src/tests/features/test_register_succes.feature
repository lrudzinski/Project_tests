Feature: Register 

  Scenario: Check if the user can register
    Given the user is on the register page
    When  the user enters correct register data
    Then  the user is registered successfully