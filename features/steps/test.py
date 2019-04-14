from behave import *
from selenium import webdriver

#use_step_matcher("re")

use_step_matcher("parse")


@given("I am a visitor")
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r'myLib/chromedriver.exe')
    pass

@when('I visit url "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    context.myTitle = context.driver.title
    pass


@then('I should see title as "{materials}"')
def step_impl(context, materials):
    assert context.myTitle == materials
    pass


@step('I click button "add"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('I go to the page "http://127.0.0.1:8000/create"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass