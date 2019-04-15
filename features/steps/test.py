from behave import *
from selenium import webdriver
from sys import platform
import django
django.setup()
from seleniumBdd.models import Material

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
    context.title = title
    elem = context.driver.find_element_by_id('title')
    elem.send_keys(title)
    read = elem.get_attribute('value')
    assert title == read
    pass


@step('I fill the field addrImage "{addrImage}"')
def step_impl(context,addrImage):
    context.addrImage = addrImage
    elem = context.driver.find_element_by_id('address')
    elem.send_keys(addrImage)
    read = elem.get_attribute('value')
    assert addrImage == read
    pass


@step('I fill the field code "{code:d}"')
def step_impl(context,code):
    context.code = code
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


@step('I fill the field balance "{balance:d}"')
def step_impl(context,balance):
    context.balance = balance
    elem = context.driver.find_element_by_id('balance')
    elem.send_keys(str(balance))
    read = elem.get_attribute('value')
    assert str(balance) == read
    pass

    # raise NotImplementedError(u'STEP: And I fill the field balance "19"')


@step('I click  button "create"')
def step_impl(context):
    btn = context.driver.find_element_by_id("createBtn")
    btn.click()
    # raise NotImplementedError(u'STEP: And I click  button "create"')


@then('The record is added to the database "{dbName}" in table "{tableName}"')
def step_impl(context, dbName, tableName):
    pass
    material = Material.objects.filter(title=context.title, code_material=context.code, img=context.addrImage, balance=context.balance)[0]
    context.id = material.pk
    print("id = " + str(material.id))
    assert material is not None
    # raise NotImplementedError(u'STEP: Then The record is added to the database "db.sqlite3" in table "material"')


@step('I click button "back"')
def step_impl(context):
    btn = context.driver.find_element_by_id("backBtn")
    btn.click()
    # raise NotImplementedError(u'STEP: And I click button "back"')


@step('I go to the page "{url}"')
def step_impl(context, url):
    assert url == context.driver.current_url
    # raise NotImplementedError(u'STEP: And I go to the page "http://127.0.0.1:8000/materials/"')


@then("I see an entry added")
def step_impl(context):
    print(context.id)
    currentMaterial = context.driver.find_element_by_id(str(context.id))
    assert currentMaterial is not None
    # raise NotImplementedError(u'STEP: Then I see an entry added')


@step("delete this material")
def step_impl(context):
    material = Material.objects.filter(title=context.title, code_material=context.code, img=context.addrImage, balance=context.balance)[0]
    material.delete()
    # raise NotImplementedError(u'STEP: And delete this material')