import exporter1
import searchpage
import PDP
import Homepage

if __name__ == "__main__":
    
    print("🚀 Running Homepage.py (First Script)...")
    Homepage.run_homepage_script()
    
    print("🚀 Running exporter1.py (First Script)...")
    exporter1.run()

    print("\n🚀 Running searchpage.py (Second Script)...")
    searchpage.run_second_script()


    print("\n🚀 Running Third Script operations...")
    PDP.handle_pdp_page()
    