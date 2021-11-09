from os import system
class Musteri():
    def __init__(self,ID,PAROLA,ISIM):
        self.isim = ISIM
        self.ID = ID
        self.parola = PAROLA
        self.bakiye = 0


class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self,ID,PAROLA,ISIM):
        self.musteriler.append(Musteri(ID,PAROLA,ISIM))
        print("Kayıt Başarılı!")


def main():
    banka = Banka()
    while True:
        system("cls")
        print("""
        [1] Giriş Yap
        [2] Müşteri Olmak İstiyorum
        """)

        secim = input("işlem: ")

        if secim == "1":
            for i in banka.musteriler:
                ids += [i.id]
                ID = input("ID: ")
                if ID in ids:
                    for musteri in banka.musteriler:
                        if ID == musteri.id: #musteriyi buluyoruz.
                            print("{} hoşgeldiniz.".format(musteri.isim))
                            parola = input("Parolanız: ")
                            if parola == musteri.parola:
                                print("Giriş Başarılı...")
                                while True:
                                    system("cls")
                                    print("""
                                    [1] Bakiye Sorgula
                                    [2] Kendi Hesabıma Para Yatır
                                    [3] Başka Hesaba Para Yatır
                                    [4] Para Çek
                                    [Q] Çıkış
                                    """)
                                    secim2 = input("Seçiminiz: ")

                                    if secim2 == "1":
                                        print("Bakiyeniz: {}".format(musteri.bakiye))
                                        input("Ana menüye dönmek için enter'e basın...")

                                    elif secim2 == "2":
                                        miktar = int(input("Yatırılacak miktar: "))
                                        onay = input("Hesabınıza {} TL para yatırmayı onaylıyor musunuz? (E/H)")
                                        if onay == "E" or onay == "e":
                                            musteri.bakiye += miktar
                                            print("Yatırma işlemi başarılı...")
                                            input("Ana menüye dönmek için enter'e basın...")

                                        if onay == "H" or onay == "h":
                                            print("İşlem iptal edildi...")
                                            input("Ana menüye dönmek için enter'e basın...")

                                        else:
                                            print("Hatalı giriş...")
                                            input("Ana menüye dönmek için enter'e basın...")

                                    elif secim2 == "3":
                                        arananID = input("Müşteri ID: ")
                                        if arananID in ids:
                                            for digerMusteri in banka.musteriler:
                                                if arananID == digerMusteri.id:
                                                    miktar = int(input("Yatırılacak Miktar: "))
                                                    if miktar <= musteri.bakiye:
                                                        onay = input("{} adlı müşterimize {} TL para yatırma işlemini onaylıyor musunuz?(E/H)".format(digerMusteri,miktar))

                                                        if onay == "E" or onay == "e":
                                                            digerMusteri.bakiye += miktar
                                                            musteri.bakiye -= miktar
                                                            print("Para yatırma başarılı...")
                                                            print("Yeni bakiyeniz: {}".format(musteri.bakiye))
                                                            input("Ana menüye dönmek için enter'e basın...")

                                                        elif onay == "H" or onay == "h":
                                                            print("İşlem iptal edildi...")
                                                            input("Ana menüye dönmek için enter'e basın...")
                                                        
                                                    else:
                                                        print("Bakiyeniz yetersiz...")
                                                        input("Ana menüye dönmek için enter'e basın...")

                                        else:
                                            print("Müşteri bulunamadı...")
                                            input("Ana menüye dönmek için enter'e basın...")

                                    elif secim2 == "4":
                                        miktar = int(input("Çekmek istediğiniz miktar: "))
                                        if miktar <= musteri.bakiye:
                                            musteri.bakiye -= miktar
                                            print("Lütfen paranızı alın.\n Yeni bakiyeniz: {}".format(musteri.bakiye))
                                            input("Ana menüye dönmek için enter'e basın...")

                                        else:
                                            print("Bakiyeniz yetersiz...")
                                            input("Ana menüye dönmek için enter'e basın...")

                                    elif secim2 == "q" or secim2 == "Q":
                                        print("Çıkış yapılıyor... Kartınızı alın.")
                                        break

                                    else:
                                        print("Hatalı seçim yaptınız")
                                        





                            










if __name__ == "__main__":
    main()