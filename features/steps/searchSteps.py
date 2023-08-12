from behave import step
from utils.Helpers import Helpers
from config.Config import TestData

helpers = Helpers()
testData = TestData()


@step('user should see "{filter}" filter is applied')
def filter_is_applied(context, filter):
    sb = context.sb
    sb.assert_true(filter in sb.get_text_content(helpers.return_selector("Active Search Filters")))
