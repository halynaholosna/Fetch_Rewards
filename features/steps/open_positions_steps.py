from behave import then


@then('Verify {expected_text} is present on the page')
def verify_open_positions_title(context, expected_text):
    context.app.open_positions.verify_open_positions_title(expected_text)