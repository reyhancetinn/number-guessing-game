import random

def gizli_sayi_uret():
    while True:
        rakamlar = random.sample(range(10),5)
        if rakamlar[0] != 0:
            return ''.join(map(str,rakamlar))

def tahmin_gecerli_mi(tahmin):
    if not tahmin.isdigit():
        print("Tahmin yalnızca rakamlardan oluşmalı. ")
        return False
    if len(tahmin) != 5:
        print("Tahmin tam olarak 5 basamaklı olmalı.[HATA]")
        return False
    return True

def geri_bildirim(gizli,tahmin):
    sonuc = ""
    for i in range(5):
        if tahmin [i] == gizli[i]:
            sonuc += "+"
        elif tahmin[i] in gizli:
            sonuc += "-"
        else:
            sonuc += "."
    return sonuc

def oyun():
    print("-" * 45)
    print("5 Basamaklı sayı tahmin oyunu")
    print("Her rakam birbirinden farklı.")
    print("İlk rakam sıfır olamaz.")
    print("Her tahminden sonra ipucu alırsın.")
    print("-" * 45)

    gizli_sayi = gizli_sayi_uret()
    deneme = 0

    while True:
        tahmin = input(f"\n Tahmin {deneme + 1}: ")

        if not tahmin_gecerli_mi(tahmin):
            continue


        deneme += 1

        if tahmin == gizli_sayi:
            print(f"\n Doğru bildiniz! Gizli sayı: {gizli_sayi}")
            print(f" {deneme} denemede doğru tahmin ettiniz.")
            break
        else:
            ipucu = geri_bildirim(gizli_sayi,tahmin)
            print(f" Geri Bildirim: {ipucu} ( +: dogru yerde, -: yanlış yerde, .: yok ) ")

if __name__ == '__main__':
    oyun()