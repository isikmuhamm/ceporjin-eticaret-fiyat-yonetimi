from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument("referer=https://www.google.com/")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def wait_for_page_load(driver, timeout=5, cloudflare_timeout=20):

    try:
        # Sayfanın tamamen yüklenmesini bekle
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        
        # Cloudflare doğrulama ekranını kontrol et
        if "Checking your browser" in driver.page_source or "Cloudflare" in driver.page_source:
            print("Cloudflare doğrulama ekranı algılandı, bekleniyor...")
            WebDriverWait(driver, cloudflare_timeout).until(
                lambda d: "Checking your browser" not in d.page_source and "Cloudflare" not in d.page_source
            )
            print("Cloudflare doğrulama ekranı geçildi.")
    
    except Exception as e:
        print(f"Page load timeout veya Cloudflare doğrulama hatası: {e}")
