import pandas as pd

# Fiyat indirim oranlarını belirleyen fonksiyon
def calculate_new_price_and_discount(row):
    stok_adedi = row['Stok_Adedi']
    satis_adedi = row['Satis_Adedi']
    satis_orani = row['Satis_Orani'] 
    satis_fiyat = row['Satis_Fiyat']

    #Satis_Orani = Satis_Adedi / (Satis_Adedi + Stok_Adedi) 
    #Formuluyle excelde yoksa burada da hesaplayabilirsiniz.
    
    # Satış ve stok bilgisi eksik veya negatifse fiyatı değiştirme
    if pd.isna(stok_adedi) or pd.isna(satis_adedi) or pd.isna(satis_orani) or stok_adedi < 0 or satis_adedi < 0:
        discount = 0  # Fiyatı sabit tut, indirim %0

    # Sıfır stoklu ürünler (stok = 0)
    if stok_adedi == 0:
        discount = 0  # Fiyatı sabit tut, indirim %0

    # Az stoklu ve düşük satış oranı (Stok <= 3 ve Satış Oranı < 0.34)
    if stok_adedi <= 3 and satis_orani < 0.34:
        discount = 0.10  # %10 indirim
        
    # Az stoklu ve yüksek satış oranı (Stok <= 3 ve Satış Oranı >= 0.3)
    elif stok_adedi <= 3 and satis_orani >= 0.3:
        discount = 0.05  # %5 indirim
        
    # Normal stoklu ve düşük satış oranı (Stok 4-9 ve Satış Oranı < 0.3)
    elif 4 <= stok_adedi <= 9 and satis_orani < 0.3:
        discount = 0.15  # %15 indirim
        
    # Normal stoklu ve iyi satış oranı (Stok 4-9 ve Satış Oranı >= 0.3)
    elif 4 <= stok_adedi <= 9 and satis_orani >= 0.3 and satis_orani <= 0.6:
        discount = 0.10  # %10 indirim
        
    # Normal stoklu ve yüksek satış oranı (Stok 4-9 ve Satış Oranı >= 0.3)
    elif 4 <= stok_adedi <= 9 and satis_orani >= 0.6:
        discount = 0.05  # %5 indirim
        
    # Çok stoklu ve düşük satış oranı (Stok >= 10 ve Satış Oranı < 0.2)
    elif stok_adedi >= 10 and satis_orani < 0.2:
        discount = 0.30 # %30 indirim
        
    # Çok stoklu ve iyi satış oranı (Stok >= 10 ve 0.5 >= Satış Oranı >= 0.3)
    elif stok_adedi >= 10 and satis_orani >= 0.2 and satis_orani <= 0.5:
        discount = 0.20  # %20 indirim

    # Çok stoklu ve yüksek satış oranı (Stok >= 10 ve Satış Oranı >= 0.5)
    elif stok_adedi >= 10 and satis_orani >= 0.5:
        discount = 0.10  # %10 indirim

    else: discount = 0 # Diğer durumlarda indirim yapma
    new_price = satis_fiyat * (1-discount)
    return new_price, discount

# Excel dosyasını okuyun
df = pd.read_excel('urun_satis_adetleri_oranlari_stoklari.xlsx')

# Yeni fiyatları ve indirim oranlarını hesaplayın
df['Yeni_Fiyat'], df['Yapilan_Indirim'] = zip(*df.apply(calculate_new_price_and_discount, axis=1))

# Sonuçları yeni bir Excel dosyasına kaydedin
df.to_excel('yeni_satis_fiyatlari.xlsx', index=False)
