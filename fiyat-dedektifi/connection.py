import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

# Maksimum tekrar sayısı, bekleme süresi ve diğer ayarlar
MAX_RETRIES = 5
WAIT_TIME = 10
BACKOFF = 5
FORCE_LIST = [500, 502, 503, 504]

# Genel headers değişkeni
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept-Language': 'tr-TR,tr;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

def create_session(
    retries=MAX_RETRIES,
    backoff_factor=BACKOFF,
    status_forcelist=FORCE_LIST,
    timeout=WAIT_TIME,
    session=None
):
    """
    Yeni bir requests.Session nesnesi oluşturur ve otomatik tekrar mekanizması ekler.

    :param retries: Yeniden deneme sayısı.
    :param backoff_factor: Her hatada bekleme süresinin artış faktörü.
    :param status_forcelist: Hangi HTTP durum kodlarında tekrar deneneceği.
    :param timeout: Her istekteki zaman aşımı.
    :param session: Var olan bir session varsa onu kullanma.
    :return: Hazırlanmış requests.Session nesnesi.
    """
    
    # Eğer dışarıdan bir session verilmezse yeni bir session oluştur
    session = session or requests.Session()

    # Retry stratejisini ayarla
    retry_strategy = Retry(
        total=retries,
        status_forcelist=status_forcelist,
        backoff_factor=backoff_factor,
        raise_on_status=False,
        allowed_methods=["HEAD", "GET", "OPTIONS"]  # Hangi HTTP metodlarında tekrar deneme yapılacağı
    )

    # Session'a adaptör ekleyerek retry mekanizmasını tanımla
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount('https://', adapter)
    session.mount('http://', adapter)

    # Timeout'u her istekte kullanmak için session'un get metodunu override ediyoruz
    def request_with_timeout(method, url, **kwargs):
        kwargs.setdefault('timeout', timeout)
        return session.request(method, url, **kwargs)

    # Timeout'u session get ve post metodlarına bağla
    session.get = lambda url, **kwargs: request_with_timeout('GET', url, **kwargs)
    session.post = lambda url, **kwargs: request_with_timeout('POST', url, **kwargs)

    return session

def retry_request(function, *args, retries=MAX_RETRIES, wait=WAIT_TIME):
    """
    Verilen fonksiyonu yeniden denemek için bir wrapper fonksiyonu.

    :param function: Yeniden denenecek fonksiyon.
    :param args: Fonksiyona geçilecek argümanlar.
    :param retries: Yeniden deneme sayısı.
    :param wait: Bekleme süresi.
    :return: Fonksiyon başarılı olursa dönüş değeri, aksi halde boş liste.
    """
    for attempt in range(retries):
        try:
            return function(*args)
        except Exception as e:
            print(f"Hata oluştu: {e}. {attempt + 1}. deneme...")
            time.sleep(wait * (attempt + 1))  # Exponential backoff
    print(f"{retries} denemeden sonra başarısız.")
    return []

# Örnek kullanım
def example_usage():
    session = create_session()
    
    try:
        response = session.get("https://www.example.com")
        print(f"Status Code: {response.status_code}")
        print(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")
