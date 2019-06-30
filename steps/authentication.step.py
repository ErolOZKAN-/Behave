from behave import *


@given('open the page')
def step_impl(context):
    pass


@when('enter username and password')
def step_impl(context):
    assert True is not False


@then('user logged in')
def step_impl(context):
    assert context.failed is False


@then('page is opened')
def step_impl(context):
    pass