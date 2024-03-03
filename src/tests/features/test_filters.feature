Feature: filter 

  Scenario: Check basic filters
    Given the user choose category
    When the user filterying by Tops
    Then items shows according to filter