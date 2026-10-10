"""Ders Geçme Hesaplama

Kullanıcıdan aldığı derslerin vize ve final notlarını alır.
Ortalama = vize x %40 + final x %60 olarak hesaplanır.
Bir dersi geçmek için hem final notu hem de ortalama en az 50 olmalıdır.
"""

GECME_NOTU = 50
VIZE_ORANI = 0.4
FINAL_ORANI = 0.6


def not_al(mesaj):
    """Kullanıcıdan 0-100 arasında geçerli bir not alır."""
    while True:
        try:
            deger = float(input(mesaj))
        except ValueError:
            print("Lütfen sayı girin!")
            continue
        if 0 <= deger <= 100:
            return deger
        print("Not 0 ile 100 arasında olmalıdır!")


print("         ------>Derslerinizi gectiniz mi merak mi ediyorsunuz? Hadi ogrenelim!<------")
print("   lutfen ilk once bana hangi dersleri aldiginizi ve bu derslerden kac puan aldiginizi soyleyin.")
print("**************************************************************************************************")

aldiginiz_dersler = {}
while True:
    ders_adi = input("Dersin adini girin (aldiğiniz bütün dersleri girdiğinizde 'q' tusuna basin): ").strip()
    if ders_adi.lower() == 'q':
        break
    if not ders_adi:
        print("Ders adı boş olamaz!")
        continue
    vize = not_al(f"{ders_adi} dersinden aldiginiz vize puanini girin: ")
    final = not_al(f"{ders_adi} dersinden aldiginiz final puanini girin: ")
    aldiginiz_dersler[ders_adi] = (vize, final)

if not aldiginiz_dersler:
    print("Hiç ders girmediniz.")
else:
    print(" ALDIĞINIZ DERSLER VE PUANLAR:\n")
    for ders, (vize, final) in aldiginiz_dersler.items():
        print(f"{ders}: Vize: {vize}, Final: {final}")

    ortalamalar = {}
    for ders, (vize, final) in aldiginiz_dersler.items():
        ortalama = (vize * VIZE_ORANI) + (final * FINAL_ORANI)
        ortalamalar[ders] = ortalama

    print(" ALDIĞINIZ DERSLER VE ORTALAMA PUANLAR:\n")
    for ders, ortalama in ortalamalar.items():
        print(f"{ders}: {ortalama:.1f}")

    for ders, ortalama in ortalamalar.items():
        final_notu = aldiginiz_dersler[ders][1]
        if final_notu >= GECME_NOTU and ortalama >= GECME_NOTU:
            print(f"Tebrikler! {ders} dersini gectiniz.")
        else:
            print(f"Maalesef, {ders} dersini gecemediniz.")
