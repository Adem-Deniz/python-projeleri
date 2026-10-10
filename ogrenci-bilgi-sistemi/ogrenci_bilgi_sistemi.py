"""Öğrenci Bilgi Sistemi

Konsol üzerinden öğrenci ekleme, silme ve listeleme yapar.
Veriler program çalışırken bellekte tutulur, program kapanınca silinir.
"""

ogrenciler = []

while True:
    print("Ogrenci Bilgi Sistemi'ne Hos Geldiniz!")
    print("Lutfen yapmak istediginiz islemi secin:")
    secim = input("1. Ogrenci Ekle\n2. Ogrenci Sil\n3. Ogrenci Listele\n4. Cikis\nSeciminiz: ")

    if secim == "1":
        ad = input("Ogrencinin Adi: ")
        soyad = input("Ogrencinin Soyadi: ")
        ogrenci_no = input("Ogrenci Numarasi: ")
        ogrenciler.append({"Ad": ad, "Soyad": soyad, "Numara": ogrenci_no})
        print(f"{ad} {soyad} basariyla eklendi.")

    elif secim == "2":
        ogrenci_ismi = input("Silmek istediginiz ogrencinin adini girin: ")
        silindi = False
        for ogrenci in ogrenciler:
            if ogrenci["Ad"] == ogrenci_ismi:
                ogrenciler.remove(ogrenci)
                print(f"{ogrenci_ismi} basariyla silindi.")
                silindi = True
                break

        if not silindi:
            print(f"{ogrenci_ismi} adli ogrenci bulunamadi.")

    elif secim == "3":
        print("Listelenecek ogrenciyi secin:")
        print("1. Tum Ogrenciler\n2. Belirli Bir Ogrenci")
        liste_secim = input("Seciminiz: ")

        if liste_secim == "1":
            if not ogrenciler:
                print("Kayitli ogrenci yok.")
            else:
                for ogrenci in ogrenciler:
                    print(f"Ad: {ogrenci['Ad']}\nSoyad: {ogrenci['Soyad']}\nNumara: {ogrenci['Numara']}\n")

        elif liste_secim == "2":
            ogrenci_ismi = input("Listelenecek ogrencinin adini girin: ")
            bulundu = False
            for ogrenci in ogrenciler:
                if ogrenci["Ad"] == ogrenci_ismi:
                    print(f"Ad: {ogrenci['Ad']}\nSoyad: {ogrenci['Soyad']}\nNumara: {ogrenci['Numara']}\n")
                    bulundu = True
                    break

            if not bulundu:
                print(f"{ogrenci_ismi} adli ogrenci bulunamadi.")

        else:
            print("Gecersiz listeleme secenegi.")

    elif secim == "4":
        print("Sistemden cikiliyor...")
        break

    else:
        print("Gecersiz secim. Lutfen 1-4 arasinda bir deger girin.")
