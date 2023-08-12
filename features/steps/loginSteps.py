import time

from behave import step
from utils.Helpers import Helpers
from config.Config import TestData

helpers = Helpers()
testData = TestData()


@step('User tries to login with "{credential_type}" credentials')
def login_with_creds(context, credential_type):
    sb = context.sb

    email = testData.LOGIN_CREDENTIALS[credential_type]["email"]
    password = testData.LOGIN_CREDENTIALS[credential_type]["password"]

    sb.type(helpers.return_selector("Login Email"), email)
    sb.type(helpers.return_selector("Login Password"), password)
    sb.click(helpers.return_selector("Login Button"))
















@step('user should not see "{locator}"')  # yarım
def user_should_not_see_element(context, locator):
    sb = context.sb
    sb.assert_element(helpers.return_selector(locator))
    sb.is_text_visible()


@step('type test "{locator}" "{text}"')
def type_test(context, locator, text):
    sb = context.sb
    sb.type(helpers.return_selector(locator), text)


@step('sleep "{sec}" seconds')
def sleep_secs(context, sec):
    time.sleep(int(sec))


