from playwright.sync_api import sync_playwright

def fill_quote_form(quote_page):
    """Fills out and submits the quote form on the given page."""
    try:
        quote_page.wait_for_selector("input#nameBLInput", timeout=10000)
        quote_page.fill("input#nameBLInput", "John Doe")
        quote_page.fill("input#emailBLInput", "johndoe123@temp-mail.org")
        quote_page.fill("input#numberBLInput", "9999999999")
        quote_page.fill("input#prodNameBLInput", "Cab Service")
        quote_page.fill("textarea#descBLInput", "Hi Hello")
        quote_page.wait_for_timeout(5000)
        quote_page.click("button.btn-green", timeout=10000)

        # Try closing the success popup
        try:
            quote_page.click("svg[width='22'][height='22']", timeout=5000)
        except Exception as close_err:
            print("❌ Could not click close icon:", close_err)

    except Exception as e:
        print("❌ Error while filling the quote form:", e)


def run():
    with sync_playwright() as p:
        browser = None
        try:
            # Launch the browser
            browser = p.chromium.launch(headless=False, slow_mo=500)
            context = browser.new_context(viewport={"width": 1536, "height": 960})
            page = context.new_page()

            # Landing
            page.goto("https://export.indiamart.com/", timeout=20000)
            for _ in range(10):  # Scroll down
                page.mouse.wheel(0, 100)
                page.wait_for_timeout(300)
            print("✅ Landed successfully.")

            # Click "Get Quote" and fill form
            with context.expect_page() as new_tab:
                page.click("a:has-text('Get Quote')")
            quote_page = new_tab.value
            quote_page.wait_for_load_state("domcontentloaded")
            fill_quote_form(quote_page)
            print("✅ Requirement1 Submitted successfully")

            # Change language and currency
            page.bring_to_front()
            page.click("text=English")
            page.click("text=Save")
            page.click("#currencyText")
            page.select_option("select#currency-select", value="USD")
            page.click("#currencyWrapper .save-btn")
            print("✅ Language and currency changed")

            # Open SignIn dropdown and click Home
            page.locator("div.sign-in-btn.language-currency-btn").scroll_into_view_if_needed()
            page.locator("div.sign-in-btn.language-currency-btn").click(force=True)
            page.wait_for_timeout(2000)
            page.click("a:has-text('Home')")
            print("✅ Clicked on Home")

            # Search for "toys"
            page.fill("input#searchInputHome", "toys")
            page.click("button#btnSearchHome")
            print("✅ Toys search completed.")

            # Open SignIn dropdown again
            try:
                page.click("div.sign-in-btn.language-currency-btn")
                page.wait_for_selector("a[href*='get-quote']", timeout=5000)
                print("✅ Dropdown opened successfully.")
            except Exception as e:
                print("❌ Step failed while opening dropdown:", e)

            # Open new quote page and fill form
            try:
                with context.expect_page(timeout=10000) as new_tab2:
                    page.click("a[href*='get-quote']", timeout=5000)
                quote_page2 = new_tab2.value
                quote_page2.wait_for_load_state("domcontentloaded")
                quote_page2.wait_for_selector("input#nameBLInput", timeout=10000)
                fill_quote_form(quote_page2)
                print("✅ Requirement2 Submitted successfully")
            except Exception as e:
                print("❌ Requirement2 form fill failed:", e)

        except Exception as e:
            print("❌ Main exception occurred:", e)
        finally:
            if browser:
                browser.close()


if __name__ == "__main__":
    run()
