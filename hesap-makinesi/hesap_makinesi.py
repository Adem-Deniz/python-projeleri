"""Basit Hesap Makinesi

Toplama, çıkarma, çarpma, bölme, üs alma, mod alma ve karekök işlemlerini yapar.
"""

print("Basit Hesap Makinesine Hos Geldiniz!")
print("Lutfen yapmak istediginiz islemi secin:")

islem = input(
    "toplama icin '+' yazin\n"
    "cikarma icin '-' yazin\n"
    "carpma icin '*' yazin\n"
    "bolme icin '/' yazin\n"
    "uslu sayilar icin '^' yazin\n"
    "mod alma icin '%' yazin\n"
    "kok alma icin '√' yazin\n"
)

if islem not in ("+", "-", "*", "/", "^", "%", "√"):
    print("Geçersiz işlem!")
else:
    try:
        sayi1 = float(input("Birinci sayiyi girin: "))
        # Karekök için ikinci sayıya gerek yok
        if islem != "√":
            sayi2 = float(input("Ikinci sayiyi girin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
    else:
        if islem == "+":
            print(sayi1 + sayi2)
        elif islem == "-":
            print(sayi1 - sayi2)
        elif islem == "*":
            print(sayi1 * sayi2)
        elif islem == "/":
            if sayi2 == 0:
                print("Sıfıra bölme yapılamaz!")
            else:
                print(sayi1 / sayi2)
        elif islem == "^":
            print(sayi1 ** sayi2)
        elif islem == "%":
            if sayi2 == 0:
                print("Sıfıra göre mod alınamaz!")
            else:
                print(sayi1 % sayi2)
        elif islem == "√":
            if sayi1 < 0:
                print("Negatif sayının karekökü alınamaz!")
            else:
                print(sayi1 ** 0.5)
