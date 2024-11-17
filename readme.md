# Ceporjin E-ticaret Fiyat Yönetimi (English Explanation Below)

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



----------------------------------------------------------------------------------------------------------------------------



# Ceporjin E-commerce Price Management

This project is designed to track product prices across various e-commerce sites and create automated discount programs. **Ceporjin E-commerce Price Management** provides a Python-based solution for dynamic pricing, competitor analysis, and discount management. I actively use this project for pricing management on my own e-commerce site [www.ceporjin.com](https://www.ceporjin.com) and my marketplace accounts.

## Project Components

1. **fiyat_dedektifi.py**  
   The main script that monitors product prices on e-commerce sites and tracks price changes. It pulls prices from various sites and performs comparisons.

2. **scrapper.py**  
   A scraper that sends requests to sites like N11, Trendyol, Amazon, and Çiçeksepeti to fetch price data. It supports dynamic pages and works with static HTML.

3. **scrapper_hb.py**  
   Collects dynamic content and price information from Hepsiburada using Selenium. This script detects content loaded via JavaScript on the page.

4. **connection.py**  
   A helper file that manages the connection between the scripts and databases or other systems. It organizes data flow.

5. **Automated Discount Program**  
   A system that analyzes price changes and plans automatic discounts based on certain rules. It dynamically initiates discounts within targeted price ranges.

## Use Cases

This project is designed for e-commerce platforms that want to monitor competitor prices and manage dynamic pricing. I also use it on my own business site to optimize product pricing and campaign management processes.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup
- requests

## Setup and Usage

1. Clone the project files:
   ```bash
   git clone https://github.com/ceporjin/eticaret-fiyat-yonetimi.git
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the relevant scripts:
   ```bash
   python fiyat-dedektifi/fiyat_dedektifi.py
   python indirim-otomasyonu/otomatik_indirim.py
   ```

## Contribution

If you'd like to contribute to the project, please open a pull request or report any issues. Don't hesitate to reach out for any developments!

## License

This project is licensed under the MIT License.
