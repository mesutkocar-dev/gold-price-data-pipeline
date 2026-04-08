# gold-price-data-pipeline
Automated data ingestion pipeline for live gold prices with built-in data cleaning using Regex and BeautifulSoup.(Regex ve BeautifulSoup kullanarak veri temizleme özelliği olan, canlı altın fiyatları için otomatik veri besleme hattı.)
#  Live Gold Price Data Pipeline

[English]
This project is a real-time data ingestion tool that scrapes gold prices from Google Finance and stores them in a structured CSV format for time-series analysis.

[Türkçe]
Bu proje, Google Finans üzerinden anlık altın fiyatlarını çeken ve zaman serisi analizi için yapılandırılmış bir CSV formatında depolayan bir gerçek zamanlı veri toplama aracıdır.

---

##  Key Features | Öne Çıkan Özellikler

- **Real-time Monitoring:** Fetches data every 60 seconds.
- **Data Cleaning:** Uses **Regex** to extract numeric values from messy HTML strings.
- **Automated Logging:** Saves data to `altin_arsivi.csv` with timestamps.
- **Resilient Parsing:** Designed to handle dynamic HTML structures.

- **Gerçek Zamanlı İzleme:** Her 60 saniyede bir veri çeker.
- **Veri Temizleme:** Karmaşık HTML içerisinden sayısal değerleri ayıklamak için **Regex** kullanır.
- **Otomatik Kayıt:** Verileri zaman damgasıyla birlikte `altin_arsivi.csv` dosyasına kaydeder.
- **Esnek Ayrıştırma:** Dinamik HTML yapılarını işleyecek şekilde tasarlanmıştır.

##  Tech Stack | Kullanılan Teknolojiler

- **Language:** Python 3.14
- **Libraries:** BeautifulSoup4, Requests, Regex
- **Data Format:** CSV (Semicolon separated / Noktalı virgül ayırmalı)

##  How to Run | Nasıl Çalıştırılır

1. Clone this repository. / Depoyu bilgisayarınıza indirin.
2. Install dependencies: / Gerekli kütüphaneleri kurun:  
   `pip install requests beautifulsoup4`
3. Run the script: / Kodu çalıştırın:  
   `python web.py`

---
*Developed for Big Data Analytics and Data Science Portfolio.*
