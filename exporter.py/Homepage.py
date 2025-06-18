from playwright.sync_api import sync_playwright

def run_homepage_script():
    with sync_playwright() as p:

    
        browser = p.chromium.launch(headless=False, slow_mo=400)
        context = browser.new_context(viewport={"width": 1536, "height": 960})
        page = context.new_page()
        
        # Step 1: Navigate to the page
        page.goto("https://export.indiamart.com/", timeout=50000)
        print("✅ Page loaded successfully.")
        
        # Step 2: Fill the search input
        page.fill("input#searchInputHome", "ball")
        print("✅ Search term entered.")
        
        # Step 3: Click the search button
        page.wait_for_selector("button#btnSearchHome", timeout=3000)
        page.click("button#btnSearchHome")
        print("✅ Search button clicked.")
        
        # Step 4: Click the logo (if necessary)
        page.wait_for_selector("img.logo", timeout=3000)
        page.click("img.logo")
        print("✅ Logo clicked.")
        
        # Step 5: Scroll down
        page.mouse.wheel(0, 300)
        print("✅ Page scrolled down.")
        
        # Step 6: Click "Get Verified Exporters"
        page.locator("a:has-text('Get Verified Exporters')").nth(2).wait_for(timeout=5000)
        page.locator("a:has-text('Get Verified Exporters')").nth(2).click()
        print("✅ 'Get Verified Exporters' link clicked.")
        
        # Step 7: Click the logo (if necessary)
        page.wait_for_selector("img.logo", timeout=3000)
        page.click("img.logo")
        print("✅ Logo clicked.")
        
        # Step 8: Scroll down slowly and click "Home"
        for _ in range(10):  # Adjust the range for more or less scrolling
            page.mouse.wheel(0, 100)  # Scroll down by 100 pixels
            page.wait_for_timeout(300)  # Wait for 300 milliseconds between scrolls
        
        # Click the "Home" link at the bottom
        page.locator('a.clrBlk').wait_for(timeout=5000)
        page.locator('a.clrBlk').click()
        print("✅ 'Home' link clicked.")

        browser.close()

        
        
       
        


        
        
            
            