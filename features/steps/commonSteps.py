from behave import step
from utils.Helpers import Helpers
from config.Config import TestData

helpers = Helpers()
testData = TestData()

@step('user should see page title is "{expected_title}"')
def page_title_is(context, expected_title):
    context.sb.assert_title(expected_title)


@step("user is not logged in")
def step_impl(context):
    context.sb.clear_local_storage()


@step('Open the "{}"')
def open_page(context, page):
    sb = context.sb
    sb.open(page)


@step('User is at "{page}"')
def go_to_page(context, page):
    sb = context.sb
    sb.open(helpers.return_page_url(page))


@step('user clicks to the "{locator}"')
def click_to_element(context, locator):
    sb = context.sb
    sb.click(helpers.return_selector(locator))


@step('user should see "{locator}"')
def user_should_see_element(context, locator):
    sb = context.sb
    sb.assert_element(helpers.return_selector(locator))


@step('user should see url is "{page}"')
def step_impl(context, page):
    sb = context.sb
    sb.assert_true(sb.get_current_url() == helpers.return_page_url(page))


@step('user should see text "{text}"')
def user_should_see_text(context, text):
    sb = context.sb
    sb.assert_element(f"//*[contains(text(),'{text}')]")


@step('"{element}"\'s "{attribute}" attribute has "{required_value}"')
def step_impl(context, element, attribute, required_value):
    sb = context.sb
    sb.assert_true(required_value in (sb.get_attribute(helpers.return_selector(element), attribute)))