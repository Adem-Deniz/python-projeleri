"""Asal Sayı Bulma

Kullanıcının girdiği iki sayı arasındaki asal sayıları bulur.
Büyük olan sayı aralığa dahil edilir, küçük olan sayı dahil edilmez.
"""

sayi1 = int(input("sayi1 = "))
sayi2 = int(input("sayi2 = "))

liste = []


def asalsayibulma(sayi1, sayi2):
    # 1. DURUM: sayi1 büyükse sayi1'i eksilterek sayi2'ye kadar kontrol et
    if sayi1 > sayi2:
        while sayi1 > sayi2:
            if sayi1 > 1:
                i = 2
                asal_mi = True
                # i değerini sayi1'e kadar büyüterek böleni var mı bakıyoruz
                while i < sayi1:
                    if sayi1 % i == 0:
                        asal_mi = False
                        break
                    i += 1

                # Eğer hiçbir sayıya bölünmediyse asal listesine ekle
                if asal_mi:
                    liste.append(sayi1)

            # Dış döngüdeki sayi1'i 1 azaltıp bir sonraki sayıya geçiyoruz
            sayi1 -= 1

    # 2. DURUM: sayi2 büyükse sayi2'yi eksilterek sayi1'e kadar kontrol et
    if sayi2 > sayi1:
        while sayi2 > sayi1:
            if sayi2 > 1:
                i = 2
                asal_mi = True
                # i değerini sayi2'ye kadar büyüterek böleni var mı bakıyoruz
                while i < sayi2:
                    if sayi2 % i == 0:
                        asal_mi = False
                        break
                    i += 1

                # Eğer hiçbir sayıya bölünmediyse asal listesine ekle
                if asal_mi:
                    liste.append(sayi2)

            # Dış döngüdeki sayi2'yi 1 azaltıp bir sonraki sayıya geçiyoruz
            sayi2 -= 1

    print(liste)


# Fonksiyonu çağırıyoruz
asalsayibulma(sayi1, sayi2)
