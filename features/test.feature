Feature: showing off behave

Scenario: Run a simple test
    Given I am a visitor
    When I visit url "http://127.0.0.1:8000/materials"
    Then I should see title as "materials"