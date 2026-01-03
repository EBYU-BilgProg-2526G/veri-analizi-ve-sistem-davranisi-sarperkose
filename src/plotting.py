# -*- coding: utf-8 -*-
"""
Grafik çizim fonksiyonları
"""

def plot_time(t, x_raw, x_filt, save_path):
    """
    Ham ve filtrelenmiş sinyali zaman domeninde çizer

    Parametreler:
        t        : zaman vektörü
        x_raw   : ham sinyal
        x_filt  : filtrelenmiş sinyal
        save_path : kayıt edilecek dosya yolu
    """
    # TODO:
    # matplotlib kullanarak:
    # - iki sinyali aynı grafikte çiz
    # - eksen isimleri ve başlık ekle
    # - grafiği dosyaya kaydet
    pass

#ham görüntü ve filtrelenmiş görüntü diğer kodlardan alınmıştır
import os
import matplotlib.pyplot as plt


# Modülleri içe aktar
from verileri_okuma1 import verileri_oku 
from görev4 import hareketli_ortalama

def main():
    dosya_adi = 'sample_signal.csv'
    

    veri = verileri_oku(dosya_adi)
    
    if veri is None:
        print("Hata: Veri yüklenemedi!")
        return


    try:
        if hasattr(veri, "iloc"): # Pandas ise
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
        cizim_zamani = zaman[fark:] 
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
