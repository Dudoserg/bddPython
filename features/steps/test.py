from behave import *
from selenium import webdriver
from sys import platform
#use_step_matcher("re")

use_step_matcher("parse")


@given("I am a visitor")
def step_impl(context):
    if platform == "linux" or platform == "linux2":
        context.driver = webdriver.Chrome(executable_path=r'myLib/chromedriver')
        print("linux")
    else:
        context.driver = webdriver.Chrome(executable_path=r'myLib/chromedriver.exe')
        print("not linux")

    pass

@when('I visit url "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    context.myTitle = context.driver.title
    pass


@then('I should see title as "{materials}"')
def step_impl(context, materials):
    assert context.myTitle == materials



@step('I click button "add"')
def step_impl(context):
    btn = context.driver.find_element_by_id("addBtn")
    btn.click()
    print()


@then('I go to the page "{url}"')
def step_impl(context, url):

    assert url == context.driver.current_url


@step('I fill the field title "{title}"')
def step_impl(context,title):
    elem = context.driver.find_element_by_id('title')
    elem.send_keys(title)
    read = elem.get_attribute('value')
    assert title == read
    pass


@step('I fill the field addrImage "{addrImage}"')
def step_impl(context,addrImage):
    elem = context.driver.find_element_by_id('address')
    elem.send_keys(addrImage)
    read = elem.get_attribute('value')
    assert addrImage == read
    pass


@step('I fill the field code "{code:d}"')
def step_impl(context,code):
    elem = context.driver.find_element_by_id('code')
    elem.send_keys(str(code))
    read = elem.get_attribute('value')
    assert str(code) == read
    pass


@then('I fill the field balance "{balance:d}"')
def step_impl(context,balance):
    elem = context.driver.find_element_by_id('balance')
    elem.send_keys(str(balance))
    read = elem.get_attribute('value')
    assert str(balance) == read
    pass