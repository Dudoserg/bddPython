from behave import *

#use_step_matcher("re")

use_step_matcher("parse")


@given("I am a visitor")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

@when('I visit url "{url}"')
def step_impl(context, url):
    """asdf
    :type context: behave.runner.Context
    """
    pass


@then('I should see title as "{materials}"')
def step_impl(context, materials):
    """
    :type context: behave.runner.Context
    """
    pass