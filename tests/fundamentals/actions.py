def test_click(page):
    page.goto("https://automationexercise.com/")
    page.pause()
    #page.get_by_role("link", name="Website for automation").click(button="right")
    page.get_by_role("link", name="Website for automation").click()
    #page.get_by_role("link", name="Website for automation").click(position={ "x": 50, "y": 70})
    page.get_by_role("link", name="(5) H&M").click()
    page.get_by_role("link", name="(5) H&M").click(modifiers=['Control'])   # Alt|Control|ControlOrMeta|Meta|Shift

def test_click_notability(page):
    page.goto("https://bootswatch.com/default/")
    page.pause()
    page.get_by_role('button', name='Primary').nth(1).click(timeout=5000)

def test_fill(page):
    page.goto('https://automationexercise.com/login')
    page.pause()
    page.get_by_role("textbox", name="Name").fill('Wesllan', timeout=10000)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill('teste@wstack.com')
    page.get_by_role("button", name="Signup").click()

def test_check_uncheck(page):
    page.goto('https://bootswatch.com/default/')
    page.pause()
    page.get_by_role("checkbox", name="Default checkbox").check()
    page.get_by_role("checkbox", name="Default checkbox").uncheck()
    page.pause()
