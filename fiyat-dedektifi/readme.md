# Fiyat Dedektifi (Price Detector)

Fiyat Dedektifi is a Python-based price detection tool that scrapes product prices from various Turkish e-commerce websites and calculates statistical price values (minimum, average, and maximum) for each product. It utilizes both requests and Selenium for web scraping, ensuring efficient data retrieval even from dynamic content sites.

## İçindekiler

- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Dosya Yapısı](#dosya-yapısı)
- [Giriş ve Çıkış](#giriş-ve-çıkış)
- [Örnek](#örnek)
- [Katkıda Bulunanlar](#katkıda-bulunanlar)

## Kurulum

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:

- `pandas`
- `requests`
- `beautifulsoup4`
- `selenium`
- `webdriver_manager`
- `openpyxl` (Excel dosyası için)

### Kurulum Adımları

1. Python ve pip'in sisteminizde yüklü olduğundan emin olun.
2. Projeyi klonlayın veya indirin:
   ```bash
   git clone https://github.com/isikmuhamm/ceporjin-eticaret-fiyat-yonetimi.git
   cd ceporjin-eticaret-fiyat-yonetimi/fiyat-dedektifi
   ```
3. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas requests beautifulsoup4 selenium webdriver_manager openpyxl
   ```

## Kullanım

Projeyi kullanmak için `fiyat_dedektifi.py` dosyasını çalıştırmanız yeterlidir:

```bash
python fiyat_dedektifi.py
```

Bu script, `urunler.xlsx` dosyasındaki ürünleri okuyacak, belirtilen e-ticaret sitelerinden fiyatları toplayacak ve sonuçları `output` klasörüne ve `urunler_sonuc.xlsx` dosyasına kaydedecektir.

## Dosya Yapısı

```
fiyat-dedektifi/
│
├── connection.py
├── scrapper.py
├── scrapper_hb.py
├── fiyat_dedektifi.py
├── urunler.xlsx
└── output/
    └── (metin dosyaları)
```

## Giriş ve Çıkış

### Giriş Dosyası

`urunler.xlsx`:
- **Urun_Adi**: Ürün adı
- **Urun_Kodu**: Ürün kodu

### Çıkış Dosyası

- `output/`: Her ürün için metin dosyaları içerir.
- `urunler_sonuc.xlsx`: Her e-ticaret sitesinin minimum, ortalama ve maksimum fiyat bilgilerini içerir.

## Örnek

### Giriş Dosyası Örneği (`urunler.xlsx`)

| Urun_Adi        | Urun_Kodu |
|------------------|-----------|
| Ürün A           | A001      |
| Ürün B           | B002      |

### Çıkış Dosyası Örneği

#### `output/A001.txt`

```
Ürün Kodu: A001
Ürün Adı: Ürün A

Amazon Sonuçları:
Ürün A: 100 TL
Ürün A: 110 TL

N11 Sonuçları:
Ürün A: 105 TL

...

```

#### `urunler_sonuc.xlsx`

| Urun_Adi | Amazon Min | Amazon Avg | Amazon Max | N11 Min | N11 Avg | N11 Max |
|----------|------------|------------|------------|---------|---------|---------|
| Ürün A   | 100        | 105        | 110        | 105     | 105     | 105     |


## Geliştirme

Bu projeyi geliştirerek daha fazla site ekleyebilir veya yazılımın stabilitesini artırabilirsiniz. Herhangi bir geliştirme için iletişime geçmekten çekinmeyin!

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır.