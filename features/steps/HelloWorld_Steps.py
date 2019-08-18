from behave import given, when, then
from hamcrest import assert_that, equal_to

from hello.HelloWorld import HelloWorld

#
# 'Then' step, which asserts the output of
# {@link HelloWorld#printGreeting()} equals the supplied value.
#
# @param greeting The expected greeting from the {@link HelloWorld} class.
#
@then('should result in "{greeting}"')
def check_greeting(context, greeting):
    assert_that(context.greeter.print_greeting(), equal_to(greeting))


#
# Given' step, which asserts the {@link HelloWorld#setName(String)}
# method properly saves the supplied name.
#
# @param name The name to set in the {@link HelloWorld} class.
#
@given('the name "{name}"')
def set_name(context, name):
    context.greeter = HelloWorld()
    context.greeter.name = name
    assert_that(context.greeter.name, equal_to(name))


#
# 'When' step, which asserts the {@link HelloWorld#setSalutation(String)}
# method properly saves the supplied salutation.
#
# @param salutation The salutation to set in the {@link HelloWorld} class.
#
@when('combined with "{salutation}"')
def set_salutation(context, salutation):
    context.greeter.salutation = salutation
    assert_that(context.greeter.salutation, equal_to(salutation))
