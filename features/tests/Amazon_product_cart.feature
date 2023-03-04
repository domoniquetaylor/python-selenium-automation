# Created by domon at 3/3/2023
Feature: Adding a product to the cart
  # Enter feature description here

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input text Vase
    When Click on Search button
    And Click on a product
    And Click Add to Cart button
    And Click Cart Icon
    And Open Cart Page
    Then Verify that cart has 1 item(s)