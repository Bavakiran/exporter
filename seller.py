from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()

    # Step 1: Open URL
    page.goto("https://seller.indiamart.com/", timeout=60000)

    # Step 2: Login Flow
    page.fill("input#mobNo", "9971305703")
    page.click("button.login_btn")
    page.get_by_text("Sign in with Password").nth(1).click(force=True)
    page.fill("input#usr_password", "12345678")
    page.click("input#signWP")
    page.wait_for_timeout(3000)

    # Step 3: Navigate to Manage Products Tab
    page.click("li#Manageproduct_tab")

    # Step 4: Handle Popup by Clicking on Cross Icon
    try:
        # Wait for the popup to appear
        page.wait_for_selector("button.popup-close-imcrp", timeout=10000)
        
        # Click the cross icon to close the popup
        page.click("button.popup-close-imcrp")
        print("Popup closed successfully.")
    except Exception as e:
        print("Popup not found or couldn't close:", e)

    # Additional steps if needed
    # ...

    context.close()
    browser.close()

# Run the script
with sync_playwright() as playwright:
    run(playwright)

