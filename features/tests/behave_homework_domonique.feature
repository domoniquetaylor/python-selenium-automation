# Created by domon at 2/17/2023
Feature: Test Scenarios for Sign In via Returns and Orders

  Scenario: User can verify that logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Click Orders
    Then Sign In header is visible
    And Email input field is present


Scenario: User can verify that Amazon cart is empty
    Given Open Amazon page
    When Click Cart Icon
    Then Verify Cart is Empty