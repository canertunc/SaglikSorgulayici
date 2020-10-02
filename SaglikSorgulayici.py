import os

menu = """
[1] Şeker Hastalığı Ölçümü
[2] Obezite Hastalığı Ölçümü
[3] Tansiyon Sorgulama 
[4] Nabız Sorgulama
[Q] Çıkış

"""

acliktokluk = """

Açım diyorsanız  : 'açım' yazmanız gerekli!
Tokum diyorsanız : 'tokum' yazmanız gerekli!

"""

tansiyonölcümü = """

[1] Büyük Tansiyon Sorgulama
[2] Küçük Tansiyon Sorgulama

"""


def seker():
    print(acliktokluk)

    durum = input("Açlık Durumunu Belirtiniz: ")
    if durum == "açım" or durum == "Açım":

        ölcüm = float(input("Ölçümleriniz kaç mg\dl: "))

        if ölcüm >= 50 and ölcüm <= 70:
            print("Sonucunuz sizin 'Hipoglisemi' olduğunuzu gösteriyor. ")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

        elif ölcüm >= 71 and ölcüm <= 100:
            print("Sonucunuz sizin 'Normal' olduğunuzu gösteriyor. ")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")


        elif ölcüm >= 101 and ölcüm <= 125:
            print("Sonucunuz sizin 'Gizli Şeker' olduğunuzu gösteriyor. ")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")


        elif ölcüm >= 126 and ölcüm <= 10000:
            print("Sonucunuz sizin 'Diyabet' olduğunuzu gösteriyor. ")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

        else:
            print("Lütfen ölçülen değerinizin doğru girdiğinize emin olunuz!")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

    elif durum == "tokum" or durum == "Tokum":
        ölcüm = float(input("Ölçümleriniz kaç mg\dl: "))

        if ölcüm >= 100 and ölcüm <= 140:
            print("Sonucunuz sizin 'Normal' olduğunuzu gösteriyor. ")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

        elif ölcüm >= 141 and ölcüm <= 200:
            print("Sonucunuz sizin 'Gizli Şeker' olduğunuzu gösteriyor. ")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")


        elif ölcüm >= 201 and ölcüm <= 10000:
            print("Sonucunuz sizin 'Diyabet' olduğunuzu gösteriyor. ")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

        else:
            print("Lütfen ölçülen değerinizin doğru girdiğinize emin olunuz!")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

    else:
        print("Hatalı tuşlama yaptınız")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

def tansiyon():
    büyüktansiyon = float(input("Büyük tansiyon ölçümünüz: "))
    kücüktansiyon = float(input("Küçük tansiyon ölçümünüz: "))

    print(tansiyonölcümü)
    tansiyonsoru = input("Lütfen bir seçim yapınız! ")

    if tansiyonsoru == "1":
        if büyüktansiyon >= 10 and büyüktansiyon <= 13.5:
            print("Büyük tansiyonunuz normal seviyede!")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")
        else:
            print("Büyük tansiyonunuz anormal seviyede!")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")
    elif tansiyonsoru == "2":
        if kücüktansiyon >= 6 and kücüktansiyon <= 8.5:
            print("Küçük tansiyonunuz normal seviyede!")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")
        else:
            print("Küçük tansiyonunuz anormal seviyede!")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")
    else:
        print("Hatalı tuşlama yaptınız!")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")


def obezite():
    kilo = float(input("Ağırlığınız kg cinsinden: "))
    boy  = float(input("Boyunuz cm cinsinden: "))
    boy2 = boy * 1 / 100
    endeks = kilo / boy2 ** 2
    print("Vücut kitle Endeksiniz:", endeks)

    if endeks <= 19.9:
        print("Ölçümleriniz 'zayıf' olduğunuzu gösteriyor!")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

    elif endeks >= 20 and endeks <= 24.9:
        print("Ölçümleriniz 'normal' olduğunuzu gösteriyor!")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

    elif endeks >= 25 and endeks <= 29.9:
        print("Ölçümleriniz 'kilolu' olduğunuzu gösteriyor!")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

    elif endeks >= 30 and endeks <= 34.9:
        print("Ölçümleriniz 'obez' olduğunuzu gösteriyor!")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

    elif endeks >= 35 and endeks <= 39.9:
        print("Ölçümleriniz 'tip 2 obez' olduğunuzu gösteriyor!")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

    elif endeks >= 40 and endeks <= 49.9:
        print("Ölçümleriniz 'morbid obez' olduğunuzu gösteriyor!")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

    elif endeks >= 50:
        print("Ölçümleriniz 'süper obez' olduğunuzu gösteriyor!")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

    else:
        print("Lütfen değerlerinizi doğru girdiğinize emin olunuz!")
        input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

def nabiz():
    cinsiyet = input("Cinsiyetiniz nedir?: ")
    if cinsiyet == "Erkek" or cinsiyet == "erkek":
        sporcu = input("Uzun zamandır spor yapıyorsanız 'evet' yapmıyorsanız 'hayır' yazmalısınız!: ")
        if sporcu == "hayır" or sporcu == "Hayır":
            yas = float(input("Yaşınız?: "))
            if yas == 1:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 80 and nabizsoru <= 160:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 161 or nabizsoru <= 79:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
            
            elif yas >= 2 and yas <= 4:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 80 and nabizsoru <= 120:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 121 or nabizsoru <= 79:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                        
            elif yas >= 5 and yas <= 6:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 75 and nabizsoru <= 115:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 116 or nabizsoru <= 74:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
        
            elif yas >= 7 and yas <= 8:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 70 and nabizsoru <= 110:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 111 or nabizsoru <= 69:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
            
            elif yas >= 9 and yas <= 10:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 70 and nabizsoru <= 110:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 111 or nabizsoru <= 79:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            elif yas >= 11 and yas <= 12:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 65 and nabizsoru <= 105:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 106 or nabizsoru <= 64:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
            

            elif yas >= 13 and yas <= 14:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 60 and nabizsoru <= 100:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 101 or nabizsoru <= 59:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            elif yas >= 15 and yas <= 16:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 55 and nabizsoru <= 95:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 96 or nabizsoru <= 54:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            elif yas == 17:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 50 and nabizsoru <= 90:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 91 or nabizsoru <= 49:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
            
            elif yas >= 18:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 60 and nabizsoru <= 100:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 101 or nabizsoru <= 59:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            else:
                print("Hatalı değer girdiniz!")
                input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

        elif sporcu == "evet" or sporcu == "Evet":
            nabizsoru = float(input("Nabız değeriniz nedir?: "))
            if nabizsoru >= 45 and nabizsoru <= 100:
                print("Nabız değeri 'normal' seviyededir!")
                input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
            elif nabizsoru >= 101 or nabizsoru <= 44:
                print("Nabız değeri 'anormal' seviyededir!")
                input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

        else:
            print("Hatalı kelime kullandınız!")
            input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")







    elif cinsiyet == "Kız" or cinsiyet == "kız":
        sporcu = input("Uzun zamandır spor yapıyorsanız 'evet' yapmıyorsanız 'hayır' yazmalısınız!: ")
        if sporcu == "hayır" or sporcu == "Hayır":
            yas = float(input("Yaşınız?: "))
            if yas == 1:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 80 and nabizsoru <= 160:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 161 or nabizsoru <= 79:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            if yas >= 2 and yas <= 4:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 80 and nabizsoru <= 120:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 121 or nabizsoru <= 79:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            if yas >= 5 and yas <= 6:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 75 and nabizsoru <= 115:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 116 or nabizsoru <= 74:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            if yas >= 7 and yas <= 8:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 70 and nabizsoru <= 110:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 111 or nabizsoru <= 69:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            if yas >= 9 and yas <= 10:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 70 and nabizsoru <= 110:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 111 or nabizsoru <= 79:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            if yas >= 11 and yas <= 12:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 70 and nabizsoru <= 110:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 111 or nabizsoru <= 59:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            if yas >= 13 and yas <= 14:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 65 and nabizsoru <= 105:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 106 or nabizsoru <= 64:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            if yas >= 15 and yas <= 16:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 60 and nabizsoru <= 100:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 101 or nabizsoru <= 59:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            if yas == 17:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 55 and nabizsoru <= 95:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 96 or nabizsoru <= 54:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            if yas >= 18:
                nabizsoru = float(input("Nabız değeriniz nedir?: "))
                if nabizsoru >= 60 and nabizsoru <= 100:
                    print("Nabız değeri 'normal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                elif nabizsoru >= 101 or nabizsoru <= 59:
                    print("Nabız değeri 'anormal' seviyededir!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
                else:
                    print("Hatalı değer girdiniz!")
                    input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

            else:
                print("Hatalı değer girdiniz!")
                input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

        elif sporcu == "evet" or sporcu == "Evet":
            nabizsoru = float(input("Nabız değeriniz nedir?: "))
            if nabizsoru >= 45 and nabizsoru <= 100:
                print("Nabız değeri 'normal' seviyededir!")
                input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
            elif nabizsoru >= 101 or nabizsoru <= 44:
                print("Nabız değeri 'anormal' seviyededir!")
                input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")

        else:
            print("Hatalı kelime kullandınız!")
            input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")
        
    else:
        print("Hatalı kelime kullandınız!")
        input("Ana menüye dönmek için 'enter' tuşuna basmalısınız!")



def main():
    while True:
        os.system("cls")
        
        isim = input("Merhaba, isim ve soyisiminiz nedir: ")
        print("Hoşgeldiniz", isim)

        print(menu)
        secim = input("Lütfen bir seçim yapınız: ")

        if secim == "1":
            seker()

        elif secim == "2":
            obezite()

        elif secim == "3":
            tansiyon()

        elif secim == "4":
            nabiz()

        elif secim == "Q" or secim == "q":
            quit()

        else:
            print("Hatalı tuşlama yaptınız")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

main()

