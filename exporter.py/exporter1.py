from playwright.sync_api import sync_playwright

def fill_quote_form(quote_page):
    quote_page.wait_for_selector("input#nameBLInput", timeout=10000)
    quote_page.fill("input#nameBLInput", "John Doe")
    quote_page.fill("input#emailBLInput", "johndoe123@temp-mail.org")
    quote_page.fill("input#numberBLInput", "9999999999")
    quote_page.fill("input#quantityBLInput", "1")
    quote_page.select_option("select#quantityUnitSelect", label="Piece")
    quote_page.fill("textarea#descBLInput", "Hi Hello")
    quote_page.click("button.btn-green", timeout=10000)
    quote_page.wait_for_timeout(5000)
    try:
        quote_page.click("svg[width='22'][height='22'] path[d^='M10.9998']", timeout=5000)
    except Exception as close_err:
        print("❌ Could not click close icon:", close_err)

def run():
    with sync_playwright() as p:
        browser = None
        try:
            browser = p.chromium.launch(headless=False, slow_mo=500)
            context = browser.new_context(viewport={"width": 1536, "height": 960})
            page = context.new_page()

            # Step 1: Search "ball"
            page.goto("https://www.indiamart.com/", timeout=20000)
            page.fill("input#search_string", "ball")
            page.click("input#btnSearch")
            page.wait_for_load_state("networkidle")

            # Step 2: Get Quote
            with context.expect_page() as new_tab:
                page.click("a:has-text('Get Quote')")
            quote_page = new_tab.value
            quote_page.wait_for_load_state("domcontentloaded")
            fill_quote_form(quote_page)

            # Step 3–9: Settings adjustments
            page.bring_to_front()
            page.click("text=English")
            page.click("text=Save")
            page.click("#currencyText")
            page.select_option("select#currency-select", value="USD")
            page.click("#currencyWrapper .save-btn")

            # Step 10: Click Sign In
            print("➡ Clicking Sign In (1st time)...")
            page.locator("div.sign-in-btn.language-currency-btn").scroll_into_view_if_needed()
            page.locator("div.sign-in-btn.language-currency-btn").click(force=True)
            page.wait_for_timeout(2000)

            # Step 11: Click Home
            page.click("a:has-text('Home')")

            # Step 12: Search for toys
            page.fill("input#searchInputHome", "toys")
            page.click("button#btnSearchHome")
        

            # Step 13: Expand Sign In dropdown
            print("🔄 Step 13: Clicking 'Sign In' to open dropdown...")
            try:
                page.click("div.sign-in-btn.language-currency-btn")
                page.wait_for_selector("a[href*='get-quote']", timeout=5000)
                print("✅ Dropdown opened successfully.")
            except Exception as e:
                print("❌ Step 13 failed:", e)

            # Step 14: Click Get Quote from dropdown
            print("🔄 Step 14: Clicking 'Get Quote' inside dropdown...")
            try:
                with context.expect_page(timeout=10000) as new_tab2:
                    page.click("a[href*='get-quote']", timeout=5000)
                quote_page2 = new_tab2.value
                quote_page2.wait_for_load_state("domcontentloaded")
                quote_page2.wait_for_selector("input#nameBLInput", timeout=10000)
                print("✅ Second Get Quote page loaded.")
                # Step 15: Fill quote form again
                print("➡ Step 15: Filling second quote form...")
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
