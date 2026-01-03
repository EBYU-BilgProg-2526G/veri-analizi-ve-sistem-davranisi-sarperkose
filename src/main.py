"""
Ana çalışma dosyası
Öğrenciler bu dosyayı çalıştıracaktır.
"""

def main():
    # TODO:
    # 1. CSV dosyasını oku
    # 2. örnekleme frekansını hesapla
    # 3. temel istatistikleri yazdır
    # 4. hareketli ortalama filtresi uygula
    # 5. sonucu çizdir
    pass


if __name__ == "__main__":
    main()




#bütün kodların birleşmiş ve olabildiğince sadeleşmiş hali (tek kod sayfasında çalışabilecek hali. Diğer bloklar birbiryle bağlantılı farklı bloklarda çalışabilmektedir)


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os



df = pd.read_csv('sample_signal.csv')

dosya = 'sample_signal.csv'
def verileri_oku(dosya_yolu):
    
    """
    Belirtilen CSV dosyasını okur ve DataFrame olarak döndürür.
    """
    if os.path.exists(dosya_yolu):
        df = pd.read_csv(dosya_yolu)
        print(f"Başarılı: '{dosya_yolu}' dosyası yüklendi.")
        return df
    else:
        print(f"Hata: '{dosya_yolu}' dosyası bulunamadı!")
        return None


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

sinyal = df.iloc[:, 1].values 

def hareketli_ortalama(sinyal, pencere_boyutu=10):
    """
    Sinyaldeki gürültüyü azaltmak için hareketli ortalama filtresi uygular.
    Pencere boyutu ne kadar büyükse sinyal o kadar pürüzsüz olur.
    """
    n = len(sinyal)
    filtrelenmis_sinyal = np.zeros(n) # sonuçları saklamak için bir denklem oluştur
    
    for i in range(n):
        
        baslangic = max(0, i - pencere_boyutu + 1)
        
        #noktaya kadar olan pencere dilimini al
        pencere_dilimi = sinyal[baslangic : i + 1]
        
        #  ortalamasını hesapla ve vektöre ata
        filtrelenmis_sinyal[i] = np.mean(pencere_dilimi)
        
    return filtrelenmis_sinyal

# filtreyi uygula (pencere uzunluğu 10)
x_filtrelenmis = hareketli_ortalama(sinyal, pencere_boyutu=10)

print(f"Filtreleme tamamlandı. Filtrelenmiş vektör boyutu: {len(x_filtrelenmis)}")

def main():
    dosya_adi = 'sample_signal.csv'
    
    
    veri = verileri_oku(dosya_adi)
    
    if veri is None:
        print("Hata: Veri yüklenemedi!")
        return

    try:
        if hasattr(veri, "iloc"):
            zaman = veri.iloc[:, 0].values
            ham_sinyal = veri.iloc[:, 1].values
        else:
            zaman = veri[:, 0]
            ham_sinyal = veri[:, 1]
    except Exception as e:
        print(f"Veri ayrıştırma hatası: {e}")
        return

    # 4. görev filtreleme
    filtrelenmis_sinyal = hareketli_ortalama(ham_sinyal)

    if len(zaman) != len(filtrelenmis_sinyal):
        fark = len(zaman) - len(filtrelenmis_sinyal)
        cizim_zamani = zaman[fark:] # Genellikle pencere kaybı baştan olur
    else:
        cizim_zamani = zaman

    # 5. kısım-grafik
    figure_path = 'report/figures'
    if not os.path.exists(figure_path):
        os.makedirs(figure_path)

    plt.figure(figsize=(12, 6))

    # ham Sinyal
    plt.plot(zaman, ham_sinyal, label='Ham Sinyal', color='gray', alpha=0.5, linestyle='-')
    
    # filtreleme
    plt.plot(cizim_zamani, filtrelenmis_sinyal, label='Filtrelenmiş Sinyal (MA)', color='darkcyan', linewidth=1.5)

    # grafik çizimi
    plt.title('Ham ve Filtrelenmiş Sinyal Karşılaştırması', fontsize=14)
    plt.xlabel('Zaman (s)', fontsize=12)
    plt.ylabel('Genlik', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)

    # kaydetme ve gösterme plt.savefig kullanarak kaydediyorum
    save_path = os.path.join(figure_path, 'time_signal.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Grafik başarıyla kaydedildi: {save_path}")
    
    # plt.show() ile ekranda gösterilebilir

if __name__ == "__main__":
    main()
