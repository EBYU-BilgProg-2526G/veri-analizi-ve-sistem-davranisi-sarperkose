[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/6GHEcYuJ)
# Python ile Mühendislik Veri Analizi  
## NumPy ve Matplotlib Kullanarak Temel Sinyal İşleme

### Ders: Bilgisayar Programlama  
### Bölüm: Elektrik-Elektronik Mühendisliği

---

## Ödevin Amacı

Bu ödevin amacı, Python kullanarak:

- Sayısal veriyi dosyadan okumayı
- NumPy ile temel mühendislik hesapları yapmayı
- Basit bir filtreleme yöntemi uygulamayı
- Matplotlib ile akademik kalitede grafik üretmeyi

öğrenmektir.

Bu ödevde **hazır kütüphanelerle doğrudan çözüm yapılması değil**,  
**algoritmik düşünme ve kod yazma becerisi** hedeflenmektedir.

---

## Proje Yapısı

```
assignment/
├─ README.md
├─ main.py
├─ src/
│  ├─ io_utils.py
│  ├─ analysis.py
│  ├─ signal_tools.py
│  └─ plotting.py
├─ data/
│  └─ sample_signal.csv
└─ report/
   ├─ report.md
   └─ figures/
```

---

## Kullanılmasına İzin Verilen Kütüphaneler

- `numpy`
- `csv`
- `matplotlib`

`pandas`, hazır filtre fonksiyonları veya ileri seviye kütüphaneler **kullanılmayacaktır**.

---

## Görevler

### **Görev 1 — Veri Okuma**
`data/sample_signal.csv` dosyasında iki sütun bulunmaktadır:

```
t,x
```

- `t`: zaman (saniye)
- `x`: sinyal genliği

Yapılacaklar:
- CSV dosyasını **csv modülü** kullanarak okuyunuz.
- Zaman ve sinyal değerlerini iki ayrı vektör olarak elde ediniz.

---

### **Görev 2 — Temel Analiz**
Sinyal için aşağıdaki değerleri hesaplayınız:

- Ortalama
- Standart sapma
- RMS (root mean square)
- Minimum ve maksimum değer

Yapılacaklar:
- Hesaplamaları **NumPy** kullanarak yapınız.
- Sonuçları ekrana yazdırınız.
- Aynı değerleri `report/report.md` dosyasına ekleyiniz.

---

### **Görev 3 — Örnekleme Frekansı**
Zaman vektörünü kullanarak:

fs = 1 / Δt

formülü ile örnekleme frekansını hesaplayınız.

Yapılacaklar:
- Ardışık iki zaman örneği arasındaki farkı kullanınız.
- Sonucu Hz cinsinden yazdırınız.

---

### **Görev 4 — Basit Filtreleme**
Sinyale **hareketli ortalama filtresi** uygulayınız.

Yapılacaklar:
- Pencere uzunluğu serbesttir (ör. 5, 10).
- Filtre algoritmasını **kendiniz yazınız**.
- Filtrelenmiş sinyali yeni bir vektör olarak elde ediniz.

---

### **Görev 5 — Grafik Çizimi**
Ham ve filtrelenmiş sinyali aynı grafikte çiziniz.

Grafik kuralları:
- Eksen isimleri olmalı
- Başlık olmalı
- Legend (açıklama) olmalı
- Grid açık olmalı

Grafiği:
```
report/figures/time_signal.png
```
adıyla kaydediniz.

---