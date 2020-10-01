import os
menu = """
[1] Şeker Hastalığı Ölçümü
[2] Obezite Hastalığı Ölçümü
[Q] Çıkış

"""

acliktokluk = """
Açım diyorsanız  : 'açım' yazmanız gerekli!
Tokum diyorsanız : 'tokum' yazmanız gerekli!

"""

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

                ölcüm = float(input("Ölçümleriniz kaç mg\dl: "))

                if ölcüm >= 50 and ölcüm <= 70:
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
         

        elif secim == "2":
            obezite()
        
        
        elif secim == "Q" or secim == "q":
            quit()

        else:
            print("Hatalı tuşlama yaptınız")
            input("Ana Menüye dönmek için 'enter' tuşuna basmalısınız!")

main()

