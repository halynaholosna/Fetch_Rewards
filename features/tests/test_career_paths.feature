# Created by halyna holosna at 3/22/2020

Feature: Tests for Open Positions paths

  Scenario Outline: User can get to Open Positions page by clicking on Open Positions Footer link
    Examples:
    |url            |
    |main           |
    |how-it-works   |
    |brands         |
    |rewards        |
    |referrals      |
    |aboutUs.jsp    |
    |stores         |
    |press          |
    Given Open Fetch Rewards <url> page
    When Click on Open Positions link
    Then Verify Current Job Openings is present on the page

  Scenario: User can get to the Open Positions page from About Us page by clicking View Jobs button
    Given Open Fetch Rewards aboutUs.jsp page
    When Click View Jobs button
    Then Verify Current Job Openings is present on the page

  Scenario: User can get to the Open Positions page from Main Page via About Us page
    Given Open Fetch Rewards main page
    When Click on About Us link
    And Click View Jobs button
    Then Verify Current Job Openings is present on the page
