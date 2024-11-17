from bs4 import BeautifulSoup
from connection import wait_for_page_load

def search_amazon(search_term, driver):
    url = f"https://www.amazon.com.tr/s?k={search_term}&s=price-asc-rank"
    
    try:
        driver.get(url)
        wait_for_page_load(driver)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = []
        items = soup.find_all("span", class_="a-size-base-plus a-color-base a-text-normal")
        print(f"Amazon: Found {len(items)} products.")

        for item in items[:30]:
            product_name = item.get_text()
            price_whole = item.find_next("span", class_="a-price-whole")
            price_decimal = item.find_next("span", class_="a-price-fraction")
            if price_whole and price_decimal:
                price = f"{price_whole.get_text()}{price_decimal.get_text()} TL"
                products.append((product_name, price))
        
        return products
    except Exception as e:
        print(f"Amazon error: {e}")
        return []

def search_n11(search_term, driver):
    url = f"https://www.n11.com/arama?q={search_term.replace(' ', '+')}&srt=PRICE_LOW"
    
    try:
        driver.get(url)
        wait_for_page_load(driver)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = []
        items = soup.find_all("div", class_="pro")
        print(f"N11: Found {len(items)} products.")
        
        for item in items[:30]:
            product_name_tag = item.find("h3", class_="productName")
            if product_name_tag:
                product_name = product_name_tag.get_text(strip=True)
            
            price_tag = item.find("span", class_="newPrice cPoint priceEventClick")
            if price_tag:
                price_ins = price_tag.find("ins")
                if price_ins:
                    price = price_ins.get_text(strip=True)
                    products.append((product_name, price))
        
        return products
    except Exception as e:
        print(f"N11 error: {e}")
        return []

def search_trendyol(search_term, driver):
    url = f"https://www.trendyol.com/sr?q={search_term}&sst=PRICE_BY_ASC"
    
    try:
        driver.get(url)
        wait_for_page_load(driver)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = []
        items = soup.find_all("h3", class_="prdct-desc-cntnr-ttl-w")
        print(f"Trendyol: Found {len(items)} products.")

        for item in items[:30]:
            product_name = item.get_text()
            price = item.find_next("div", class_="prc-box-dscntd")
            if price:
                products.append((product_name, price.get_text()))
        
        return products
    except Exception as e:
        print(f"Trendyol error: {e}")
        return []

def search_pazarama(search_term, driver):
    url = f"https://www.pazarama.com/arama?q={search_term.replace(' ', '%20')}&siralama=artan-fiyat"
    
    try:
        driver.get(url)
        wait_for_page_load(driver)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = []
        items = soup.find_all("div", class_="product-card")
        print(f"Pazarama: Found {len(items)} products.")

        for item in items[:30]:
            product_name = item.find("div", class_="line-clamp-2 text-gray-600 h-8 text-xs leading-4 mb-1.5")
            if product_name:
                product_name = product_name.get_text(strip=True)
            
            price = item.find("div", class_="leading-tight text-blue-500 font-semibold text-huge") or \
                    item.find("div", class_="leading-tight font-semibold text-huge text-gray-600") or \
                    item.find("div", class_="leading-tight font-semibold text-huge text-error")
            
            if price and product_name:
                price_text = price.get_text(strip=True)
                products.append((product_name, price_text))
        
        return products
    except Exception as e:
        print(f"Pazarama error: {e}")
        return []

def search_ciceksepeti(search_term, driver):
    url = f"https://www.ciceksepeti.com/arama?query={search_term.replace(' ', '%20')}&qt={search_term.replace(' ', '%20')}&choice=1"
    try:
        driver.get(url)
        wait_for_page_load(driver)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = []

        # Ürün kartlarını bul
        items = soup.find_all("a", attrs={"data-cs-product-box": "true"})
        print(f"Çiçeksepeti: Found {len(items)} products.")
        
        for item in items[:30]:
            product_name = item.find("span", attrs={"data-cs-pb-name": "true"})
            price_tag = item.find("span", attrs={"data-cs-pb-price-text": "true"})

            if product_name and price_tag:
                name = product_name.text.strip()
                price = price_tag.text.strip()
                products.append((name, price))
        
        return products
    except Exception as e:
        print(f"Çiçeksepeti error: {e}")
        return []

def search_hepsiburada(search_term, driver):
    url = f"https://www.hepsiburada.com/ara?q={search_term}&siralama=artanfiyat"
    
    try:
        driver.get(url)
        wait_for_page_load(driver)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        products = []
        items = soup.find_all("li", class_="productListContent-zAP0Y5msy8OHn5z7T_K_")
        print(f"Hepsiburada: Found {len(items)} products.")
        
        for item in items[:30]:
            name_element = item.find("h3", {"data-test-id": "product-card-name"})
            price_element = item.find("div", {"data-test-id": "price-current-price"})

            if name_element and price_element:
                name = name_element.text.strip()
                price = price_element.text.strip()
                products.append((name, price))
        
        return products
    except Exception as e:
        print(f"Hepsiburada error: {e}")
        return []

def get_results(search_term, driver):
   
    try:
        results = {
            'Amazon': search_amazon(search_term, driver),
            'N11': search_n11(search_term, driver),
            'Hepsiburada': search_hepsiburada(search_term, driver),
            'Trendyol': search_trendyol(search_term, driver),
            'Pazarama': search_pazarama(search_term, driver),
            'Çiçeksepeti': search_ciceksepeti(search_term, driver)
        }
        return results
    except Exception as e:
        print(f"Getting results error: {e}")
        return []