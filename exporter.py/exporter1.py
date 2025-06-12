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
        try:
            browser = p.chromium.launch(headless=False, slow_mo=500)
            context = browser.new_context(viewport={"width": 1536, "height": 960})
            page = context.new_page()

            # Step 1: Visit IndiaMART and search "ball"
            page.goto("https://www.indiamart.com/", timeout=20000)
            page.wait_for_selector("input#search_string", timeout=10000)
            page.fill("input#search_string", "ball")
            page.click("input#btnSearch")
            page.wait_for_load_state("networkidle")

            # Step 2: Click on Get Quote and handle popup
            with context.expect_page() as new_tab:
                page.click("a:has-text('Get Quote')")
            quote_page = new_tab.value
            quote_page.wait_for_load_state("domcontentloaded")

            # Step 3-6: Fill and submit form
            fill_quote_form(quote_page)

            # Step 7: Switch back to parent
            page.bring_to_front()

            # Step 8: Click English and Save
            page.wait_for_selector("text=English", timeout=5000)
            page.click("text=English")
            page.wait_for_selector("text=Save", timeout=5000)
            page.click("text=Save")

            # Step 9: Change Currency to USD
            page.click("#currencyText")
            page.wait_for_selector("select#currency-select", timeout=5000)
            page.select_option("select#currency-select", value="USD")
            page.click("#currencyWrapper .save-btn", timeout=5000)

            # Step 10: Click Sign In (first time)
            page.click("text=Sign In", timeout=5000)

        

            # Step 11: Click Home
            page.click("a:has-text('Home')", timeout=5000)

            # Step 12: Search for "toys"
            page.wait_for_selector("input#searchInputHome", timeout=3000)
            page.fill("input#searchInputHome", "toys")
            page.click("button#btnSearchHome")
            page.wait_for_load_state("networkidle")

            # Step 13: Click Sign In again
            page.click("text=Sign In", timeout=5000)

            # Step 14: Click Get Quote again
            with context.expect_page(timeout=15000) as new_tab2:
                page.evaluate("document.querySelector('a[href*=\"get-quote\"]')?.click()")
            quote_page2 = new_tab2.value
            quote_page2.wait_for_load_state("domcontentloaded", timeout=15000)
            quote_page2.wait_for_selector("input#nameBLInput", timeout=10000)
            quote_page2.wait_for_load_state("domcontentloaded")

            # Step 15: Repeat Step 3-6
            fill_quote_form(quote_page2)

        except Exception as e:
            print("❌ Exception occurred:", e)
        finally:
            browser.close()

if __name__ == "__main__":
    run()
