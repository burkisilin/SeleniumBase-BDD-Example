import time

from behave import step
from utils.Helpers import Helpers
from config.Config import TestData

helpers = Helpers()
testData = TestData()


@step('user should see filter "{filter}" is "{state}"')
def filter_is_applied(context, filter, state):
    sb = context.sb
    if state == "applied":
        sb.assert_true(filter in sb.get_text_content(helpers.return_selector("Active Search Filters")))
    elif state == "not applied":
        sb.assert_true(filter not in sb.get_text_content(helpers.return_selector("Active Search Filters")))
    else:
        raise Exception("Unexpected state from feature file!")


@step('user searches "{search_keyword}" item')
def search_item(context, search_keyword):
    sb = context.sb
    sb.type(helpers.return_selector("search input"), search_keyword)
    sb.click(helpers.return_selector("search button"))


@step('user should see results are "{state}"')
def results_shown(context, state):
    sb = context.sb
    item_amount = helpers.return_int_from_string(sb.get_text_content(helpers.return_selector("search result amount")))
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
    if "color-red" in elem_class and category in sb.get_text_content(
            helpers.return_selector("search selected category")):
        sb.assert_true(True)
    else:
        sb.assert_true(False)


@step('user should see item amount of "{category}" category is shown')
def category_item_amount_is_correct(context, category):
    sb = context.sb
    elem_text = sb.get_text_content(helpers.return_selector("search selected category"))
    category_item_amount = helpers.return_int_from_string(elem_text)
    actual_result_amount = helpers.return_int_from_string(sb.get_text_content(helpers.return_selector("search result amount")))
    sb.assert_equal(category_item_amount, actual_result_amount)


@step('user select "{combobox_text}" combobox as "{selection}"')
def select_combobox(context, combobox_text, selection):
    sb = context.sb
    locators_to_click = [f"//span[text()='{combobox_text}']", f"//*[text()='{selection}']", "button.close-cities-items"]
    sb.click_chain(locators_to_click)


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


@step('user remove "{filter}" filter')
def remove_filter(context, filter):
    sb = context.sb
    sb.click_visible_elements(f"//span[contains(text(),'{filter}')]")


@step('user applies order filter "{order}"')
def apply_order(context, order):
    sb = context.sb
    locators_to_click = [helpers.return_selector("search page order dropdown"), f"//*[contains(text(),'{order}')]"]
    sb.click_chain(locators_to_click)


@step('user should see that "{section}" are ordered by "{order}"')
def check_section_order(context, section, order):
    sb = context.sb
    elements = sb.find_elements(helpers.return_selector(section))
    element_texts = []
    for elem in elements:
        elem_value = elem.get_attribute("textContent")
        if "date" not in section:
            elem_value = helpers.return_int_from_string(elem_value)
        else:
            elem_value = elem_value.replace(" ", "").replace("\n", "")
        element_texts.append(elem_value)
    if "date" in section:
        for index in range(len(element_texts)):
            formatted_date = helpers.reformat_turkish_date(element_texts[index])
            element_texts[index] = formatted_date
        sb.assert_true(helpers.items_are_ordered(items_list=element_texts, items_type="date", order_type=order))
    else:
        sb.assert_true(helpers.items_are_ordered(items_list=element_texts, items_type="numeric", order_type=order))


@step('user added {item_index}. item to the favorites')
def add_item_to_fav(context, item_index):
    sb = context.sb
    item_selector = f'{helpers.return_selector("search result items")}[{item_index}]'
    add_to_favorite_button = f'{item_selector}{helpers.return_selector("search result add / remove fav")}'
    sb.hover_and_click(item_selector, add_to_favorite_button)
    sb.click_visible_elements(helpers.return_selector("favorite list"))
    time.sleep(5)


@step("{item_index}. item is at favorites")
def item_is_at_favorites(context, item_index):
    sb = context.sb
    item_selector = f'{helpers.return_selector("search result items")}[{item_index}]'
    sb.hover(item_selector)
    sb.assert_text("Favorilerimde", helpers.return_selector("search result add / remove fav"))


@step('user click "{state}" for {item_index}. item')
def hide_show_item(context, state, item_index):
    sb = context.sb
    item_selector = f'{helpers.return_selector("search result items")}[{item_index}]'
    hide_show_button = f'{item_selector}{helpers.return_selector(state)}'
    if state == "show item":
        sb.click_visible_elements(hide_show_button)
    else:
        sb.hover_and_click(item_selector, hide_show_button)


@step('user should see {item_index}. item is "{state}"')
def item_state_is_correct(context, state, item_index):
    sb = context.sb
    item_selector = f'{helpers.return_selector("search result items")}[{item_index}]'
    sb.hover(item_selector)
    if state == "hidden":
        text_to_assert = "Göster"
        state = "show item"
    elif state == "shown":
        text_to_assert = "Gizle"
        state = "hide item"
    else:
        raise Exception("Invalid state provided at cucumber file!")

    hide_show_button = f'{item_selector}{helpers.return_selector(state)}'
    sb.assert_text(text_to_assert, hide_show_button)


@step("user open {1}. product")
def open_product(context, item_index):
    sb = context.sb
    item_selector = f'{helpers.return_selector("search result items")}[{item_index}]'
    item_name = sb.get_text_content(f"{item_selector}{helpers.return_selector('item titles')}")
    context.item_name = item_name
    sb.click(item_selector)


@step("user should see item name is correct")
def product_name_is_correct(context):
    sb = context.sb
    detail_item_name = sb.get_text_content(helpers.return_selector("item detail title"))
    sb.assert_equal(detail_item_name, context.item_name)


@step("user should see page title contains item title")
def page_title_is_item_title(context):
    sb = context.sb
    sb.assert_true(context.item_name in sb.get_title())


@step('user got "{result_type}" result')
def search_result_amount(context, result_type):
    sb = context.sb
    search_result_amount = helpers.return_int_from_string(sb.get_text_content(helpers.return_selector("search result amount")))
    expected_result_amount = helpers.return_int_from_string(result_type)
    if "atleast" in result_type:
        sb.assert_true(search_result_amount >= expected_result_amount)
    elif "max" in result_type:
        sb.assert_true(search_result_amount <= expected_result_amount)
    else:
        sb.assert_true(search_result_amount == expected_result_amount)


@step('user switch page to "{page}"')
def switch_pagination(context, page):
    sb = context.sb
    item_selector = f'{helpers.return_selector("search result items")}[1]'
    first_item_name = sb.get_text_content(f"{item_selector}{helpers.return_selector('item titles')}")
    context.first_item_name = first_item_name  # store first item name so it can be controlled later on
    sb.click(f"#paging_{page}")


@step("user should see first item name is changed")
def first_item_is_changed(context):
    sb = context.sb
    item_selector = f'{helpers.return_selector("search result items")}[1]'
    new_first_item_name = sb.get_text_content(f"{item_selector}{helpers.return_selector('item titles')}")
    old_first_item_name = context.first_item_name
    sb.assert_not_equal(new_first_item_name, old_first_item_name)


@step('user should see "{page}". page is active at pagination')
def pagination_page_is_active(context, page):
    sb = context.sb
    sb.assert_true(sb.get_attribute(f"//a[@id='paging_{page}']/parent::li", "class") == "active")