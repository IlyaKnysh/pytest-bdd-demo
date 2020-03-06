Feature: Check that all header buttons appear

  Scenario Outline: Check each page button
    Given login page is opened
    Then login as Account Manager
    Then check that logged in
    Then I can see the <element>
    Examples:
      | element                      |
      | surveillance_tab             |
      | logout_btn                   |