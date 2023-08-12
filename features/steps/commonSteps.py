import time

from behave import step
from utils.Helpers import Helpers
from config.Config import TestData

helpers = Helpers()
testData = TestData()


@step('user should see page title is "{expected_title}"')
def page_title_is(context, expected_title):
    context.sb.assert_title(expected_title)


@step("user is not logged in")
def clear_local_storage(context):
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
def page_url_is(context, page):
    if "http" in page:
        expected_url = page
    else:
        expected_url = helpers.return_page_url(page)

    sb = context.sb
    sb.assert_true(sb.get_current_url() == expected_url)


@step('user should see text "{text}"')
def user_should_see_text(context, text):
    sb = context.sb
    sb.assert_element(f"//*[contains(text(),'{text}')]")


@step('"{element}"\'s "{attribute}" attribute has "{required_value}"')
def element_attr_has_value(context, element, attribute, required_value):
    sb = context.sb
    sb.assert_true(required_value in (sb.get_attribute(helpers.return_selector(element), attribute)))


@step('user should see "{item}" contains "{itemText}" text')
def menu_contains_text(context, item, itemText):
    sb = context.sb
    texts = sb.get_text_content(helpers.return_selector(item))
    sb.assert_true(itemText in texts)


@step('user should see "{locator}" contains "{item_amount}" items')
def elem_contains_number_of_items(context, locator, item_amount):
    sb = context.sb
    sb.assert_true(len(sb.find_elements(f"{helpers.return_selector(locator)}>li")) == int(item_amount))


@step("user is accepted cookie popup")
def accept_cookie_popup(context):
    sb = context.sb
    sb.click(helpers.return_selector("accept cookie button"))


@step('user should not see "{locator}"')
def user_should_not_see_element(context, locator):
    sb = context.sb
    sb.assert_false(sb.is_element_visible(helpers.return_selector(locator)))


@step("User refreshes the page")
def refresh_page(context):
    sb = context.sb
    sb.refresh_page()


@step('user clicked the "{text}" from "{locator}"')
def click_text_from_items(context, text, locator):
    sb = context.sb
    elements = sb.find_elements(helpers.return_selector(locator))
    clicked = False
    for elem in elements:
        if text in elem.get_attribute("textContent"):
            print(elem.get_attribute("textContent"))
            elem.click()
            clicked = True
            break
    if not clicked:
        sb.assert_true(False)  # fail the test if the click has not made


@step('user select "{combobox_text}" combobox as "{selection}"')
def select_combobox(context, combobox_text, selection):
    sb = context.sb
    locators_to_click = [f"//span[text()='{combobox_text}']", f"//*[text()='{selection}']", "button.close-cities-items"]
    sb.click_chain(locators_to_click)
    time.sleep(3)
