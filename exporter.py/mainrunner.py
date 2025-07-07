import header
import searchpage
import PDP
import Homepage
import CompanyPage

if __name__ == "__main__":
    
    print("🚀 Running Homepage.py (First Script)...")
    Homepage.run_homepage_script()
    
    print("🚀 Running .py (Second Script)...")
    header.run()

    print("\n🚀 Running searchpage.py (Third Script)...")
    searchpage.run_second_script()


    print("\n🚀 Running PDP.py (Fourth Script)...")
    PDP.handle_pdp_page()
    
    print("\n🚀 Running Company.py (Fifth Script)...")
    CompanyPage.handle_company_page()