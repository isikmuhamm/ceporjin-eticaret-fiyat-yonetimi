import pandas as pd
import time
import random
import os
from scrapper import get_results

# Excel dosyasını oku
input_file = 'fiyat-dedektifi/urunler.xlsx'  # Excel dosyasının adı
df = pd.read_excel(input_file)

# Çıktı klasörünü oluştur
output_dir = 'fiyat-dedektifi/output'
os.makedirs(output_dir, exist_ok=True)

# Fiyatları hesaplamak için bir fonksiyon
def calculate_prices(products):
    prices = []
    for price in products:
        try:
            # Fiyat stringini temizle: TL birimini kaldır, binlik ayıracı noktaları sil, ondalık ayıracı virgülleri noktaya çevir
            clean_price = price[1].replace(' TL', '').replace('.', '').replace(',', '.').replace('\xa0', '').strip()
            
            # Eğer fiyat binlik ayıracı içeriyorsa ve noktadan önce 3 karakter varsa, sadece bu noktayı sil
            if clean_price.count('.') > 1:
                parts = clean_price.split('.')
                clean_price = parts[0] + ''.join(parts[1:])

            prices.append(float(clean_price))
        except (ValueError, IndexError) as e:
            # Dönüştürme işlemi başarısız olursa, hatayı atla
            continue

    # Eğer geçerli fiyatlar varsa, min, ortalama ve max değerleri döndür
    if prices:
        return min(prices), sum(prices) / len(prices), max(prices)
    
    # Eğer geçerli fiyat yoksa None döndür
    return None, None, None


# Her ürünü işle
for index, row in df.iterrows():
    product_name = row['Urun_Adi']
    product_code = row['Urun_Kodu']

    # Rastgele bekleme süresi (10-30 saniye)
    wait_time = random.randint(5, 15)
    print(f"{product_name} için {wait_time} saniye bekleniyor...")
    time.sleep(wait_time)

    # Her site için arama yap
    results = get_results(product_name)
    
    # Çıktıyı bir dosyaya yaz
    output_file = os.path.join(output_dir, f"{product_code}.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Ürün Kodu: {product_code}\nÜrün Adı: {product_name}\n\n")
        for site, products in results.items():
            f.write(f"{site} Sonuçları:\n")
            for product_name, price in products:
                f.write(f"{product_name}: {price}\n")
            f.write("\n")

    # Fiyatları hesapla
    site_prices = {}
    for site, products in results.items():
        min_price, avg_price, max_price = calculate_prices(products)
        site_prices[site] = {
            'Min': min_price,
            'Avg': avg_price,
            'Max': max_price
        }

    # Sonuçları DataFrame'e ekle
    for site, prices in site_prices.items():
        df.at[index, f"{site} Min"] = prices['Min']
        df.at[index, f"{site} Avg"] = prices['Avg']
        df.at[index, f"{site} Max"] = prices['Max']

# Güncellenmiş veriyi yeni bir Excel dosyasına kaydet
output_excel_file = 'fiyat-dedektifi/urunler_sonuc.xlsx'
df.to_excel(output_excel_file, index=False)

print("İşlem tamamlandı. Sonuçlar 'output' klasörüne ve 'urunler_sonuc.xlsx' dosyasına kaydedildi.")
