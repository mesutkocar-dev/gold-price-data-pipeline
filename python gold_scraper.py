import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime
import os

url = "https://www.google.com/finance/quote/GAU-TRY:TCMB"
headers = {"User-Agent": "Mozilla/5.0"}
dosya_adi = "altin_arsivi.csv"

# Eğer dosya yoksa başlık satırını ekle (Sütun isimleri: Tarih, Saat, Fiyat)
if not os.path.exists(dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write("Tarih;Saat;Fiyat\n")

print("--- Altın Takip Botu Başlatıldı ---")
print(f"Veriler '{dosya_adi}' dosyasına kaydediliyor. Durdurmak için Ctrl+C tuşlarına basabilirsin.\n")

try:
    while True: # Sonsuz döngü: Program açık olduğu sürece çalışır
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        
        bulunan_metin = ""
        for div in soup.find_all("div"):
            if "₺" in div.text and len(div.text) < 20:
                bulunan_metin = div.text
                break

        if bulunan_metin:
            # Veriyi temizleme
            temiz_fiyat = re.findall(r"\d+\.?\d*", bulunan_metin.replace(",", ""))[0]
            
            # Zaman bilgilerini al
            simdi = datetime.now()
            tarih = simdi.strftime("%d.%m.%Y")
            saat = simdi.strftime("%H:%M:%S")
            
            # Dosyaya ekleme moduyla ('a' - append) yaz
            with open(dosya_adi, "a", encoding="utf-8") as f:
                f.write(f"{tarih};{saat};{temiz_fiyat}\n")
            
            print(f"[{saat}] Veri Kaydedildi: {temiz_fiyat} TL")
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Veri bulunamadı, tekrar deneniyor...")

        # Bekleme süresi (60 saniye).
        time.sleep(60)

except KeyboardInterrupt:
    print("\nBot kullanıcı tarafından durduruldu. Veriler güvende!")
except Exception as e:
    print(f"Bir hata oluştu: {e}")