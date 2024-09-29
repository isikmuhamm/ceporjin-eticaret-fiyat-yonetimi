### README.md

# Otomatik İndirim Programı

Bu Python scripti, bir Excel dosyasında listelenen ürünlerin stok, satış ve satış oranı bilgilerini kullanarak dinamik bir fiyatlandırma algoritması uygular. İndirilen Excel dosyasındaki her bir ürün için yeni bir fiyat hesaplanır ve yapılan indirim oranı ile birlikte sonuçlar Excel dosyasına kaydedilir.

## Algoritma

Script, ürünlerin stok ve satış oranı bilgilerini temel alarak fiyatlarda otomatik indirim yapar. İndirim stratejisi stok adedi ve satış oranı kombinasyonlarına dayalıdır:

1. **Stok <= 3 ve Satış Oranı < 0.34**: %10 indirim
2. **Stok <= 3 ve Satış Oranı >= 0.34**: %5 indirim
3. **Stok 4-9 ve Satış Oranı < 0.3**: %15 indirim
4. **Stok 4-9 ve Satış Oranı 0.3 - 0.6**: %10 indirim
5. **Stok 4-9 ve Satış Oranı >= 0.6**: %5 indirim
6. **Stok >= 10 ve Satış Oranı < 0.2**: %30 indirim
7. **Stok >= 10 ve Satış Oranı 0.2 - 0.5**: %20 indirim
8. **Stok >= 10 ve Satış Oranı >= 0.5**: %10 indirim
9. **Stok 0 olan ürünler ve diğer durumlar**: İndirim yapılmaz.

Kendi indirim stratejilerinizi kodu düzenleyerek ekleyebilirsiniz.

### Satış Oranı:
- Satış oranı şu şekilde hesaplanır:  
  `Satış Oranı = Satış Adedi / (Satış Adedi + Stok Adedi)`
- Bu oran, ürünün ne kadar satıldığını stok durumuna göre normalize eder.

## Gereksinimler

Bu programı çalıştırmak için aşağıdaki yazılım gereksinimlerini karşılamanız gerekmektedir:

- Python 3.x
- Pandas kütüphanesi

Pandas kütüphanesini kurmak için şu komutu kullanabilirsiniz:

```bash
pip install pandas
```

## Kurulum

1. Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) Python'u indirip kurun.
2. Bu repo içerisindeki dosyaları indirin veya klonlayın.
3. İlgili Excel dosyasını (`urun_satis_adetleri_oranlari_stoklari.xlsx`) script ile aynı klasöre koyun.

## Kullanım

1. Python scriptini çalıştırmadan önce Excel dosyasının yapısının şu başlıklara sahip olduğundan emin olun:
   - `Urun_Kodu`: Ürünün kodu.
   - `Urun_Adi`: Ürünün adı.
   - `Satis_Fiyat`: Mevcut satış fiyatı.
   - `Satis_Adedi`: Toplam satış adedi.
   - `Satis_Orani`: Satış oranı (eğer yoksa program otomatik hesaplar).
   - `Stok_Adedi`: Mevcut stok miktarı.

2. Scripti çalıştırmak için terminal veya komut satırında şu komutu girin:

```bash
python otomatik_indirim.py
```

3. Script, Excel dosyasındaki ürünler için yeni fiyatları ve yapılan indirimleri hesaplar. Sonuçlar `yeni_satis_fiyatlari.xlsx` dosyasına kaydedilir.

### Örnek Excel Dosyası

| Urun_Kodu | Urun_Adi  | Satis_Fiyat | Satis_Adedi | Satis_Orani | Stok_Adedi |
|-----------|-----------|-------------|-------------|-------------|------------|
| 001       | Ürün A    | 100         | 20          | 0.4         | 5          |
| 002       | Ürün B    | 150         | 0           | 0.0         | 12         |

## Çıktı

Çıktı olarak yeni bir Excel dosyası olan `yeni_satis_fiyatlari.xlsx` oluşturulacaktır. Bu dosyada şu sütunlar bulunur:

- **Yeni_Fiyat**: Hesaplanan yeni fiyat.
- **Yapilan_Indirim**: İndirim oranı (% olarak).

| Urun_Kodu | Urun_Adi  | Satis_Fiyat | Satis_Adedi | Satis_Orani | Stok_Adedi | Yeni_Fiyat | Yapilan_Indirim |
|-----------|-----------|-------------|-------------|-------------|------------|------------|-----------------|
| 001       | Ürün A    | 100         | 20          | 0.4         | 5          | 95         | 0.05            |
| 002       | Ürün B    | 150         | 0           | 0.0         | 12         | 105        | 0.30            |

## Geliştirme

Bu scripti geliştirerek daha fazla dinamik kurallar ekleyebilir veya farklı indirim stratejileri uygulayabilirsiniz. Örneğin, sezonluk ürünler için özel indirimler eklemek ya da satış oranına dayalı farklı metrikler kullanmak mümkün.

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır.