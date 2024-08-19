import random

def tas_kagit_makas_mustafa_atakan_yucel():
    print("Taş, Kağıt, Makas Oyunu")
    print("Kurallar: Taş makası kırar, makas kağıdı keser, kağıt taşı sarar.")
    print("Oyunun amacı: İlk iki turu kazanan kişi oyunu kazanır.")

    secenekler = ["taş", "kağıt", "makas"]

    def secim_al():
        while True:
            kullanici_secimi = input("Lütfen 'taş', 'kağıt' veya 'makas' seçin: ").lower()
            if kullanici_secimi in secenekler:
                return kullanici_secimi
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

    def bilgisayar_secimi():
        return random.choice(secenekler)

    def sonuc_belirle(kullanici, bilgisayar):
        if kullanici == bilgisayar:
            return "beraberlik"
        elif (kullanici == "taş" and bilgisayar == "makas") or \
             (kullanici == "makas" and bilgisayar == "kağıt") or \
             (kullanici == "kağıt" and bilgisayar == "taş"):
            return "kullanici"
        else:
            return "bilgisayar"

    while True:
        kullanici_galibiyetleri = 0
        bilgisayar_galibiyetleri = 0

        while kullanici_galibiyetleri < 2 and bilgisayar_galibiyetleri < 2:
            print("\nYeni Tur Başlıyor!")
            kullanici = secim_al()
            bilgisayar = bilgisayar_secimi()
            print(f"Bilgisayarın seçimi: {bilgisayar}")

            tur_sonucu = sonuc_belirle(kullanici, bilgisayar)

            if tur_sonucu == "kullanici":
                kullanici_galibiyetleri += 1
                print("Bu turu kazandınız!")
            elif tur_sonucu == "bilgisayar":
                bilgisayar_galibiyetleri += 1
                print("Bu turu bilgisayar kazandı!")
            else:
                print("Bu tur berabere!")

            print(f"Skor - Siz: {kullanici_galibiyetleri}, Bilgisayar: {bilgisayar_galibiyetleri}")

        if kullanici_galibiyetleri == 2:
            print("Tebrikler, oyunu kazandınız!")
        else:
            print("Bilgisayar oyunu kazandı.")

        devam_et = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        if devam_et != "evet":
            bilgisayar_ister_mi = random.choice(["evet", "hayır"])
            if bilgisayar_ister_mi == "hayır":
                print("Bilgisayar başka bir oyun oynamak istemiyor.")
                break
            else:
                print("Bilgisayar başka bir oyun oynamak istiyor.")
        else:
            print("Yeni oyuna başlıyoruz!")


tas_kagit_makas_mustafa_atakan_yucel()
