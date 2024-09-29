from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import random

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=200,150")
    chrome_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 100)}.0.{random.randint(4000, 5000)}.0 Safari/537.36")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def wait_for_js_load(driver):
    return driver.execute_script("return document.readyState") == "complete"

def search_hepsiburada(search_term):
    driver = setup_driver()
    url = f"https://www.hepsiburada.com/ara?q={search_term}&siralama=artanfiyat"
    
    try:
        driver.get(url)
        print("Hepsiburada Connection Page content loading.")
        
        # Sayfanın tamamen yüklenmesini bekle
        WebDriverWait(driver, 30).until(wait_for_js_load)
        print("Hepsiburada Connection Page content loaded.")
        
        # Sayfanın HTML içeriğini al
        page_source = driver.page_source
        
        # BeautifulSoup ile HTML'i parse et
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Ürünleri bul
        product_items = soup.find_all("li", class_="productListContent-zAP0Y5msy8OHn5z7T_K_")
        print(f"Found {len(product_items)} products.")
        products = []
        for item in product_items[:30]:  # İlk 30 ürünü al
            name_element = item.find("h3", {"data-test-id": "product-card-name"})
            price_element = item.find("div", {"data-test-id": "price-current-price"})
            
            if name_element and price_element:
                name = name_element.text.strip()
                price = price_element.text.strip()
                products.append((name, price))
        
        return products
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return []
    
    finally:
        driver.quit()