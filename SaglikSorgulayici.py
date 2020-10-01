import os
menu = """
[1] Şeker Hastalığı Risk Oranı Ölçümü
[Q] Çıkış


"""

acliktokluk = """

Açım diyorsanız  : 'açım' yazmanız gerekli!
Tokum diyorsanız : 'tokum' yazmanız gerekli!



"""

def main():
    while True:
        os.system("cls")
        isim = input("Merhaba, isim ve soyisiminiz nedir: ")

        print("Hoşgeldiniz", isim)


        print(menu)
        secim = input("Lütfen bir seçim yapınız: ")

        if secim == "1":
            print(acliktokluk)

            durum = input("Açlık Durumunu Belirtiniz: ")
            if durum == "açım" or durum == "Açım":


                ölcüm = int(input("Ölçümleriniz kaç mg\dl: "))

                if ölcüm <= 49 or ölcüm >=10001:
                    print("Lütfen ölçülen değerinizin doğru girdiğinize emin olunuz!")
                    input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

                elif ölcüm >= 50 and ölcüm <= 70:
                    print("Sonucunuz sizin 'Hipoglisemi' olduğunuzu gösteriyor. ")
                    input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

                elif ölcüm >= 71 and ölcüm <= 100:
                    print("Sonucunuz sizin 'Normal' olduğunuzu gösteriyor. ")
                    input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")


                elif ölcüm >= 101  and ölcüm <= 125:
                    print("Sonucunuz sizin 'Gizli Şeker' olduğunuzu gösteriyor. ")
                    input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")


                elif ölcüm >= 126 and ölcüm <= 10000:
                    print("Sonucunuz sizin 'Diyabet' olduğunuzu gösteriyor. ")
                    input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

            elif durum == "tokum" or durum == "Tokum":
                ölcüm = int(input("Ölçümleriniz kaç mg\dl: "))

                if ölcüm <= 99 or ölcüm >=10001:
                    print("Lütfen ölçülen değerinizin doğru girdiğinize emin olunuz!")
                    input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

                elif ölcüm >= 100 and ölcüm <= 140:
                    print("Sonucunuz sizin 'Normal' olduğunuzu gösteriyor. ")
                    input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

                elif ölcüm >= 141 and ölcüm <= 200:
                    print("Sonucunuz sizin 'Gizli Şeker' olduğunuzu gösteriyor. ")
                    input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")


                elif ölcüm >= 201 and ölcüm <= 10000:
                    print("Sonucunuz sizin 'Diyabet' olduğunuzu gösteriyor. ")

                    input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

            else:
                print("Hatalı tuşlama yaptınız")
                input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")


        elif secim == "Q" or secim == "q":
            quit()

        else:
            print("Hatalı tuşlama yaptınız")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

main()

