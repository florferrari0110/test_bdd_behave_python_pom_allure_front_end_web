Feature: Test Page https://www.demoblaze.com/index.html

 @Browser
  Scenario: Sign in Page
    Given The user is in the main page https://www.demoblaze.com/index.html
    And The user click on sing up
    And The user enters correct data
    When The user click on sign up button
    Then Assert that the text of pop up is Sign up successful
    Then Close the browser

  @Browser  
   Scenario: Log in
    Given The user is in the main page https://www.demoblaze.com/index.html
    And The user click on log in
    And The user enter correct credentials
    When The user click on log in button
    Then Assert that the name of user is in the banner
    And Close the browser

  @Browser
  Scenario: Log out
    Given The user is in the main page https://www.demoblaze.com/index.html
    And The user click on log in
    And The user enter correct credentials
    And The user click on log in button
    When The user click on log out
    Then Assert that the sign up link is visible
    Then Close the browser
    
  @Browser
  Scenario: Add product to cart
    Given The user is in the main page https://www.demoblaze.com/index.html
    And The user click on link Laptops
    And The user select the product Sony vaio i5
    When The user click on add to cart
    Then Assert the text of pop up is Product added
    Then Close the browser