Feature: Authentication

  @login
  Scenario: Login
     Given open the page
      When enter username and password
      Then user logged in
      Then page is opened