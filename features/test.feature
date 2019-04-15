Feature: showing off behave

Scenario: Run a simple test
    Given I am a visitor
    When I visit url "http://127.0.0.1:8000/materials"
    Then I should see title as "materials"

Scenario: Run a simple test
    Given I am a visitor
    When I visit url "http://127.0.0.1:8000/materials"
    And I click button "add"
    Then I go to the page "http://127.0.0.1:8000/create/"

Scenario: Run a simple test
    Given I am a visitor
    When I visit url "http://127.0.0.1:8000/create"
    And I fill the field title "title"
    And I fill the field addrImage "addrImage"
    And I fill the field code "12"
    Then I fill the field balance "19"

Scenario: Run a simple test
    Given I am a visitor
    When I visit url "http://127.0.0.1:8000/create"
    And I fill the field title "title"
    And I fill the field addrImage "addrImage"
    And I fill the field code "12"
    And I fill the field balance "19"
    And I click  button "create"
    Then The record is added to the database "db.sqlite3" in table "material"
    And delete this material

Scenario: Run a simple test
    Given I am a visitor
    When I visit url "http://127.0.0.1:8000/create"
    And I fill the field title "title"
    And I fill the field addrImage "addrImage"
    And I fill the field code "12"
    And I fill the field balance "19"
    And I click  button "create"
    Then The record is added to the database "db.sqlite3" in table "material"
    And I go to the page "http://127.0.0.1:8000/materials/"
    Then I see an entry added
    And delete this material