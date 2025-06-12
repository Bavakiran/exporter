from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser and load saved login state
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="C:/Users/Anmol Goyal/Desktop/Automation/auth.json")
    page = context.new_page()

    # Step 1: Open IndiaMART Directory page
    page.goto("https://dir.indiamart.com/")
    page.wait_for_load_state("load")

    # Step 2: Click "Get Best Price" button from header
    page.click("text=Get Best Price")

  # Step 3: Wait and enter product name
    page.wait_for_selector("#t0901prodtitle", timeout=15000)
    page.fill("#t0901prodtitle", "Jute Bags")

   
  # Step 5: Click Next
    page.click("#t0901_submit")

    # Step 6: Fill in quantity
    page.wait_for_selector("#t0901txtbx_option12", timeout=10000)
    page.fill("#t0901txtbx_option12", "2")

   

    # Step 9: Click Next
    page.click("#t0901_fBtn")

    # Step 10: Click Next again
    page.click("#t0901_submitdiv")

    # Step 11: Click Submit
    page.click("#t0901_submit")

    # Optional: Pause or wait to observe
    page.wait_for_timeout(5000)

    browser.close()

