# Python Projelerim

Python öğrenirken yazdığım küçük konsol uygulamaları. Her proje kendi klasöründe, tek bir `.py` dosyası olarak durur.

## Projeler

| Proje | Açıklama | Öğrendiklerim |
|-------|----------|---------------|
| [Hesap Makinesi](hesap-makinesi/) | Dört işlem, üs, mod ve karekök hesaplar | `if/elif`, `try/except`, sıfıra bölme kontrolü |
| [Sayı Tahmin Oyunu](sayi-tahmin-oyunu/) | 1-10 arası sayıyı 5 hakta bulmaya çalışırsın | `random`, `while` döngüsü, girdi doğrulama |
| [Asal Sayı Bulma](asal-sayi-bulma/) | İki sayı arasındaki asal sayıları listeler | İç içe döngüler, fonksiyonlar |
| [Öğrenci Bilgi Sistemi](ogrenci-bilgi-sistemi/) | Öğrenci ekleme, silme ve listeleme | Liste, sözlük, menü döngüsü |
| [Çalışan Yönetim Sistemi](calisan-yonetim-sistemi/) | Bölümlere göre çalışan ekleme, güncelleme, silme | Sözlük, `isdigit()` ile doğrulama |
| [İkramiye Takip](ikramiye-takip/) | İkramiye ortalamasına göre çalışan düzeyi hesaplar | Fonksiyonlar, dosya okuma/yazma, hata yönetimi |
| [Ders Geçme Hesaplama](ders-gecme-hesaplama/) | Vize ve final notlarından ortalama hesaplar, dersi geçip geçmediğini söyler | Sözlük, demet (tuple), girdi doğrulama |

## Nasıl çalıştırılır?

Bilgisayarında [Python 3](https://www.python.org/downloads/) kurulu olmalı. Ek bir kütüphane gerekmez.

```bash
git clone https://github.com/Adem-Deniz/python-projeleri.git
cd python-projeleri
python hesap-makinesi/hesap_makinesi.py
```

Başka bir projeyi çalıştırmak için dosya yolunu değiştirmen yeterli. Örneğin:

```bash
python sayi-tahmin-oyunu/sayi_tahmin_oyunu.py
```

Windows'ta `python` çalışmazsa `py` komutunu dene.

> **Not:** İkramiye Takip programı çalışırken aynı klasörde `calisanlar.txt` ve `ikramiyeler.txt` dosyalarını oluşturur. Bu dosyalar `.gitignore` ile GitHub'a yüklenmez.

## Geliştirme planım

- [ ] Projeleri fonksiyonlara bölmek (öğrenci ve çalışan sistemleri)
- [ ] Verileri JSON dosyasına kaydetmek
- [ ] Sınıflar (OOP) ile yeniden yazmak
- [ ] Asal sayı bulmayı daha verimli yapmak (kareköke kadar kontrol)
- [ ] SQLite veritabanına geçmek
- [ ] Flask ile web arayüzü eklemek

## Hakkımda

Bilgisayar mühendisliği öğrencisiyim. Python öğreniyorum, ilerleyen zamanda web geliştirme ve yazılım proje yönetimi alanlarında çalışmak istiyorum.
