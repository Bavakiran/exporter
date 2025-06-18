from playwright.sync_api import sync_playwright

def handle_pdp_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True to run in the background
        page = browser.new_page()

        # Step 1: Navigate to the search page URL
        search_url = "https://export.indiamart.com/search.php?ss=led+bulbs&tags=res:RC3|ktp:N0|stype:attr=1|mtp:G|wc:2|qr_nm:gd|cs:12670|com-cf:nl|ptrs:na|mc:30613|cat:826|qry_typ:P|lang:en|rtn:1-0-0-0-0-8-1|qrd:250617|mrd:250617|prdt:250618"
        page.goto(search_url)

        # Wait for the page to load completely
        page.wait_for_load_state("networkidle")

        # Step 2: Click on the product name
        page.wait_for_selector('p#prdname_2', timeout=60000)
        page.click('p#prdname_2')

        # Step 3: Click on "Get Best Price"
        # Wait for the "Get Best Price" button to appear and click it
        page.wait_for_selector('text="Get Best Price"', timeout=60000)
        page.click('text="Get Best Price"')
        page.click('input.quantBx', timeout=60000)

        print("🚀 Interaction completed successfully!")
        browser.close()

if __name__ == "__main__":
    handle_pdp_page()
