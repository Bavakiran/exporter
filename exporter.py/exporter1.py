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
            # Step 1: Launch the browser
            browser = p.chromium.launch(headless=False, slow_mo=500)
            context = browser.new_context(viewport={"width": 1536, "height": 960})
            page = context.new_page()

            # Step 2: Scroll on the homepage
            page.goto("https://export.indiamart.com/", timeout=20000)
            for _ in range(10):  # Adjust range for scrolling
                page.mouse.wheel(0, 100)  # Scroll down by 100 pixels
                page.wait_for_timeout(300)
            print("✅ Page scrolled successfully.")

            # Step 3: Click "Get Quote" and fill form
            with context.expect_page() as new_tab:
                page.click("a:has-text('Get Quote')")
            quote_page = new_tab.value
            quote_page.wait_for_load_state("domcontentloaded")
            fill_quote_form(quote_page)

            # Step 4: Adjust settings (Language, Currency)
            page.bring_to_front()
            page.click("text=English")
            page.click("text=Save")
            page.click("#currencyText")
            page.select_option("select#currency-select", value="USD")
            page.click("#currencyWrapper .save-btn")
            print("✅ Settings adjusted.")

            # Step 5: Click "Sign In" dropdown
            print("➡ Clicking Sign In (1st time)...")
            page.locator("div.sign-in-btn.language-currency-btn").scroll_into_view_if_needed()
            page.locator("div.sign-in-btn.language-currency-btn").click(force=True)
            page.wait_for_timeout(2000)

            # Step 6: Navigate to Home
            page.click("a:has-text('Home')")

            # Step 7: Search for toys
            page.fill("input#searchInputHome", "toys")
            page.click("button#btnSearchHome")
            print("✅ Toys search completed.")

            # Step 8: Expand Sign In dropdown
            print("🔄 Step 13: Clicking 'Sign In' to open dropdown...")
            try:
                page.click("div.sign-in-btn.language-currency-btn")
                page.wait_for_selector("a[href*='get-quote']", timeout=5000)
                print("✅ Dropdown opened successfully.")
            except Exception as e:
                print("❌ Step 13 failed:", e)

            # Step 9: Click Get Quote from dropdown and fill form
            print("🔄 Step 14: Clicking 'Get Quote' inside dropdown...")
            try:
                with context.expect_page(timeout=10000) as new_tab2:
                    page.click("a[href*='get-quote']", timeout=5000)
                quote_page2 = new_tab2.value
                quote_page2.wait_for_load_state("domcontentloaded")
                quote_page2.wait_for_selector("input#nameBLInput", timeout=10000)
                print("✅ Second Get Quote page loaded.")
                fill_quote_form(quote_page2)
            except Exception as e:
                print("❌ Step 14 failed:", e)

        except Exception as e:
            print("❌ Main exception occurred:", e)
        finally:
            if browser:
                browser.close()

if __name__ == "__main__":
    run()
