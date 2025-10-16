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