Feature: Shoping flow 

  Scenario: Check shoping flow 
    Given User login on Website and choose category
    When Choose item and change propereties of item
    When Go to summary, increase items amount and proceed checkout
    When User enter address data
    When User accept agreement
    When User choose payment method
    Then Payment successfull