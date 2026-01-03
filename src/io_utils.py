# -*- coding: utf-8 -*-
"""
CSV dosyasından sinyal verisi okuma yardımcı fonksiyonları
"""

def load_signal_csv(path):
    """
    CSV formatı:
    t,x
    0.0, 1.23
    0.01, 1.10
    ...

    Parametre:
        path (str): CSV dosya yolu

    Dönen:
        t : zaman vektörü
        x : sinyal vektörü
    """
    # TODO:
    # 1. csv modülünü kullan
    # 2. dosyayı satır satır oku
    # 3. t ve x listelerini doldur
    # 4. numpy array olarak döndür
    pass

#yapılan
import pandas as pd
import os
# Dosya yolunu kendi dosya adınızla değiştirin
# Eğer dosya proje klasöründe değilse tam yolu yazın (Örn: 'C:/Users/Ad/Masaüstü/veri.csv')

df = pd.read_csv('sample_signal.csv')

#print(df.hea1d())#ile ilk 5 satır çalışır


#df['t']# 1. sütunu görmek içim
#df['x']# 2. sütunu görmek için
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

