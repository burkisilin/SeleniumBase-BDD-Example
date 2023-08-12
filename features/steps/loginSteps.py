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


@step('"{field}" is entered as "{inpt}"')
def enter_field(context, field, inpt):
    context.sb.type(helpers.return_selector(field), inpt)


@step('type test "{locator}" "{text}"')
def type_test(context, locator, text):
    sb = context.sb
    sb.type(helpers.return_selector(locator), text)


@step('sleep "{sec}" seconds')
def sleep_secs(context, sec):
    time.sleep(int(sec))


@step('password is "{needed_visibility}"')
def switch_password_visibility(context, needed_visibility):
    if not (needed_visibility.lower() == "hidden" or needed_visibility.lower() == "shown"):
        raise Exception("Unexpected keyword from cucumber file!")

    sb = context.sb
    pw_input_type = sb.get_attribute(helpers.return_selector("Login Password"), "type")
    if pw_input_type == "password":
        current_state = "hidden"
    elif pw_input_type == "text":
        current_state = "shown"

    if needed_visibility != current_state:
        sb.click(helpers.return_selector("Hide / Show Password Icon"))
