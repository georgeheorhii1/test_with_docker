from playwright.sync_api import sync_playwright


def test_youtube():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.youtube.com/")
        assert "YouTube" in page.title()
        browser.close()
        print("Test is done")



if __name__ == "__main__":
    test_youtube()
