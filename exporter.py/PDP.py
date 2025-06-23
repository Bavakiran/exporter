from playwright.sync_api import sync_playwright
import time  # For additional manual delays if needed

def fill_requirement(page, quantity, option_id, text_option, details):
    """Fills the requirement details and submits the form."""
    page.fill('input.quantBx', quantity) 
    page.click(f'li:has-text("{option_id}")', timeout=5000)
    page.click(f'li:has-text("{text_option}")', timeout=5000)
    page.click('input[type="submit"][value="Next"]', timeout=5000)
    time.sleep(2) 
    page.fill('textarea[placeholder="Additional details about your requirement..."]', details) 
    page.click('input[type="submit"][onclick="reqDetailSubmit(event)"]', timeout=5000)
    time.sleep(2)  
    page.click('input[type="submit"][onclick="userEnrichmentSubmit(event)"]', timeout=5000)
    page.locator('svg[width="22"][height="22"]').nth(1).click(timeout=7000)
    

def handle_pdp_page():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False, slow_mo=500)  
        context = browser.new_context(viewport={"width": 1536, "height": 960})
        page = context.new_page()

        #  Navigate to the search page URL
        search_url = "https://export.indiamart.com/search.php?ss=led+bulbs&tags=res:RC3|ktp:N0|stype:attr=1|mtp:G|wc:2|qr_nm:gd|cs:12670|com-cf:nl|ptrs:na|mc:30613|cat:826|qry_typ:P|lang:en|rtn:1-0-0-0-0-8-1|qrd:250617|mrd:250617|prdt:250618"
        page.goto(search_url)
        print("✅ Landed successfully")

        # Wait for the page to load completely
        page.wait_for_load_state("networkidle")
        time.sleep(2) 

        #  Click on the product name
        page.wait_for_selector('p#prdname_2', timeout=70000)
        page.click('p#prdname_2')
        print("✅ Clicked on product name")
        time.sleep(2)  

        # Click on "Get Best Price"
        page.wait_for_selector('text="Get Best Price"', timeout=70000)
        page.click('text="Get Best Price"')
        print("✅ Clicked on Get Best Price")
        time.sleep(2) 

        # Step 4: Enter Email ID
        container_selector = '#frEmInputDiv'
        page.wait_for_selector(container_selector, timeout=70000)
        email_input_selector = f"{container_selector} input"
        page.fill(email_input_selector, "johndoe123@temp-mail.org")
        time.sleep(2)  
        submit_button_selector = 'input[onclick="loginSubmit(event,true)"]'
        page.wait_for_selector(submit_button_selector, timeout=70000)
        page.click(submit_button_selector)
        time.sleep(2)  

        # Fill requirement 1
        fill_requirement(
            page=page,
            quantity="1",
            option_id="5W",
            text_option="Monthly",
            details="Please provide LED bulbs with high luminosity and energy efficiency."
        )
        print("✅ Requirement1 Submitted successfully")

        # Image Operation
        page.hover('img#prdimgdiv')
        time.sleep(2)  # Wait to observe hover effect
        for img_alt in ["image_1", "image_2", "image_3"]:
            page.wait_for_selector(f'img[alt="{img_alt}"]', timeout=70000)
            page.click(f'img[alt="{img_alt}"]')
            time.sleep(1)  # Wait to observe each click
        print("✅ All images are seen successfully")

        # Fill requirement 2
        page.locator("span#bnCTA_PDP").nth(0).click(timeout=5000)
        print("✅ Clicked on Get Latest Price")
        fill_requirement(
            page=page,
            quantity="2",
            option_id="9W",
            text_option="Sample Only",
            details="high luminosity and energy efficiency."
        )
        print("✅ Requirement2 Submitted successfully")
        
        # Fill requirement 3
        page.locator("span#bnCTA_PDP").nth(1).click(timeout=5000)
        print("✅ Clicked on Send Email")
        fill_requirement(
            page=page,
            quantity="2",
            option_id="10W",
            text_option="Quarterly / Half Yearly / Annual",
            details="Please provide LED bulbs"
        )
        print("✅ Requirement3 Submitted successfully")
        
        # Fill requirement 4
        page.click('span:has-text("Contact Supplier")')
        print("✅ Clicked on Contact  Supplier")
        fill_requirement(
            page=page,
            quantity="3",
            option_id="12W",
            text_option="Quarterly / Half Yearly / Annual",
            details="Please provide LED bulbs"
        )
        print("✅ Requirement4 Submitted successfully")
        
        #Get Products Similar
        
        page.click("img[onclick=\"GATrack('PDP_Photo', 'CTA_Clicked', 'd2615f', 'Product_0', '226833')\"]")
        page.go_back
        page.locator('p#prdname_0').nth(0).click()
        page.go_back
        locator = page.locator('a.lne2txt.ofh.lh1-1.mr15.new_mobile_card_cname')
        locator.first.wait_for(timeout=10000)  
        locator.nth(1).click()
        page.wait_for_load_state("networkidle")
        page.go_back()
        page.click("span#bn_cta_0")
        page.fill('textarea[placeholder="Additional details about your requirement..."]', "Hi helo") 
        page.click('input[type="submit"][onclick="reqDetailSubmit(event)"]', timeout=5000)
        page.click('input[type="submit"][onclick="userEnrichmentSubmit(event)"]', timeout=5000)
        page.locator('svg[width="22"][height="22"]').nth(1).click()
        print("✅ Requirement5 Submitted successfully")
        
        page.click('text="View more"')
        print("✅ Clicked on View More")
        page.mouse.wheel(0, 300)
        page.locator('a.card-items.df.aic.jcsb').nth(1).click(timeout=5000)
        print("✅ Clicked on Browse Related Category")
        page.go_back()
        page.mouse.wheel(0, 1000)  
        time.sleep(2)  
        page.wait_for_selector('button:has-text("Submit Requirement")', timeout=10000)
        page.locator('button:has-text("Submit Requirement")').click()
        print("✅ Clicked 'Submit Requirement' at the bottom of the page")
        fill_requirement(
            page=page,
            quantity="3",
            option_id="12W",
            text_option="Quarterly / Half Yearly / Annual",
            details="Please provide LED bulbs"
        )
        print("✅ Requirement6 Submitted successfully")
        
         # Scroll down slowly and click "Home"
    
        for _ in range(10):  
            page.mouse.wheel(0, 100)  
        page.wait_for_timeout(300)  
        page.locator('a.clrBlk').wait_for(timeout=5000)
        page.locator('a.clrBlk').click()
        print("✅ Home")    
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    handle_pdp_page()
