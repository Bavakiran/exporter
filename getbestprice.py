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

# Step 6: Scroll to the bottom and submit requirements again (only if the form was filled)
                if form_filled:
                    print("➡ Submitting additional requirements...")
                    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    page.wait_for_timeout(2000)

                    try:
                        page.locator("button:has-text('Submit Requirement')").nth(1).click(force=True)
                        print("✅ Successfully clicked the second 'Submit Requirement' button.")
                        
                        # Enter quantity
                        print("➡ Entering quantity...")
                        page.fill('input.quantBx', "1")
                        print("✅ Quantity entered.")

                        # Select unit
                        print("➡ Selecting quantity unit...")
                        page.locator("li:has-text('carton')").click()
                        print("✅ Quantity unit selected.")

                        # Select material
                        print("➡ Selecting material...")
                        page.click("text=Metal (Die Cast)")
                        print("✅ Material selected.")

                        # Select product type
                        print("➡ Selecting product type...")
                        page.click("text=Pull Back Toy Car")  # Select 'Pull Back Toy Car' option
                        print("✅ Product type selected.")

                        # Click the Submit button
                        print("➡ Submitting form...")
                        page.wait_for_selector("input[value='Next']:not([disabled])", timeout=5000)
                        page.click("input[value='Next']")
                    except Exception as e:
                        print(f"❌ Error in additional requirements: {e}")
                else:
                    print("❌ Skipping additional requirements as form submission was incomplete.")

                # Step 7: Click cross button
                try:
                      # Locate the specific path element and scroll it into view
                    path_element = page.locator("path[d='M10.9998 12.2999L5.8998 7.1999L7.5998 5.4999L12.6998 10.5999L17.7998 5.4999L19.4998 7.1999L14.3998 12.2999L19.4998 17.3999L17.7998 19.0999L12.6998 13.9999L7.5998 19.0999L5.8998 17.3999L10.9998 12.2999Z'][fill='#0F0F10']")
                    path_element.scroll_into_view_if_needed()

                    # Click the path element
                    path_element.click()
                except Exception as e:
                    print(f"❌ Could not close requirements form: {e}")

                # Step 8: Click on "Show More Products"
                try:
                    page.click("text=Show More Products", timeout=5000)
                    print("✅ Clicked on 'Show More Products'.")
                except Exception as e:
                    print(f"❌ Could not click 'Show More Products': {e}")

                # Step 9: Handle "Send OTP" process
                try:
                    page.click("input#passwordbtn1", timeout=5000)
                    print("✅ Clicked on 'Send OTP' button.")
                    page.click("a#signInasDiffUser", timeout=5000)
                    print("✅ Clicked on 'Not On Email?'.")
                    page.fill("input#mobileNumber", "newemail123@temp-mail.org")
                    page.check("input#myCheckbox")
                    page.click("input#submtbtn", timeout=10000)
                    print("✅ Submitted as different user.")
                    page.click("input#passwordbtn1", timeout=5000)
                    print("✅ Sent OTP again.")

                    # Close OTP modal
                    page.locator('svg[width="22"][height="22"]').nth(2).click(timeout=5000)
                    print("✅ Closed OTP modal.")
                except Exception as e:
                    print(f"❌ Error in OTP process: {e}")
