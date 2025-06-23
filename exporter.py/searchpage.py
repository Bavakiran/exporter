from playwright.sync_api import sync_playwright

def run_second_script():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=400)
        context = browser.new_context(viewport={"width": 1536, "height": 960})
        page = context.new_page()

        try:
            # Navigate to the Exportpage from Indiamart Homepage with increased timeout
            page.goto("https://www.indiamart.com/", timeout=20000)
            page.fill("input#search_string", "toys")
            page.click("input#btnSearch")
            page.wait_for_load_state("networkidle")
            print("✅ Landed on Export page from Indiamart Homepage")

            #  Click directly on the specified filters
            filters_to_click = ["Kids Toys", "Baby Toys", "Toy Car"]
            for filter_text in filters_to_click:
                try:
                    print(f"➡ Clicking filter: {filter_text}")
                    page.click(f"text={filter_text}")
                    page.wait_for_timeout(2000)  # Wait after each click
                except Exception as e:
                    print(f"❌ Failed to click filter '{filter_text}': {e}")

            # Clicked and fill the form through "Get Latest Price" button
            get_price_button = page.locator("text=Get Latest Price").first
            if get_price_button.is_visible():
                get_price_button.click()
                page.wait_for_timeout(5000)

                # Fill the form
                try:
                    
                    page.locator('input[type="text"]').nth(3).fill("johndoe123@temp-mail.org")
                    page.click("input[onclick='loginSubmit(event,true)']")
                    page.fill('input.quantBx', "1")
                    page.locator("li:has-text('carton')").click()  
                    page.click("text=Metal (Die Cast)")  
                    page.click("text=Pull Back Toy Car")  
                    page.click("input[value='Next']")
                    
                except Exception as e:
                    print(f"❌ Error during form interaction: {e}")
                try:
                    page.wait_for_selector("textarea[placeholder='Additional details about your requirement...']", timeout=5000)
                    page.fill("textarea[placeholder='Additional details about your requirement...']", "hi hello")
                    page.click("input[onclick='reqDetailSubmit(event)']",timeout=5000)
                    page.click("input[onclick='userEnrichmentSubmit(event)']",timeout=5000)
                    svg_element = page.locator("svg path[d='M10.9998 12.2999L5.8998 7.1999L7.5998 5.4999L12.6998 10.5999L17.7998 5.4999L19.4998 7.1999L14.3998 12.2999L19.4998 17.3999L17.7998 19.0999L12.6998 13.9999L7.5998 19.0999L5.8998 17.3999L10.9998 12.2999Z']").nth(1)
                    svg_element.click()
                    print("✅ Requirement1 Submitted successfully")
                except Exception as e:
                    print(f"❌ Error during additional details submission: {e}")

                # Scroll to the bottom and Click on submit requirements
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                page.wait_for_timeout(2000)  
                submit_button = page.locator("button.cp.clr0.fs18.bdr_n").nth(1)
                submit_button.click()
                page.wait_for_timeout(2000)
                page.fill('input.quantBx', "1")
                page.locator("li:has-text('carton')").click()  
                page.click("text=Metal (Die Cast)")  
                page.click("text=Pull Back Toy Car")  
                page.click("input[value='Next']")
                page.fill("textarea[placeholder='Additional details about your requirement...']", "hi hello")
                page.click("input[onclick='reqDetailSubmit(event)']",timeout=5000)
                page.click("input[onclick='userEnrichmentSubmit(event)']",timeout=5000)
                svg_element = page.locator("svg path[d='M10.9998 12.2999L5.8998 7.1999L7.5998 5.4999L12.6998 10.5999L17.7998 5.4999L19.4998 7.1999L14.3998 12.2999L19.4998 17.3999L17.7998 19.0999L12.6998 13.9999L7.5998 19.0999L5.8998 17.3999L10.9998 12.2999Z']").nth(1)
                svg_element.click()
                print("✅ Requirement2 Submitted successfully")
                
             # Click on "Show More Products"
                try:
                    page.click("text=Show More Products", timeout=5000)
                    print("✅ Clicked on 'Show More Products'.")
                except Exception as e:
                    print(f"❌ Could not click 'Show More Products': {e}")

                # Handle "Send OTP" process
                try:
                    page.click("input#passwordbtn1", timeout=5000)
                    print("✅ Clicked on 'Send OTP' button.")
                    page.click("a#signInasDiffUser", timeout=5000)
                    print("✅ Clicked on Signin as different user")
                    page.fill("input#mobileNumber", "newemail123@temp-mail.org")
                    page.check("input#myCheckbox")
                    page.click("input#submtbtn", timeout=10000)
                    print("✅ signed in  as different user.")
                    page.click("input#passwordbtn1", timeout=5000)
                    print("✅ Sent OTP again.")

                    # Close OTP modal
                    page.locator('svg[width="22"][height="22"]').nth(2).click(timeout=5000)
                    print("✅ Closed OTP modal.")
                except Exception as e:
                    print(f"❌ Error in OTP process: {e}")
                    
            # Scroll down slowly and click "Home"
            for _ in range(10):  
                page.mouse.wheel(0, 100)  
            page.wait_for_timeout(300)  
            page.locator('a.clrBlk').wait_for(timeout=5000)
            page.locator('a.clrBlk').click()
            print("✅ Home")    
            
        except Exception as e:
            print(f"❌ Error occurred: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    run_second_script()