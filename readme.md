# Ceporjin E-ticaret Fiyat Yönetimi

Bu proje, çeşitli e-ticaret sitelerindeki ürünlerin fiyatlarını izlemek ve otomatik indirim programları oluşturmak amacıyla hazırlanmıştır. **Ceporjin E-ticaret Fiyat Yönetimi**, dinamik fiyatlandırma, rekabet analizi ve indirim yönetimi için Python tabanlı bir çözüm sunmaktadır. Bu projeyi kendi e-ticaret sitem [www.ceporjin.com](https://www.ceporjin.com) üzerinde ve pazaryeri hesaplarımda fiyatlandırma yönetimi için aktif olarak kullanmaktayım.

## Proje Bileşenleri

1. **fiyat_dedektifi.py**  
   E-ticaret sitelerindeki ürünlerin fiyatlarını izleyen ve değişiklikleri takip eden ana script. Çeşitli sitelerden fiyatları çekerek karşılaştırmalar yapar.

2. **scrapper.py**  
   Fiyat verilerini almak için N11, Trendyol, Amazon, Çiçeksepeti gibi sitelere istekte bulunan bir scraper. Dinamik sayfaları destekler ve statik HTML ile çalışır.

3. **scrapper_hb.py**  
   Hepsiburada üzerinde dinamik içerik yüklemeleri ve fiyat bilgilerini Selenium kullanarak toplar. Bu script, sayfanın JavaScript ile yüklediği içerikleri algılayabilmektedir.

4. **connection.py**  
   Scriptlerin veri tabanlarıyla veya diğer sistemlerle olan bağlantılarını yöneten yardımcı dosya. Veri akışını düzenler.

5. **Otomatik İndirim Programı**  
   Fiyat değişikliklerini analiz eden ve belirli kurallara dayalı olarak otomatik indirimler planlayan sistem. Hedeflenen fiyat aralıklarında dinamik olarak indirim başlatır.

## Kullanım Alanları

Bu proje, özellikle rakip fiyat izleme ve dinamik fiyat yönetimi yapmak isteyen e-ticaret platformları için tasarlanmıştır. Kendi iş sitem üzerinde de kullanarak ürün fiyatlandırma ve kampanya yönetim süreçlerini optimize etmekteyim.

## Gereksinimler

- Python 3.x
- Selenium
- BeautifulSoup
- requests

## Kurulum ve Kullanım

1. Proje dosyalarını klonlayın:
   ```bash
   git clone https://github.com/ceporjin/eticaret-fiyat-yonetimi.git
   ```
2. Gerekli Python paketlerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. İlgili scriptleri çalıştırın:
   ```bash
   python fiyat-dedektifi/fiyat_dedektifi.py
   python indirim-otomasyonu/otomatik_indirim.py
   ```

## Katkıda Bulunma

Projeye katkıda bulunmak isterseniz, lütfen bir pull request açın veya hataları issue olarak bildirin. Herhangi bir geliştirme için iletişime geçmekten çekinmeyin!

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır.
