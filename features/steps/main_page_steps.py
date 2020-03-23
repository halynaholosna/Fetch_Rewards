from behave import given


@given('Open Fetch Rewards {url} page')
def open_page(context, url):
    if url == 'main':
        url = ''
    context.app.main_page.open_page(url)