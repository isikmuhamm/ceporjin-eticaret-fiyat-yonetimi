import requests
from bs4 import BeautifulSoup
import scrapper_hb

# Genel headers değişkeni
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept-Language': 'tr-TR,tr;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# Amazon çalışıyor
def search_amazon(search_term): 
    url = f"https://www.amazon.com.tr/s?k={search_term}&s=price-asc-rank"
    
    response = requests.get(url, headers=headers)
    print(f"Amazon Connection Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print("Amazon Connection Request failed.")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    if soup: print("Amazon Connection Page content loaded.")

    products = []
    print(f"Found {len(soup.find_all("span", class_="a-size-base-plus a-color-base a-text-normal"))} products.")

    for item in soup.find_all("span", class_="a-size-base-plus a-color-base a-text-normal")[:30]:
        product_name = item.get_text()
        price_whole = item.find_next("span", class_="a-price-whole")
        price_decimal = item.find_next("span", class_="a-price-fraction")
        if price_whole and price_decimal:
            price = f"{price_whole.get_text()}{price_decimal.get_text()} TL"
            products.append((product_name, price))
    
    return products



def search_n11(search_term):
    url = f"https://www.n11.com/arama?q={search_term.replace(' ', '+')}&srt=PRICE_LOW"
    
    response = requests.get(url, headers=headers)
    print(f"N11 Connection Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print("N11 Connection Request failed.")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    if soup: print("N11 Connection Page content loaded.")

    products = []
    items = soup.find_all("div", class_="pro")
    print(f"Found {len(items)} products.")
    
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


def search_trendyol(search_term):
    url = f"https://www.trendyol.com/sr?q={search_term}&sst=PRICE_BY_ASC"
    
    response = requests.get(url, headers=headers)
    print(f"Trendyol Connection Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print("Trendyol Connection Request failed.")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    if soup: print("Trendyol Connection Page content loaded.")
    
    products = []
    print(f"Found {len(soup.find_all("h3", class_="prdct-desc-cntnr-ttl-w"))} products.")

    for item in soup.find_all("h3", class_="prdct-desc-cntnr-ttl-w")[:30]:
        product_name = item.get_text()
        price = item.find_next("div", class_="prc-box-dscntd")
        if price:
            products.append((product_name, price.get_text()))
    
    return products


def search_pazarama(search_term):
    url = f"https://www.pazarama.com/arama?q={search_term.replace(' ', '%20')}&siralama=artan-fiyat"
    
    response = requests.get(url, headers=headers)
    print(f"Pazarama Connection Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print("Pazarama Connection Request failed.")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    if soup: print("Pazarama Connection Page content loaded.")
    
    products = []
    print(f"Found {len(soup.find_all("div", class_="product-card"))} products.")

    for item in soup.find_all("div", class_="product-card")[:30]:
        product_name = item.find("div", class_="line-clamp-2 text-gray-600 h-8 text-xs leading-4 mb-1.5").get_text(strip=True)
        
        price = item.find("div", class_="leading-tight text-blue-500 font-semibold text-huge") or \
                item.find("div", class_="leading-tight font-semibold text-huge text-gray-600") or \
                item.find("div", class_="leading-tight font-semibold text-huge text-error")
        
        if price:
            price_text = price.get_text(strip=True)
            products.append((product_name, price_text))
    
    return products


def search_ciceksepeti(search_term):
    url = f"https://www.ciceksepeti.com/arama?choice=1&orderby=3&query={search_term}"
    
    response = requests.get(url, headers=headers)
    print(f"Çiçeksepeti Connection Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print("Çiçeksepeti Connection Request failed.")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Çiçeksepeti Connection Page content loaded.")
    
    products = []
    print(f"Found {len(soup.find_all("p", class_="products__item-title"))} products.")
    
    for item in soup.find_all("p", class_="products__item-title")[:30]:
        product_name = item.get_text()
        price_integer = item.find_next("span", class_="price__integer-value")
        price_decimal = item.find_next("span", class_="price__decimal-value-with-currency")
        if price_integer and price_decimal:
            price = f"{price_integer.get_text()},{price_decimal.get_text()}"
            products.append((product_name, price))
    
    return products


def get_results(search_term):
    results = {
        'Amazon': search_amazon(search_term),
        'N11': search_n11(search_term),
        'Hepsiburada': scrapper_hb.search_hepsiburada(search_term),
        'Trendyol': search_trendyol(search_term),
        'Pazarama': search_pazarama(search_term),
        'Çiçeksepeti': search_ciceksepeti(search_term)
    }
    return results