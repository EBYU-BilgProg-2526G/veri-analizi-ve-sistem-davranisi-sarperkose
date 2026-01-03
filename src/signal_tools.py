# -*- coding: utf-8 -*-
"""
Basit sinyal işleme fonksiyonları
"""

def moving_average(x, window_size):
    """
    Hareketli ortalama filtresi

    Parametreler:
        x           : sinyal vektörü
        window_size : pencere uzunluğu (int)

    Dönen:
        y : filtrelenmiş sinyal
    """
    # TODO:
    # 1. her örnek için pencereyi belirle
    # 2. pencere içindeki ortalamayı hesapla
    # 3. sonucu yeni bir listeye yaz
    pass

#yapılan:

import numpy as np
from verileri_okuma1 import verileri_oku 

dosya_adi = 'sample_signal.csv'
df = verileri_oku(dosya_adi)
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
