baska_var_mi="e"
toplam_harcanan_ton=0
fazladan_gun=0
tonaj_fatura=0
atik_su_ucreti=0
toplam_fatura=0
gune_eklenen_1 = 0
gune_eklenen_2 = 0
KDV = 0
abone_tipi_adi = " "
konut_abone_sayisi = 0
is_yeri_abone_sayisi = 0
resmi_daire_abone_sayisi= 0
organize_sanayi_abone_sayisi = 0
ilce_tarım_hayvan_sulama_abone_sayisi = 0
tum_abone_sayisi = 0
toplam_ton_konut = 0
toplam_ton_is_yeri = 0
toplam_ton_resmi_daire = 0
toplam_ton_organize_sanayi= 0
toplam_ton_ilce_tarim_hayvan_sulama = 0
toplam_gun_konut= 0
toplam_gun_is_yeri = 0
toplam_gun_resmi_daire = 0
toplam_gun_organize_sanayi = 0
toplam_gun_ilce_tarim_hayvan_sulama = 0
aylik_su_tuketim_50_tondan_fazla_olan_ilce_abone_sayisi = 0
aylik_100_ton_uzeri_veya_500_tlden_fazla = 0
aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_abone_nosu= 0
aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_tonu = 0
aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_gunu = 0
konut_haric_en_yuksek_su_tuketim_ton = 0
konut_haric_en_yuksek_su_tuketim_abone_no = 0
konut_haric_en_yuksek_su_tuketim_abone_tipi = " "
konut_haric_en_yuksek_su_tuketim_aylik_tuketim_ton = 0
konut_haric_en_yuksek_su_tuketim_aylik_tuketim_ucreti = 0

su_tuketim_ucret_konut_toplam = 0
su_tuketim_ucret_is_yeri_toplam = 0
su_tuketim_ucret_resmi_daire_toplam = 0
su_tuketim_ucret_organize_sanayi_toplam = 0
su_tuketim_ucret_ilce_tarim_hayvan_sulama_toplam = 0

izsu_toplam = 0
ilce_belediye_aldigi_toplam = 0
buyuksehir_belediye_aldigi_toplam = 0
devletin_aldigi_toplam = 0



while baska_var_mi=="e" or baska_var_mi=="E":

    ctv_miktari=0
    KATI_ATIK=13
    BERTARAF=2.54
    


    abone_no=int(input("Abone numaranızı giriniz: "))

    abone_tipi_kodu=int(input("Abone tipi kodunuzu giriniz (1-5 arasında): "))
    while abone_tipi_kodu<1 or abone_tipi_kodu>5:
        abone_tipi_kodu=int(input("Hatalı giriş yaptınız.Lütfen belirtilen aralıklarda bir abone tipi kodu giriniz (1-5 arasında): "))

    onceki_sayac_degeri=int(input("Önceki sayaç değerini giriniz: "))
    while onceki_sayac_degeri<0:
        onceki_sayac_degeri=int(input("Hatalı giriş yaptınız.Lütfen önceki sayaç değeri için 0 yada 0'dan büyük bir sayı giriniz: "))

    simdiki_sayac_degeri=int(input("Şimdiki sayaç değerini giriniz: "))
    while simdiki_sayac_degeri<onceki_sayac_degeri:
        simdiki_sayac_degeri=int(input("Hatalı giriş yaptınız.Lütfen önceki sayaç değerine eşit veya daha büyük bir değer giriniz: "))
    toplam_harcanan_ton = simdiki_sayac_degeri - onceki_sayac_degeri  # Harcanan suyu bulduk
    ctv_miktari=toplam_harcanan_ton*0.39

    sayac_okuma_gun_sayisi=int(input("Önceki ve şimdiki sayaç okuma tarihleri arasındaki gün sayısını giriniz (0'dan büyük olmalı): "))
    while sayac_okuma_gun_sayisi<0:
        sayac_okuma_gun_sayisi=int(input("Hatalı giriş yaptınız.Lütfen 0 veya daha büyük bir gün sayısı giriniz: "))

    fazladan_gun = sayac_okuma_gun_sayisi - 30
    gune_eklenen_1 = fazladan_gun * 13 / 30
    gune_eklenen_2 = fazladan_gun * 7 / 30

    if abone_tipi_kodu==1:
        toplam_gun_konut += sayac_okuma_gun_sayisi
        toplam_ton_konut += toplam_harcanan_ton
        abone_tipi_adi="Konut"
        hane_sayisi=int(input("Hane sayısını giriniz: "))
        while hane_sayisi<1:
            hane_sayisi=int(input("Hatalı değer girdiniz.Lütfen 1 ya da 1'den büyük bir değer giriniz: "))
        konut_abone_sayisi += hane_sayisi
        if hane_sayisi==1:
            
            indirim_durumu=input("Herhangi bir indirimi durumunuz var mı ? (Yok/Şehit/Gazi/Sporcu/Engelli (Y/y/Ş/ş/G/g/S/s/E/e karakterleri): ")
            while indirim_durumu!="Y" and indirim_durumu!="y" and indirim_durumu!="Ş" and indirim_durumu!="ş" and indirim_durumu!="G" and indirim_durumu!="g" and indirim_durumu!="E" and indirim_durumu!="e":
                indirim_durumu=input("Hatalı karakter girişi yaptınız.Herhangi bir indirimi durumunuz var mı ? (Yok/Şehit/Gazi/Sporcu/Engelli (Y/y/Ş/ş/G/g/S/s/E/e karakterleri): ")

            if indirim_durumu=="Y" or indirim_durumu=="y":

                if toplam_harcanan_ton>0 and toplam_harcanan_ton<=13+gune_eklenen_1:
                    tonaj_fatura=toplam_harcanan_ton*2.89
                    atik_su_ucreti=toplam_harcanan_ton*1.44
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari  
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV

                elif toplam_harcanan_ton>13+gune_eklenen_1 and toplam_harcanan_ton<=20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=(toplam_harcanan_ton-13-gune_eklenen_1)*3.13 + (13+gune_eklenen_1)*2.89
                    atik_su_ucreti=(toplam_harcanan_ton-13-gune_eklenen_1)*1.56 +(13+gune_eklenen_1)*1.44
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV

                elif toplam_harcanan_ton>20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=(toplam_harcanan_ton-20 - gune_eklenen_1 - gune_eklenen_2)*6.43 + (7+gune_eklenen_2)*3.13 + (13+gune_eklenen_1)*2.89
                    atik_su_ucreti=(toplam_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*3.22+ (7+gune_eklenen_2)*1.56 + (13+gune_eklenen_1)*1.44
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
            if indirim_durumu=="Ş" or indirim_durumu=="ş" or indirim_durumu=="G" or indirim_durumu=="g" or indirim_durumu=="S" or indirim_durumu=="s":
                if toplam_harcanan_ton>0 and toplam_harcanan_ton<=13+gune_eklenen_1:
                    tonaj_fatura=(toplam_harcanan_ton*2.89)*0.5
                    atik_su_ucreti=(toplam_harcanan_ton*1.44)*0.5
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                elif toplam_harcanan_ton>13+gune_eklenen_1 and toplam_harcanan_ton<=20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=((toplam_harcanan_ton-13-gune_eklenen_1)*3.13 + (13+gune_eklenen_1)*2.89)*0.5
                    atik_su_ucreti=((toplam_harcanan_ton-13-gune_eklenen_1)*1.56 +(13+gune_eklenen_1)*1.44)*0.5
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                elif toplam_harcanan_ton>20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=((toplam_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*6.43 + (7+gune_eklenen_2)*3.13 + (13+gune_eklenen_1)*2.89)*0.5
                    atik_su_ucreti=((toplam_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*3.22+(7+gune_eklenen_2)*1.56 + (13+gune_eklenen_1)*1.44)*0.5
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
            elif indirim_durumu == "E" or indirim_durumu == "e":
                if toplam_harcanan_ton>0 and toplam_harcanan_ton<=13+gune_eklenen_1:
                    tonaj_fatura=(toplam_harcanan_ton*2.89)*0.5
                    atik_su_ucreti=(toplam_harcanan_ton*1.44)*0.5
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                elif toplam_harcanan_ton>13+gune_eklenen_1 and toplam_harcanan_ton<=20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=((toplam_harcanan_ton-13-gune_eklenen_1)*3.13 + (13+gune_eklenen_1)*2.89)*0.5
                    atik_su_ucreti=((toplam_harcanan_ton-13-gune_eklenen_1)*1.56 +(13+gune_eklenen_1)*1.44)*0.5
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                elif toplam_harcanan_ton>20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=(toplam_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*6.43 + ((7+gune_eklenen_2)*3.13 + (13+gune_eklenen_1)*2.89)*0.5
                    atik_su_ucreti=(toplam_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*3.22+ ((7+gune_eklenen_2)*1.56 + (13+gune_eklenen_1)*1.44)*0.5
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
            if toplam_harcanan_ton > 100 or (tonaj_fatura/sayac_okuma_gun_sayisi)*30>500:
                aylik_100_ton_uzeri_veya_500_tlden_fazla += 1
        

        elif hane_sayisi>1:
            sehit_gazi_sporcu_sayisi=int(input("Şehit, gazi veya sporcu sayısı (0 ile hane sayısı arasında) :"))
            engelli_sayisi=int(input("Engelli sayısını giriniz (0 ile hane sayısı arasında)"))
            while sehit_gazi_sporcu_sayisi+engelli_sayisi<0 or sehit_gazi_sporcu_sayisi+engelli_sayisi>hane_sayisi:
                print("Şehit, gazi, sporcu ve engelli sayısı hane sayısını geçemez.Lütfen değerleri yeniden giriniz")
                sehit_gazi_sporcu_sayisi = int(input("Şehit, gazi veya sporcu sayısı (0 ile hane sayısı arasında) :"))
                engelli_sayisi = int(input("Engelli sayısını giriniz (0 ile hane sayısı arasında)"))

            hane_basi_harcanan_ton = toplam_harcanan_ton/hane_sayisi
            engelli_1_hane_fatura = 0
            engelli_toplam_faturasi = 0
            sehit_1_hane_fatura = 0
            sehit_toplam_faturasi = 0
            digerleri_1_hane_fatura = 0
            digerlerinin_toplam_faturasi = 0

            if engelli_sayisi >= 1:
                if hane_basi_harcanan_ton>0 and hane_basi_harcanan_ton<=13+gune_eklenen_1:
                    tonaj_fatura=(hane_basi_harcanan_ton*2.89)*0.5
                    atik_su_ucreti=(hane_basi_harcanan_ton*1.44)*0.5
                    KATI_ATIK *= hane_sayisi
                    BERTARAF *= hane_sayisi
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                    engelli_1_hane_fatura = toplam_fatura
                    
                elif hane_basi_harcanan_ton>13+gune_eklenen_1 and hane_basi_harcanan_ton<=20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=((hane_basi_harcanan_ton-13-gune_eklenen_1)*3.13 + (13+gune_eklenen_1)*2.89)*0.5
                    atik_su_ucreti=((hane_basi_harcanan_ton-13-gune_eklenen_1)*1.56 +(13+gune_eklenen_1)*1.44)*0.5
                    KATI_ATIK *= hane_sayisi
                    BERTARAF *= hane_sayisi
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                    engelli_1_hane_fatura = toplam_fatura

                elif hane_basi_harcanan_ton>20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=(hane_basi_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*6.43 + ((7+gune_eklenen_2)*3.13 + (13+gune_eklenen_1)*2.89)*0.5
                    atik_su_ucreti=(hane_basi_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*3.22+ ((7+gune_eklenen_2)*1.56 + (13+gune_eklenen_1)*1.44)*0.5
                    KATI_ATIK *= hane_sayisi
                    BERTARAF *= hane_sayisi
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                    engelli_1_hane_fatura = toplam_fatura
                engelli_toplam_faturasi = engelli_1_hane_fatura*engelli_sayisi

            if sehit_gazi_sporcu_sayisi>=1:
                if hane_basi_harcanan_ton>0 and hane_basi_harcanan_ton<=13+gune_eklenen_1:
                    tonaj_fatura=(hane_basi_harcanan_ton*2.89)*0.5
                    atik_su_ucreti=(hane_basi_harcanan_ton*1.44)*0.5
                    KATI_ATIK *= hane_sayisi
                    BERTARAF *= hane_sayisi
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                    sehit_1_hane_fatura = toplam_fatura

                elif hane_basi_harcanan_ton>13+gune_eklenen_1 and hane_basi_harcanan_ton<=20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=((hane_basi_harcanan_ton-13-gune_eklenen_1)*3.13 + (13+gune_eklenen_1)*2.89)*0.5
                    atik_su_ucreti=((hane_basi_harcanan_ton-13-gune_eklenen_1)*1.56 +(13+gune_eklenen_1)*1.44)*0.5
                    KATI_ATIK *= hane_sayisi
                    BERTARAF *= hane_sayisi
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                    sehit_1_hane_fatura = toplam_fatura

                elif hane_basi_harcanan_ton>20+gune_eklenen_1+gune_eklenen_2:
                    tonaj_fatura=((hane_basi_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*6.43 + (7+gune_eklenen_2)*3.13 + (13+gune_eklenen_1)*2.89)*0.5
                    atik_su_ucreti=((hane_basi_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*3.22+(7+gune_eklenen_2)*1.56 + (13+gune_eklenen_1)*1.44)*0.5
                    KATI_ATIK *= hane_sayisi
                    BERTARAF *= hane_sayisi
                    toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                    KDV = (toplam_fatura-ctv_miktari)*8/100
                    toplam_fatura += KDV
                    sehit_1_hane_fatura = toplam_fatura
                sehit_toplam_faturasi = sehit_1_hane_fatura*sehit_gazi_sporcu_sayisi
            
            if hane_basi_harcanan_ton>0 and hane_basi_harcanan_ton<=13+gune_eklenen_1:
                tonaj_fatura=hane_basi_harcanan_ton*2.89
                atik_su_ucreti=hane_basi_harcanan_ton*1.44
                KATI_ATIK *= hane_sayisi
                BERTARAF *= hane_sayisi
                toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari  
                KDV = (toplam_fatura-ctv_miktari)*8/100
                toplam_fatura += KDV
                digerleri_1_hane_fatura = toplam_fatura

            elif hane_basi_harcanan_ton>13+gune_eklenen_1 and hane_basi_harcanan_ton<=20+gune_eklenen_1+gune_eklenen_2:
                tonaj_fatura=(hane_basi_harcanan_ton-13-gune_eklenen_1)*3.13 + (13+gune_eklenen_1)*2.89
                atik_su_ucreti=(hane_basi_harcanan_ton-13-gune_eklenen_1)*1.56 +(13+gune_eklenen_1)*1.44
                KATI_ATIK *= hane_sayisi
                BERTARAF *= hane_sayisi
                toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                KDV = (toplam_fatura-ctv_miktari)*8/100
                toplam_fatura += KDV
                digerleri_1_hane_fatura = toplam_fatura

            elif hane_basi_harcanan_ton>20+gune_eklenen_1+gune_eklenen_2:
                tonaj_fatura=(hane_basi_harcanan_ton-20 - gune_eklenen_1 - gune_eklenen_2)*6.43 + (7+gune_eklenen_2)*3.13 + (13+gune_eklenen_1)*2.89
                atik_su_ucreti=(hane_basi_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*3.22+ (7+gune_eklenen_2)*1.56 + (13+gune_eklenen_1)*1.44
                KATI_ATIK *= hane_sayisi
                BERTARAF *= hane_sayisi
                toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
                KDV = (toplam_fatura-ctv_miktari)*8/100
                toplam_fatura += KDV
                digerleri_1_hane_fatura = toplam_fatura
            digerlerinin_toplam_faturasi = digerleri_1_hane_fatura*(hane_sayisi-sehit_gazi_sporcu_sayisi-engelli_sayisi)
            toplam_fatura = digerlerinin_toplam_faturasi + engelli_toplam_faturasi + sehit_toplam_faturasi
            if toplam_harcanan_ton > 100 or tonaj_fatura*30/sayac_okuma_gun_sayisi > 500:
                aylik_100_ton_uzeri_veya_500_tlden_fazla += hane_sayisi

        su_tuketim_ucret_konut_toplam += tonaj_fatura*30/sayac_okuma_gun_sayisi

    elif abone_tipi_kodu == 2:
        toplam_gun_is_yeri += sayac_okuma_gun_sayisi
        toplam_ton_is_yeri += toplam_harcanan_ton
        is_yeri_abone_sayisi += 1
        abone_tipi_adi = "İş Yeri"
        tonaj_fatura = toplam_harcanan_ton*7.38 
        atik_su_ucreti = toplam_harcanan_ton*3.68
        toplam_fatura = tonaj_fatura + KATI_ATIK +BERTARAF + atik_su_ucreti + ctv_miktari  
        KDV = (toplam_fatura-ctv_miktari)*8/100
        toplam_fatura += KDV 
        if toplam_harcanan_ton > 100 or (tonaj_fatura/sayac_okuma_gun_sayisi)*30>500:
            aylik_100_ton_uzeri_veya_500_tlden_fazla += 1
        su_tuketim_ucret_is_yeri_toplam += tonaj_fatura*30/sayac_okuma_gun_sayisi
    elif abone_tipi_kodu == 3:
        toplam_gun_resmi_daire += sayac_okuma_gun_sayisi
        toplam_ton_resmi_daire += toplam_harcanan_ton
        resmi_daire_abone_sayisi +=1
        abone_tipi_adi = "Resmi Daire"
        tonaj_fatura = toplam_harcanan_ton*4.34
        atik_su_ucreti = toplam_harcanan_ton*2.16
        toplam_fatura= tonaj_fatura + KATI_ATIK +BERTARAF + atik_su_ucreti + ctv_miktari  
        KDV = (toplam_fatura-ctv_miktari)*8/100
        toplam_fatura += KDV 
        if toplam_harcanan_ton > 100 or (tonaj_fatura/sayac_okuma_gun_sayisi)*30>500:
            aylik_100_ton_uzeri_veya_500_tlden_fazla += 1
        if toplam_harcanan_ton > aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_tonu:
            aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_abone_nosu = abone_no
            aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_tonu = toplam_harcanan_ton
            aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_gunu = sayac_okuma_gun_sayisi
        su_tuketim_ucret_resmi_daire_toplam += tonaj_fatura*30/sayac_okuma_gun_sayisi
    elif abone_tipi_kodu == 4:
        toplam_gun_organize_sanayi += sayac_okuma_gun_sayisi
        toplam_ton_organize_sanayi += toplam_harcanan_ton
        organize_sanayi_abone_sayisi += 1
        abone_tipi_adi = "Organize Sanayi"
        tonaj_fatura = toplam_harcanan_ton*5
        atik_su_ucreti = toplam_harcanan_ton*2.5
        toplam_fatura =tonaj_fatura + KATI_ATIK +BERTARAF + atik_su_ucreti + ctv_miktari  
        KDV = (toplam_fatura-ctv_miktari)*8/100
        toplam_fatura += KDV 
        if toplam_harcanan_ton > 100 or (tonaj_fatura/sayac_okuma_gun_sayisi)*30>500:
            aylik_100_ton_uzeri_veya_500_tlden_fazla += 1
        su_tuketim_ucret_organize_sanayi_toplam += tonaj_fatura*30/sayac_okuma_gun_sayisi
    elif abone_tipi_kodu == 5:
        toplam_gun_ilce_tarim_hayvan_sulama += sayac_okuma_gun_sayisi
        toplam_ton_ilce_tarim_hayvan_sulama += toplam_harcanan_ton
        ilce_tarım_hayvan_sulama_abone_sayisi +=1
        abone_tipi_adi = "İlçe Tarımsal ve Hayvan Sulama"
        if toplam_harcanan_ton>0 and toplam_harcanan_ton<=13+gune_eklenen_1:
            tonaj_fatura=toplam_harcanan_ton*1.45
            atik_su_ucreti=toplam_harcanan_ton*0.72
            toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari  
            KDV = (toplam_fatura-ctv_miktari)*8/100
            toplam_fatura += KDV

        elif toplam_harcanan_ton>13+gune_eklenen_1 and toplam_harcanan_ton<=20+gune_eklenen_1+gune_eklenen_2:
            tonaj_fatura=(toplam_harcanan_ton-13-gune_eklenen_1)*2.89 + (13+gune_eklenen_1)*1.45
            atik_su_ucreti=(toplam_harcanan_ton-13-gune_eklenen_1)*1.44 +(13+gune_eklenen_1)*0.72
            toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
            KDV = (toplam_fatura-ctv_miktari)*8/100
            toplam_fatura += KDV

        elif toplam_harcanan_ton>20+gune_eklenen_1+gune_eklenen_2:
            tonaj_fatura=(toplam_harcanan_ton-20 - gune_eklenen_1 - gune_eklenen_2)*6.43 + (7+gune_eklenen_2)*2.89 + (13+gune_eklenen_1)*1.45
            atik_su_ucreti=(toplam_harcanan_ton-20-gune_eklenen_1-gune_eklenen_2)*3.22+ (7+gune_eklenen_2)*1.44 + (13+gune_eklenen_1)*0.72
            toplam_fatura=tonaj_fatura+KATI_ATIK+BERTARAF+atik_su_ucreti+ctv_miktari
            KDV = (toplam_fatura-ctv_miktari)*8/100
            toplam_fatura += KDV
        if toplam_harcanan_ton >50:
            aylik_su_tuketim_50_tondan_fazla_olan_ilce_abone_sayisi +=1
        if toplam_harcanan_ton > 100 or (tonaj_fatura/sayac_okuma_gun_sayisi)*30>500:
            aylik_100_ton_uzeri_veya_500_tlden_fazla += 1
        su_tuketim_ucret_ilce_tarim_hayvan_sulama_toplam += tonaj_fatura*30/sayac_okuma_gun_sayisi
    
    izsu_toplam += toplam_fatura - KDV - ctv_miktari - KATI_ATIK*hane_sayisi - BERTARAF*hane_sayisi
    ilce_belediye_aldigi_toplam += ctv_miktari + BERTARAF*hane_sayisi
    devletin_aldigi_toplam += KDV
    buyuksehir_belediye_aldigi_toplam += KATI_ATIK*hane_sayisi

    if abone_tipi_kodu != 1:
        if tonaj_fatura*30/sayac_okuma_gun_sayisi > konut_haric_en_yuksek_su_tuketim_ton:
            konut_haric_en_yuksek_su_tuketim_ton = tonaj_fatura*30/sayac_okuma_gun_sayisi
            konut_haric_en_yuksek_su_tuketim_abone_no = abone_no
            konut_haric_en_yuksek_su_tuketim_abone_tipi = abone_tipi_adi
            konut_haric_en_yuksek_su_tuketim_aylik_tuketim_ton = toplam_harcanan_ton*30/sayac_okuma_gun_sayisi
            konut_haric_en_yuksek_su_tuketim_aylik_tuketim_ucreti = tonaj_fatura*30/sayac_okuma_gun_sayisi
    
    print("*************************************************************************************************************************************************************************************")
    print("Abone No: ",format(abone_no))
    print("Abone Tipi Adı: ",abone_tipi_adi)
    print("Dönemlik Su Tüketim Miktarınız: ",format(toplam_harcanan_ton,".2f"))
    print("Dönemlik Su Tüketim Ücreti: ",format(tonaj_fatura,".2f"))
    print("Dönemlik Atık Su Ücreti: ",format(atik_su_ucreti,".2f"))
    print("Dönemlik Toplam Su Tüketim ve Atık Su Ücreti: ",format(tonaj_fatura+atik_su_ucreti,".2f"))
    print("Dönemlik Toplam ÇTV Miktarı: ",format(ctv_miktari,".2f"))
    print("Dönemlik Katı Atık Toplama Ücreti: ",format(KATI_ATIK,".2f"))
    print("Dönemlik Katı Atık Bertaraf Ücreti: ",format(BERTARAF,".2f"))
    print("Dönemlik Toplam Fatura Tutarı: ",format(toplam_fatura,".2f"))
    print("Dönemlik devlete aktarılacak KDV tutarı (%8): ",format(KDV,".2f"))
    print("Dönemlik ilçe belediyesine aktarılacak tutar: ",format(ctv_miktari+KATI_ATIK,".2f"))
    print("Dönemlik büyükşehir belediyesine aktarılacak tutar: ",format(BERTARAF,".2f"))
    print("Dönemlik İZSU payı: ",format(toplam_fatura - KDV - ctv_miktari - KATI_ATIK - BERTARAF,".2f"))
    print("*************************************************************************************************************************************************************************************\n")
  
    baska_var_mi=input("Başka bir fatura var mı ?")
tum_abone_sayisi = konut_abone_sayisi + is_yeri_abone_sayisi + resmi_daire_abone_sayisi + organize_sanayi_abone_sayisi + ilce_tarım_hayvan_sulama_abone_sayisi
bornova_aylik_toplam_harcanan_ton = (toplam_ton_konut*30/toplam_gun_konut+toplam_ton_is_yeri*30/toplam_gun_is_yeri + toplam_ton_organize_sanayi*30/toplam_gun_organize_sanayi+toplam_ton_resmi_daire*30/toplam_gun_resmi_daire+toplam_ton_ilce_tarim_hayvan_sulama*30/toplam_gun_ilce_tarim_hayvan_sulama)
tum_su_tuketim_aylik = su_tuketim_ucret_ilce_tarim_hayvan_sulama_toplam+su_tuketim_ucret_is_yeri_toplam+su_tuketim_ucret_konut_toplam+su_tuketim_ucret_organize_sanayi_toplam+su_tuketim_ucret_resmi_daire_toplam



print("Konut tipi abone(hane) sayısı: ",konut_abone_sayisi,                                         "Tüm aboneler içindeki yüzdesi: ",format(konut_abone_sayisi*100/tum_abone_sayisi,".2f"),"                           Aylık ortalama su tüketim miktarı: ",format(toplam_ton_konut*toplam_gun_konut/30,".2f"))
print("İş Yeri tipi abone(hane) sayısı: ",is_yeri_abone_sayisi,                                     "Tüm aboneler içindeki yüzdesi: ",format(is_yeri_abone_sayisi*100/tum_abone_sayisi,".2f"),"                         Aylık ortalama su tüketim miktarı: ",format(toplam_ton_is_yeri*toplam_gun_is_yeri/30,".2f"))
print("Resmi Daire tipi abone(hane) sayısı: ",resmi_daire_abone_sayisi,                             "Tüm aboneler içindeki yüzdesi: ",format(resmi_daire_abone_sayisi*100/tum_abone_sayisi,".2f"),"                     Aylık ortalama su tüketim miktarı: ",format(toplam_ton_resmi_daire*toplam_gun_resmi_daire/30,".2f"))
print("Organize Sanayi tipi abone(hane) sayısı: ",organize_sanayi_abone_sayisi,                     "Tüm aboneler içindeki yüzdesi: ",format(organize_sanayi_abone_sayisi*100/tum_abone_sayisi,".2f"),"                 Aylık ortalama su tüketim miktarı: ",format(toplam_ton_organize_sanayi*toplam_gun_organize_sanayi/30,".2f"))
print("İlçe Tarım ve Hayvan Sulama tipi abone(hane) sayısı: ",ilce_tarım_hayvan_sulama_abone_sayisi,"Tüm aboneler içindeki yüzdesi: ",format(ilce_tarım_hayvan_sulama_abone_sayisi*100/tum_abone_sayisi,".2f"),"        Aylık ortalama su tüketim miktarı: ",format(toplam_ton_ilce_tarim_hayvan_sulama*toplam_gun_ilce_tarim_hayvan_sulama/30,".2f"))

"""
print("Konut tipi abonelerinden 1. kademedeki")
print("Konut tipi abonelerinden 2. kademedeki")
print("Konut tipi abonelerinden 3. kademedeki")
"""
print("Aylık su tüketim miktarı 50 tondan fazla olan ilçe tarımsal ve hayvan sulama tipi abonelerin sayısı: ",aylik_su_tuketim_50_tondan_fazla_olan_ilce_abone_sayisi,"ilçe tarımsal ve hayvan sulama tipi aboneler içindeki yüzdesi: ",format(aylik_su_tuketim_50_tondan_fazla_olan_ilce_abone_sayisi*100/ilce_tarım_hayvan_sulama_abone_sayisi,".2f"))
print("Aylık su tüketim miktarı 100 tondan yüksek veya aylık su tüketim ücreti 500 TL’den yüksek olan abonelerin (hanelerin) sayısı: ",aylik_100_ton_uzeri_veya_500_tlden_fazla)
###  print("Şehit, gazi veya devlet sporcusu olan ve engelli olan konut tipi abonelerin (hanelerin) sayısı ve konut tipi aboneler (haneler) içindeki yüzdeleri ")
print("Aylık su tüketim miktarı en yüksek olan resmi daire tipi abonenin abone no’su: ",aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_abone_nosu,"Aylık su tüketim miktarı: ",format(aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_tonu*30/aylik_su_tuketim_miktari_en_fazla_olan_resmi_daire_gunu,".2f"))
print("Aylık su tüketim ücreti en yüksek olan konut tipi dışındaki abonenin abone no’su: ",konut_haric_en_yuksek_su_tuketim_abone_no,"abone tipi adı: ",konut_haric_en_yuksek_su_tuketim_abone_tipi,"aylık su tüketim miktarı: ",format(konut_haric_en_yuksek_su_tuketim_aylik_tuketim_ton,".2f"),"ödediği aylık su tüketim ücreti: ",format(konut_haric_en_yuksek_su_tuketim_aylik_tuketim_ucreti,".2f"))

print("Konut tipindeki aylık toplam su tüketim miktarı: ",format(toplam_ton_konut*30/toplam_gun_konut,".2f"),"Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: ",format((toplam_ton_konut*30/toplam_gun_konut)*100/bornova_aylik_toplam_harcanan_ton,".2f"),"Bornova'nın aylık toplam su tüketim miktarı: ",format(bornova_aylik_toplam_harcanan_ton,".2f"))
print("İş Yeri tipindeki aylık toplam su tüketim miktarı: ",format(toplam_ton_is_yeri*30/toplam_gun_is_yeri,".2f"),"Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: ",format((toplam_ton_is_yeri*30/toplam_gun_is_yeri)*100/bornova_aylik_toplam_harcanan_ton,".2f"),"Bornova'nın aylık toplam su tüketim miktarı: ",format(bornova_aylik_toplam_harcanan_ton,".2f"))
print("Resmi Daire tipindeki aylık toplam su tüketim miktarı: ",format(toplam_ton_resmi_daire*30/toplam_gun_resmi_daire,".2f"),"Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: ",format((toplam_ton_resmi_daire*30/toplam_gun_resmi_daire)*100/bornova_aylik_toplam_harcanan_ton,".2f"),"Bornova'nın aylık toplam su tüketim miktarı: ",format(bornova_aylik_toplam_harcanan_ton,".2f"))
print("Organize Sanayi tipindeki aylık toplam su tüketim miktarı: ",format(toplam_ton_organize_sanayi*30/toplam_gun_organize_sanayi,".2f"),"Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: ",format((toplam_ton_organize_sanayi*30/toplam_gun_organize_sanayi)*100/bornova_aylik_toplam_harcanan_ton,".2f"),"Bornova'nın aylık toplam su tüketim miktarı: ",format(bornova_aylik_toplam_harcanan_ton,".2f"))
print("İlçe Tarım ve Hayvan Sulama tipindeki aylık toplam su tüketim miktarı: ",format(toplam_ton_ilce_tarim_hayvan_sulama*30/toplam_gun_ilce_tarim_hayvan_sulama,".2f"),"Bornova'nın aylık toplam su tüketim miktarı içindeki yüzdesi: ",format((toplam_ton_ilce_tarim_hayvan_sulama*30/toplam_gun_ilce_tarim_hayvan_sulama)*100/bornova_aylik_toplam_harcanan_ton,".2f"),"Bornova'nın aylık toplam su tüketim miktarı: ",format(bornova_aylik_toplam_harcanan_ton,".2f"))

print("Konut tipindeki aylık toplam su tüketim ücreti: ",format(su_tuketim_ucret_konut_toplam,".2f"))
print("İş Yeri tipindeki aylık toplam su tüketim ücreti: ",format(su_tuketim_ucret_is_yeri_toplam,".2f"))
print("Resmi Daire tipindeki aylık toplam su tüketim ücreti: ",format(su_tuketim_ucret_resmi_daire_toplam,".2f"))
print("Organize Sanayi tipindeki aylık toplam su tüketim ücreti: ",format(su_tuketim_ucret_organize_sanayi_toplam,".2f"))
print("İlçe Tarım ve Hayvan Sulama tipindeki aylık toplam su tüketim ücreti: ",format(su_tuketim_ucret_ilce_tarim_hayvan_sulama_toplam,".2f"))
print("tüm abonelerden elde edilen aylık toplam su tüketim ücreti: ",format(tum_su_tuketim_aylik,".2f"))
print("İlgili dönemde İZSU'nun elde ettiği gelir: ",format(izsu_toplam,".2f"),"İlçe belediyesinin elde ettiği gelir: ",format(ilce_belediye_aldigi_toplam,".2f"),"Büyükşehir belediyesinin elde ettiği gelir: ",format(buyuksehir_belediye_aldigi_toplam,".2f"),"Devletin elde ettiği gelir: ",format(devletin_aldigi_toplam,".2f"))
