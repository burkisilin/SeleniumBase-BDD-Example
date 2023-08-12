from behave import step
from utils.Helpers import Helpers
from config.Config import TestData

helpers = Helpers()
testData = TestData()


@step('user should see "{filter}" filter is applied')
def filter_is_applied(context, filter):
    sb = context.sb
    sb.assert_true(filter in sb.get_text_content(helpers.return_selector("Active Search Filters")))


@step('user searches "{search_keyword}" item')
def search_item(context, search_keyword):
    sb = context.sb
    sb.type(helpers.return_selector("search input"), search_keyword)
    sb.click(helpers.return_selector("search button"))


@step('user should see results are "{state}"')
def results_shown(context, state):
    sb = context.sb
    item_amount = int(sb.get_text_content(helpers.return_selector("search result amount")).replace(".",""))
    if state == "shown":
        sb.assert_true(sb.is_element_visible(helpers.return_selector("search result items")) and item_amount > 0)
    elif state == "not shown":
        sb.assert_true(sb.is_text_visible("Sonuç bulunamadı.") and item_amount == 0)
    else:
        raise Exception("Invalid state provided at cucumber file!")


@step('user should see "{category}" is selected')
def category_is_selected(context, category):
    sb = context.sb
    elem_class = sb.get_attribute(helpers.return_selector("search selected category"), "class")
    if "color-red" in elem_class and category in sb.get_text_content(helpers.return_selector("search selected category")):
        sb.assert_true(True)
    else:
        sb.assert_true(False)


@step('user should see item amount of "{category}" category is shown')
def category_item_amount_is_correct(context, category):
    sb = context.sb
    elem_text = sb.get_text_content(helpers.return_selector("search selected category"))
    category_item_amount = helpers.return_int_from_string(elem_text)
    actual_result_amount = int(sb.get_text_content(helpers.return_selector("search result amount")).replace(".", ""))
    sb.assert_equal(category_item_amount, actual_result_amount)


@step('user should see results are from "{city}"')
def results_from_city(context, city):
    sb = context.sb
    city_elements = sb.find_elements("//tr[contains(@class,'listing-list-item')]/td[7]")
    no_error = True
    for element in city_elements:
        if city.lower() not in element.get_attribute("textContent").lower():
            no_error = False
            break
    sb.assert_true(no_error)

