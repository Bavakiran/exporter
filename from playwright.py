from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=False, slow_mo=500)
            context = browser.new_context(
                viewport={"width": 1536, "height": 960}  # Simulate maximizing
            )
            page = context.new_page()
            page.goto("https://buyer.indiamart.com/login", timeout=20000)

            page.wait_for_selector("input#mobilemy", timeout=10000)
            page.fill("input#mobilemy", "1111111111")
            page.click("input#signInSubmitButton")

            page.wait_for_timeout(5000)

        except Exception as e:
            print("❌ Exception occurred:", e)

        finally:
            browser.close()

if __name__ == "__main__":
    run()
