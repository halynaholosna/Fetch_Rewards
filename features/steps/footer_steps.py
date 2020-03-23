from behave import when


@when ('Click on About Us link')
def click_about_us_link(context):
    context.app.footer.click_about_us_link()


@when ('Click on Open Positions link')
def click_open_positions_link(context):
    context.app.footer.click_open_positions_link()
