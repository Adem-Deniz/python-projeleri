"""Çalışan Yönetim Sistemi

Konsol üzerinden çalışan ekleme, listeleme, güncelleme ve silme yapar.
Çalışanlar bölümlerine göre kaydedilir. Veriler program kapanınca silinir.
"""

calisanlar = {}

bolumler_dict = {
    "1": "Bilgisayar Muhendisligi",
    "2": "Elektrik-Elektronik Muhendisligi",
    "3": "Makine Muhendisligi",
    "4": "Endustri Muhendisligi",
}


while True:

    print("\n --> SIRKET YONETIM SISTEMINE HOSGELDINIZ <--")
    print("1. Yeni Calisan Ekle")
    print("2. Calisanlari Listele")
    print("3. Calisan Bilgi Guncelle")
    print("4. Calisan Sil")
    print("5. Cikis")

    secim = input("Lutfen yapmak istediginiz islemi secin (1-5): ")

    if secim == "1":
        print("\n--- Calisan Ekleme ---")
        print("Lutfen bolumunuzu seciniz:")

        for anahtar, deger in bolumler_dict.items():
            print(f"{anahtar}. {deger}")
        print("5. Ana Menuye Don")

        bolum_secim = input("Seciminiz: ")

        if bolum_secim in bolumler_dict:
            secilen_bolum = bolumler_dict[bolum_secim]
            print(f"\n{secilen_bolum} departmanina hosgeldiniz.")

            isim = input("Isminiz: ").strip()

            if isim in calisanlar:
                print("Bu isimde bir calisan zaten kayitli!")
                continue

            while True:
                yas_girdisi = input("Yasinizi girin: ").strip()
                if yas_girdisi.isdigit():  # Sadece rakamlardan mi oluşuyor?
                    yas = int(yas_girdisi)
                    break  # Doğru girilirse döngüden çık
                else:
                    print("Lutfen sadece sayisal bir deger girin!")

            while True:
                calisan_numarasi = input("Numaraniz: ").strip()
                if calisan_numarasi.isdigit():  # Sadece rakamlardan mi oluşuyor?
                    break  # Doğru girilirse döngüden çık
                else:
                    print("Lutfen sadece sayisal bir deger girin!")

            # Veriyi sözlüğe kaydet
            calisanlar[isim] = {
                "Yas": yas,
                "Bolum": secilen_bolum,
                "Numara": calisan_numarasi
            }
            print(f"-> {isim} basariyla sisteme eklendi!")

        elif bolum_secim == "5":
            continue

        else:
            print("Gecersiz bolum secimi!")

    elif secim == "2":
        print("\n--- Calisanlar ---")
        if not calisanlar:
            print("Kayitli calisan yok.")
        for isim, bilgiler in calisanlar.items():
            print(f"Isim: {isim}, Yas: {bilgiler['Yas']}, Bolum: {bilgiler['Bolum']}, Numara: {bilgiler['Numara']}")

    elif secim == "3":
        print("\n--- Calisan Bilgi Guncelle ---")
        guncellenecek_isim = input("Bilgilerini guncellemek istediginiz calisanin ismini girin: ").strip()

        if guncellenecek_isim in calisanlar:
            print(f"-> {guncellenecek_isim} bulundu. Yeni bilgileri girin.")

            while True:
                yas_girdisi = input("Yeni yas: ").strip()
                if yas_girdisi.isdigit():
                    yas = int(yas_girdisi)
                    break
                else:
                    print("Lutfen sadece sayisal bir deger girin!")

            while True:
                calisan_numarasi = input("Yeni numara: ").strip()
                if calisan_numarasi.isdigit():
                    break
                else:
                    print("Lutfen sadece sayisal bir deger girin!")

            calisanlar[guncellenecek_isim]["Yas"] = yas
            calisanlar[guncellenecek_isim]["Numara"] = calisan_numarasi
            print(f"-> {guncellenecek_isim} bilgileri basariyla guncellendi!")

        else:
            print("Calisan bulunamadi.")

    elif secim == "4":
        print("Silmek istenen calisanin ismini girin:")
        silinecek_isim = input("Isim: ").strip()

        if silinecek_isim in calisanlar:
            del calisanlar[silinecek_isim]
            print(f"-> {silinecek_isim} basariyla silindi!")
        else:
            print("Calisan bulunamadi.")

    elif secim == "5":
        print("Cikis yapiliyor...")
        break

    else:
        print("Gecersiz secim! Lutfen 1-5 arasinda bir secenek girin.")
