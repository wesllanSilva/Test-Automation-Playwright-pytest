def test_abrir_google(page):
    page.goto("https://www.google.com")
    page.pause()
    page.get_by_role("button", name="Pesquisa Google").click()
    print(page.title())
    assert "Google" in page.title()