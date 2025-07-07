from playwright.sync_api import sync_playwright

def run():
    print("🚀 Script started")
    with sync_playwright() as p:
        browser = None
        context = None
        try:
            browser = p.chromium.launch(headless=False, channel="chrome", slow_mo=500)
            context = browser.new_context(viewport={"width": 1366, "height": 768})
            page = context.new_page()

            # Step 1: Open website
            page.goto("https://seller.indiamart.com/")
            print("🌐 Opened IndiaMART seller portal")

            # Step 2: Enter mobile number
            page.fill("#mobNo", "1435463454")
            print("📲 Entered mobile number")

            # Step 3: Click 'Start Selling'
            page.get_by_role("button", name="Start Selling").click()
            print("➡️ Clicked 'Start Selling'")

            # Step 4: Enter password
            page.wait_for_selector("#passwordbtn1", timeout=5000)
            page.click("#passwordbtn1")
            page.fill("input[type='password']", "desktoplms123")
            print("🔐 Entered password")

            # Step 5: Sign in
            page.click("#signWP")
            page.wait_for_timeout(3000)

            # Optional: check for login error
            if page.locator("text=Invalid credentials").is_visible():
                print("❌ Login failed: Invalid credentials")
                return

            print("✅ Login successful")

            # Navigate to BuyLeads
            page.wait_for_selector("a:has-text('BuyLeads')", timeout=10000)
            page.click("a:has-text('BuyLeads')")
            print("✅ Landed on BL page")

            # Debug: confirm page state
            print("📄 Page title:", page.title())
            print("📍 URL:", page.url)

            # Initial click on Contact Buyer Now
            page.wait_for_selector("div.btnCBN[title='Click to view Buyer details']", timeout=10000)
            page.click("div.btnCBN[title='Click to view Buyer details']")
            print("✅ Clicked 'Contact Buyer Now'")

            # Wait and count Buy Now buttons
            page.wait_for_selector("button.buy-btn:has-text('Buy Now')", timeout=10000)
            button_count = page.locator("button.buy-btn:has-text('Buy Now')").count()
            print(f"🔎 Found {button_count} 'Buy Now' buttons")

            for i in range(button_count):
                print(f"\n➡️ Starting cycle for 'Buy Now' button {i + 1} of {button_count}")

                # 📝 Extract <h2> title
                try:
                    page.wait_for_selector("h2", timeout=5000)
                    h2_text = page.locator("h2").nth(0).inner_text()
                    print(f"📝 BuyLead Title: {h2_text.strip()}")
                except Exception as e:
                    print(f"⚠️ Could not extract <h2> title: {e}")

                # Click "Contact Buyer Now" via JS
                try:
                    page.wait_for_timeout(1000)
                    page.wait_for_selector("div.btnCBN[title='Click to view Buyer details']", timeout=10000)
                    page.evaluate("document.querySelector('div.btnCBN[title=\"Click to view Buyer details\"]').click()")
                except Exception as e:
                    print(f"❌ Failed to click 'Contact Buyer Now': {e}")
                    break

                # Click the Buy Now button
                try:
                    page.wait_for_selector("button.buy-btn:has-text('Buy Now')", timeout=10000)
                    buy_now_buttons = page.locator("button.buy-btn:has-text('Buy Now')")
                    buy_now_buttons.nth(i).wait_for(state="visible", timeout=5000)
                    buy_now_buttons.nth(i).click()
                    print(f"✅ Clicked 'Buy Now' button {i + 1}")
                    page.wait_for_timeout(2000)
                except Exception as e:
                    print(f"❌ Failed to click 'Buy Now' button {i + 1}: {e}")
                    continue

                # Go back to BuyLeads
                page.go_back()
                page.wait_for_load_state("load")
                page.wait_for_timeout(2000)

        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")
        
            browser.close()
            print("✅ Browser closed successfully")
        except Exception as close_error:
                    print(f"⚠️ Failed to close browser: {close_error}")

if __name__ == "__main__":
    run()
