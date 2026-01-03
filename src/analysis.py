# -*- coding: utf-8 -*-
"""
Temel sinyal analiz fonksiyonları
"""

def sampling_rate(t):
    """
    Zaman vektöründen örnekleme frekansını hesaplar

    Parametre:
        t : zaman vektörü

    Dönen:
        fs : örnekleme frekansı (Hz)
    """
    # TODO:
    # 1. ardışık iki zaman örneği arasındaki farkı hesapla
    # 2. fs = 1 / dt 
    pass


#zaman vektörünün örnekleme frekansını hesaplattı


from verileri_okuma1 import verileri_oku 

dosya_adi = 'sample_signal.csv'
df = verileri_oku(dosya_adi)
zaman = df.iloc[:, 0].values
sinyal = df.iloc[:, 1].values 




zaman = df.iloc[:, 0].values
sinyal = df.iloc[:, 1].values 

dt = zaman[1] - zaman[0]
fs = 1 / dt
report_content = f"""
## Örnekleme Bilgileri
- **Ardışık Zaman Farkı (Δt):** {dt:.6f} saniye
- **Örnekleme Frekansı (fs):** {fs:.2f} Hz
"""

print(f"Delta t (Δt): {dt:.6f} s")
print(f"Örnekleme Frekansı (fs): {fs:.2f} Hz")



def basic_stats(x):
    """
    Sinyal için temel istatistikleri hesaplar

    Parametre:
        x : sinyal vektörü

    Dönen:
        stats (dict):
            mean
            std
            rms
            min
            max
    """
    # TODO:
    # numpy kullanarak gerekli istatistikleri hesapla
    pass

#max, min, ort, sapma, RMS, değerleri hesaplandı 


import numpy as np
import os
# Diğer dosyadan fonksiyonu çağırıyoruz
from verileri_okuma1 import verileri_oku 


dosya_adi = 'sample_signal.csv'
df = verileri_oku(dosya_adi)




if df is not None:
    # iloc[:, 1] ->tüm 2. sütunları seçmemi sağlar
    sinyal = df.iloc[:, 1].values 


    ortalama = np.mean(sinyal)
    std_sapma = np.std(sinyal)
    maks_deger = np.max(sinyal)
    min_deger = np.min(sinyal)
    rms_deger = np.sqrt(np.mean(sinyal**2))
    
    # sonuçları hazırlama ve yazdırma
    print("\n--- ANALİZ SONUÇLARI ---")
    print(f"Ortalama: {ortalama:.4f}")
    print(f"Standart Sapma: {std_sapma:.4f}")
    print(f"RMS: {rms_deger:.4f}")
    print(f"Minimum: {min_deger:.4f}")
    print(f"Maksimum: {maks_deger:.4f}")

    #  markdown raporunu oluşturma
    report_content = f"""# Temel Analiz Raporu

Sinyal verileri üzerinde yapılan temel istatistiksel analiz sonuçları aşağıdadır:

| Parametre | Değer |
|-----------|-------|
| Ortalama | {ortalama:.6f} |
| Standart Sapma | {std_sapma:.6f} |
| RMS | {rms_deger:.6f} |
| Minimum Değer | {min_deger:.6f} |
| Maksimum Değer | {maks_deger:.6f} |
"""

    # klasör kontrolü ve dosyaya yazma
    if not os.path.exists('report'):
        os.makedirs('report')
        print("\n[BİLGİ] 'report' klasörü oluşturuldu.")

    with open('report/report.md', 'w', encoding='utf-8') as f:
        f.write(report_content)
        print("[BİLGİ] 'report/report.md' dosyası başarıyla güncellendi.")
