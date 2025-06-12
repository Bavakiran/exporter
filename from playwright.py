from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        try:
            # Launch browser
            browser = p.chromium.launch(headless=False, slow_mo=500)
            context = browser.new_context(viewport={"width": 1536, "height": 960})
            page = context.new_page()
            
            # Go to login page and enter mobile number
            page.goto("https://buyer.indiamart.com/login", timeout=20000)
            page.wait_for_selector("input#mobilemy", timeout=10000)
            page.fill("input#mobilemy", "1212121212")
            page.click("input#signInSubmitButton")
            
            # Wait for OTP page to load
            page.wait_for_timeout(5000)
            
            # Enter product in search box and submit requirement
            page.wait_for_selector("input#prodtitle0101", timeout=10000)
            page.fill("input#prodtitle0101", "ball")
            page.click("input#t0102_submit")
            
            # Enter quantity
            page.wait_for_selector("input#ttxtbx_option1", timeout=10000)
            page.fill("input#ttxtbx_option1", "10")
            page.click("button.submit-button[type='submit']")
            
            # Enter requirement details
            page.wait_for_selector("textarea.slbox.ber-txt", timeout=10000)
            page.fill("textarea.slbox.ber-txt", "hi")
            page.click("input.form-btn[type='submit'][value='Next']")  
            
            # Click on "Manage your requirement" → opens new tab
            page.wait_for_selector("a:has-text('Manage your requirement')", timeout=20000)
            with context.expect_page() as new_page_info:
                page.click("a:has-text('Manage your requirement')")
            new_page = new_page_info.value
            new_page.wait_for_load_state()

            # Login with password on new tab
            new_page.wait_for_selector("input#passwordbtn1", timeout=20000)
            new_page.click("input#login_pass_tab", strict=True)
            new_page.fill("input#passmy", "123456")
            new_page.click("input#submtbtn")

            # Verify requirement card
            new_page.wait_for_selector(".card-body", timeout=15000)
            first_card_text = new_page.inner_text(".card-body:first-child")
            if "ball" in first_card_text.lower():
                print("✅ Verification passed - 'ball' found in the first requirement card")
            else:
                print(f"❌ Verification failed - 'ball' not found in the first card. Card text: {first_card_text}")
            
            new_page.wait_for_timeout(5000)

        except Exception as e:
            print("❌ Exception occurred:", e)

        finally:
            browser.close()

if __name__ == "__main__":
    run()
