# Created by domon at 3/3/2023
Feature: Amazon Bestsellers Page


  Scenario: User can open the Amazon Bestsellers Page
    Given Open Amazon page
    When Click on Bestsellers link
    Then Verify links are visible 