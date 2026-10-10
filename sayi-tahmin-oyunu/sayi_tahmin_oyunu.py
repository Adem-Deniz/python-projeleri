"""Sayı Tahmin Oyunu

Bilgisayar 1 ile 10 arasında bir sayı tutar, oyuncunun 5 tahmin hakkı vardır.
Ne kadar erken bilirse o kadar çok puan alır (kalan hak x 20).
"""

import random

sayi = random.randint(1, 10)
hak = 5
sayac = 0

while hak > 0:
    try:
        tahmin = int(input("1 ile 10 arasında bir sayı tahmin edin: "))
    except ValueError:
        print("Geçersiz bir tahmin girdiniz. Lütfen 1 ile 10 arasında bir sayı girin.")
        continue

    if tahmin < 1 or tahmin > 10:
        print("Lütfen 1 ile 10 arasında bir sayı girin.")
        continue

    sayac += 1

    if tahmin == sayi:
        print(f"Tebrikler! Sayıyı {sayac} denemede doğru tahmin ettiniz.")
        break
    elif tahmin < sayi:
        print("Tahmininiz çok düşük. Daha yüksek bir sayı deneyin.")
    else:
        print("Tahmininiz çok yüksek. Daha düşük bir sayı deneyin.")

    hak -= 1

    if hak == 0:
        print("Tahmin hakkınız kalmadı. Doğru sayı:", sayi)

print("Aldığınız puan:", hak * 20)
