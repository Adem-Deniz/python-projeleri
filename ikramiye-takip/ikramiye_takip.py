"""İkramiye Takip Sistemi

Çalışanların yaz ve kış ikramiyelerini dosyaya kaydeder, ortalamaya göre
çalışan düzeyini (iyi / orta / normal) hesaplar ve sonucu başka bir dosyaya yazar.

Çalışma sırasında oluşan dosyalar:
    calisanlar.txt     -> girilen ham veriler
    ikramiyeler.txt    -> hesaplanan düzeyler
"""

IYI_ESIK = 7000
ORTA_ESIK = 5000


def sayi_al(mesaj):
    """Kullanıcıdan sadece rakamlardan oluşan bir değer alır."""
    while True:
        deger = input(mesaj).strip()
        if deger.isdigit():
            return deger
        print("Lütfen sadece rakam girin!")


def ikramiye_gir():
    isim = input("çalışan isim: ").strip()
    soyisim = input("çalışan soyisim: ").strip()
    ikramiye1 = sayi_al("yaz ikramiyesi: ")
    ikramiye2 = sayi_al("kış ikramiyesi: ")

    with open("calisanlar.txt", "a", encoding="utf-8") as file:
        file.write(f"{isim} {soyisim}:{ikramiye1},{ikramiye2}\n")


def ort_ikramiye(satir):
    satir = satir.strip()  # Satır sonundaki \n ve boşlukları temizler
    if not satir:
        return None

    try:
        liste = satir.split(":")
        calisan = liste[0]
        ikramiyeler = liste[1].split(",")

        ikram1 = int(ikramiyeler[0])
        ikram2 = int(ikramiyeler[1])
    except (IndexError, ValueError):
        # Bozuk satır: programı çökertmek yerine atla
        return None

    ortalama = (ikram1 + ikram2) / 2

    if ortalama >= IYI_ESIK:
        duzey = "iyi çalışan"
    elif ortalama >= ORTA_ESIK:
        duzey = "orta çalışan"
    else:
        duzey = "kötü/normal çalışan"

    return f"{calisan}:{duzey} (Ortalama: {ortalama:.1f})"


def ikramiye_oku():
    print("****************")
    try:
        with open("calisanlar.txt", "r", encoding="utf-8") as file:
            for satir in file:
                sonuc = ort_ikramiye(satir)
                if sonuc:
                    print(sonuc)
    except FileNotFoundError:
        print("Henüz kaydedilmiş çalışan dosyası yok.")
    print("****************")


def ikramiye_kaydet():
    try:
        with open("calisanlar.txt", "r", encoding="utf-8") as file:
            sonuclar = []
            for satir in file:
                sonuc = ort_ikramiye(satir)
                if sonuc:
                    sonuclar.append(sonuc + "\n")

        with open("ikramiyeler.txt", "w", encoding="utf-8") as file2:
            file2.writelines(sonuclar)

        print("İkramiye düzeyleri 'ikramiyeler.txt' dosyasına başarıyla kaydedildi.")
    except FileNotFoundError:
        print("Okunacak 'calisanlar.txt' dosyası bulunamadı.")


while True:
    print("\n******* MENU *******")
    islemler = input("1- İkramiye gir\n2- İkramiye oku\n3- İkramiye kaydet\n4- Çıkış\nSeçiminiz: ")

    if islemler == "1":
        ikramiye_gir()
    elif islemler == "2":
        ikramiye_oku()
    elif islemler == "3":
        ikramiye_kaydet()
    elif islemler == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Lütfen (1, 2, 3, 4) değerlerinden birini giriniz.")
