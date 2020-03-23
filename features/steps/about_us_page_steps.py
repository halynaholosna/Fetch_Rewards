from behave import when


@when('Click View Jobs button')
def click_view_jobs_btn(context):
    context.app.about_us_page.click_about_us_btn()
