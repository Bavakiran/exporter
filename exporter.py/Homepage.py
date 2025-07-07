from playwright.sync_api import sync_playwright

def run_homepage_script():
    with sync_playwright() as p:

    
        browser = p.chromium.launch(headless=False, slow_mo=400)
        context = browser.new_context(viewport={"width": 1536, "height": 960})
        page = context.new_page()
        
        # Navigate to the page
        page.goto("https://export.indiamart.com/", timeout=50000)
        print("✅ Page loaded successfully.")
        
        # Search product
        page.fill("input#searchInputHome", "ball")
        page.wait_for_selector("button#btnSearchHome", timeout=3000)
        page.click("button#btnSearchHome")
        print("✅ Search product")
        
        # Click the logo 
        page.wait_for_selector("img.logo", timeout=3000)
        page.click("img.logo")
        print("✅ Logo clicked.")
        
        # Click "Get Verified Exporters"
        page.mouse.wheel(0, 300)
        page.locator("a:has-text('Get Verified Exporters')").nth(2).wait_for(timeout=5000)
        page.locator("a:has-text('Get Verified Exporters')").nth(2).click()
        print("✅ 'Get Verified Exporters' link clicked.")
        page.wait_for_selector("img.logo", timeout=3000)
        page.click("img.logo")
        
      # Scroll down slowly and click "Home"
    
        for _ in range(10):  
            page.mouse.wheel(0, 100)  
        page.wait_for_timeout(300)  
        page.get_by_role("link", name="Home", exact=True).click()
        print("✅ Home clicked")
        browser.close()

        
        
       
        


        
        
            
            