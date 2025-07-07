from playwright.sync_api import sync_playwright
import time

def handle_company_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(viewport={"width": 1536, "height": 960})
        page = context.new_page()

        try:
            # Step 1: Navigate to the search page URL
            page.goto("https://export.indiamart.com/")
            print("✅ Landed successfully")
            
            # Step 2: Search for "security guard services"
            page.fill("input#searchInputHome", "security guard services")
            page.wait_for_selector("button#btnSearchHome", timeout=3000)
            page.click("button#btnSearchHome")
            page.wait_for_selector("a.lne2txt.ofh.lh1-1.mr15.new_mobile_card_cname", timeout=5000)
            page.locator("a.lne2txt.ofh.lh1-1.mr15.new_mobile_card_cname").nth(1).click()
            print("✅ Landed on company page")
            
            # Step 3: Contact Supplier 1
            page.click("span:has-text('contact supplier')")
            page.wait_for_selector('#frEmInputDiv', timeout=7000)
            page.fill("#frEmInputDiv input", "johndoe123@temp-mail.org")
            page.click('input[onclick="loginSubmit(event,true)"]')
            page.fill('textarea[placeholder="Additional details about your requirement..."]', "hi hello")
            page.click('input[type="submit"][onclick="reqDetailSubmit(event)"]', timeout=5000)
            time.sleep(2)
            page.click('input[type="submit"][onclick="userEnrichmentSubmit(event)"]', timeout=5000)
            page.locator('svg[width="22"][height="22"]').nth(2).click(timeout=7000)
            print("✅ Requirement1 Submitted successfully")

            # Step 4: Switch between tabs
            page.locator('a:has-text("Our Products")').click()
            time.sleep(1)
            page.locator('a[onclick*="scrollToSection(\'aboutUs\')"]').click()
            time.sleep(1)
            page.locator('a[onclick*="scrollToSection(\'factsheet\')"]').click()
            time.sleep(1)
            page.locator('a[onclick*="scrollToSection(\'contactSection\')"]').click()
            time.sleep(1)
            page.evaluate("window.scrollTo(0, 0);")
            print("✅ Switched between different tabs")
            
            # Step 5: Explore "Our Products"
            page.locator('span:has-text("More Products ")').nth(0).click() 
            page.wait_for_selector("#showMoreCat", timeout=10000)
            page.locator("#showMoreCat").nth(0).scroll_into_view_if_needed()
            page.locator("#showMoreCat").nth(0).click()
            print("✅ Clicked on 'Show More Categories'")

            # Scroll and click on Share options
            page.evaluate("window.scrollTo(0, 300);")
            
            # Facebook share
            page.click('a.icon[href^="https://www.facebook.com/sharer.php"]', timeout=5000)
            page.wait_for_load_state('load')
            page.go_back()
            print("✅ Clicked on Facebook share")

            # LinkedIn share
            page.locator('a.icon[href^="https://www.linkedin.com/cws/share"]').scroll_into_view_if_needed()
            page.click('a.icon[href^="https://www.linkedin.com/cws/share"]', timeout=5000)
            page.wait_for_load_state('load')
            page.go_back()
            print("✅ Clicked on LinkedIn share")

            # Twitter share
            page.locator('a.icon[href^="https://twitter.com/share"]').scroll_into_view_if_needed()
            page.click('a.icon[href^="https://twitter.com/share"]', timeout=5000)
            page.wait_for_load_state('load')
            page.go_back()
            print("✅ Clicked on Twitter share")

            # Contact supplier
            page.evaluate("window.scrollTo(0, 300);")
            page.locator("span:has-text('contact supplier')").nth(1).click()
            page.fill('textarea[placeholder="Additional details about your requirement..."]', "hi hello")
            page.click('input[type="submit"][onclick="reqDetailSubmit(event)"]', timeout=5000)
            page.click('input[type="submit"][onclick="userEnrichmentSubmit(event)"]', timeout=5000)
            page.locator('svg[width="22"][height="22"]').nth(2).click(timeout=7000)
            print("✅ Requirement2 Submitted successfully")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    handle_company_page()