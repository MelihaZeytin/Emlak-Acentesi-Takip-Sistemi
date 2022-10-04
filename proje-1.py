ASGARI_UCRET = 2324.70  # 2020 yılı için belirlenen aylık net asgari ücret, 2324,70 TL’dir.
SATIS_KOMISYON_ORANI = 0.04  # Emlak acentesi, yapılan her satış için satış bedelinin %4’ü kadar kazanır.
PRIM_ORANI = 0.1  # Maaşlara ek olarak ödenen, 1 ayda kazandırdıkları emlak komisyonu miktarının %10’u tutarında ücret ödenir.
IKRAMIYE = ASGARI_UCRET/2  # Emlak acentesinin, danışmanlarına kotalarını doldurmaları durumunda maaşlarına ek olarak ödediği, net asgari ücretin yarısı tutarındaki ücreti ifade etmektedir.
KOTA_ORANI = 10  # kota, maaşın en az 10 katı olmalıdır.
MIN_KIRA_ADET = 10
MIN_KIRA_TUTAR = 25000

# aşağıdaki değişkenlere ilk değer ataması yapıldı.
toplam_satilan_konut_say = 0
toplam_satilan_isyeri_say = 0
toplam_satilan_arsa_say = 0
toplam_kiralanan_konut_say = 0
toplam_kiralanan_isyeri_say = 0
toplam_kiralanan_arsa_say = 0
satilan_konut_bedel_toplami = 0
satilan_isyeri_bedel_toplami = 0
satilan_arsa_bedel_toplami = 0
toplam_satilan_konut_bedeli_ortalamasi = 0
toplam_satilan_isyeri_bedeli_ortalamasi = 0
toplam_satilan_arsa_bedeli_ortalamasi = 0
en_yuksek_bedelle_satilan_emlak_tipi = ''
en_yuksek_bedelle_satilan_emlak_bedeli = 0
en_yuksek_bedelle_satilan_emlak_danisman_adi = ''
en_yuksek_bedelle_kiralanan_konut_danisman_adi = ''
asgari_ucretten_fazla_kiralik_konut_say_oran = 0
satis_yapmayan_danisman_sayisi = 0
en_cok_satis_yapan_danismanin_satis_adedi = 0
en_cok_satis_yapan_danisman_adi = ''
en_cok_satis_bedeli_yapan_danisman_emlak_say = 0
kota_dolduran_sayisi = 0
primi_maasindan_yuksek_olanlar = 0
en_yuksek_prim = 0
en_yuksek_prim_danisman_ad_soyad = ''
en_yuksek_prim_alanin_maasi = 0
en_yuksek_prim_alanin_aylik_toplam_ucreti = 0
en_dusuk_prim_danisman_ad_soyad = ''
en_dusuk_prim_alanin_maasi = 0
en_dusuk_prim = 0
en_dusuk_prim_alanin_aylik_toplam_ucreti = 0
toplam_ucretlerin_toplami = 0
toplam_komisyon = 0
asgari_ucretten_fazla_kiralik_konut_say = 0
en_cok_satis_yapan_danisman_bedelleri = 0
o_ay_en_yuksek_bedelli_kiralanan_konut = 0
tum_danismanlarin_aylik_toplam_ucreti = 0
tum_danismanlarin_aylik_toplam_ucreti_ikramiyesiz = 0
en_cok_satis_bedeli_yapan_danisman_toplam_satis_bedeli = 0
en_cok_satis_bedeli_yapan_danismanin_adi = ''
en_yuksek_bedelle_satilan_emlak = 0
o_ay_en_yuksek_bedelle_satilan_emlagin_bedeli = 0
min_kira_kosullarini_saglayanlarin_sayisi = 0

emlak_danisman_sayisi = int(input("Lütfen acenteye bağlı olarak çalışan emlak danışman sayısını giriniz:"))
while emlak_danisman_sayisi <= 0:  # emlak danışman sayısı 0 dan büyük olana kadar döngüde kalır
    emlak_danisman_sayisi = int(input("Hatalı veri girdiniz, lütfen emlak danışman sayısını giriniz:"))
# döngü danışman sayısı kadar devam eder.
for danisman_sayisi in range(1, (emlak_danisman_sayisi + 1)):
    danisman_ad_soyad = input("Lütfen ad-soyadı giriniz:")
    maas = float(input("Lütfen maaşı giriniz:"))
    while maas < ASGARI_UCRET:  # maaş asgari ücretten büyük olana kadar döngüde kalır
        maas = float(input("Maaş asgari ücretten az olamaz, lütfen maaşı tekrar giriniz:"))
    kota = float(input("lütfen kotayı giriniz:"))
    while kota < maas*KOTA_ORANI:
        kota = float(input("Hatalı veri girdiniz, lütfen kotayı giriniz:"))
    # değişken değerleri her danışman için sıfırlanır.
    satilan_emlak_adedi = 0
    satilan_konut_bedeli = 0
    satilan_arsa_bedeli = 0
    satilan_isyeri_bedeli = 0
    kiralanan_emlak_adedi = 0
    kiralanan_konut_sayisi = 0
    emlak_komisyonu_kira = 0
    kiralanan_konut_bedeli = 0
    en_yuksek_bedelli_kiralanan_konut = 0
    aylik_toplam_ucret = 0
    aylik_toplam_ucret_ikramiyesiz = 0
    kota_dolduruldu_mu = False
    danisman_satis_yapti_mi = False
    bir_danismanin_toplam_satis_bedeli = 0
    bir_danisman_kira_toplam_bedel = 0
    yeni_emlak = 'e'
    while yeni_emlak == 'e' or yeni_emlak == 'E':
        emlak_tipi = input("Emlak tipini giriniz (K/k/İ/i/A/a):")
        while emlak_tipi not in ['K', 'k', 'İ', 'i', 'A', 'a']:
            emlak_tipi = input("Hatalı veri girdiniz, lütfen emlak tipini giriniz (K/k/İ/i/A/a):")
        islem_turu = input("İşlem türünü giriniz (S/s/K/k):")
        while islem_turu not in ['S', 's', 'K', 'k']:
            islem_turu = input("Hatalı veri girdiniz, lütfen işlem türünü giriniz (S/s/K/k):")
        satis_kira_bedeli = float(input("Satış/kira bedelini giriniz: "))
        while satis_kira_bedeli <= 0:
            satis_kira_bedeli = float(input("Hatalı veri girdiniz, lütfen satış/kira bedelini giriniz:"))

        if islem_turu == 'S' or islem_turu == 's':
            satilan_emlak_adedi += 1
            bir_danismanin_toplam_satis_bedeli += satis_kira_bedeli
            danisman_satis_yapti_mi = True
            # en yüksek bedelle satılan emlağın bedelinin bulunması
            if satis_kira_bedeli > en_yuksek_bedelle_satilan_emlak:
                en_yuksek_bedelle_satilan_emlak = satis_kira_bedeli
            if emlak_tipi == 'k' or emlak_tipi == 'K':
                toplam_satilan_konut_say += 1
                satilan_konut_bedeli += satis_kira_bedeli
            elif emlak_tipi == 'i' or emlak_tipi == 'İ':
                toplam_satilan_isyeri_say += 1
                satilan_isyeri_bedeli += satis_kira_bedeli
            else:
                toplam_satilan_arsa_say += 1
                satilan_arsa_bedeli += satis_kira_bedeli

            # en çok satış bedeli yapan danışmanın bilgilerin bulunması
            if bir_danismanin_toplam_satis_bedeli > en_cok_satis_bedeli_yapan_danisman_toplam_satis_bedeli:
                en_cok_satis_bedeli_yapan_danisman_toplam_satis_bedeli = bir_danismanin_toplam_satis_bedeli
                en_cok_satis_bedeli_yapan_danismanin_adi = danisman_ad_soyad
                en_cok_satis_bedeli_yapan_danisman_emlak_say = satilan_emlak_adedi

            # o ay en yüksek bedelle satın alınan emlagın bilgilerin bulunması
            if en_yuksek_bedelle_satilan_emlak > o_ay_en_yuksek_bedelle_satilan_emlagin_bedeli:
                o_ay_en_yuksek_bedelle_satilan_emlagin_bedeli = en_yuksek_bedelle_satilan_emlak
                en_yuksek_bedelle_satilan_emlak_danisman_adi = danisman_ad_soyad
                if emlak_tipi == 'a' or emlak_tipi == 'A':
                    en_yuksek_bedelle_satilan_emlak_tipi = 'Arsa'
                elif emlak_tipi == 'i' or emlak_tipi == 'İ':
                    en_yuksek_bedelle_satilan_emlak_tipi = 'İş Yeri'
                else:
                    en_yuksek_bedelle_satilan_emlak_tipi = 'Konut'

            # o ay en çok satış yapan danışmanın verilerin bulunması
            if satilan_emlak_adedi > en_cok_satis_yapan_danismanin_satis_adedi:
                en_cok_satis_yapan_danisman_adi = danisman_ad_soyad
                en_cok_satis_yapan_danismanin_satis_adedi = satilan_emlak_adedi
                en_cok_satis_yapan_danisman_bedelleri = bir_danismanin_toplam_satis_bedeli

        else:  # işlem türü == kira
            kiralanan_emlak_adedi += 1
            bir_danisman_kira_toplam_bedel += satis_kira_bedeli
            emlak_komisyonu_kira += satis_kira_bedeli
            if emlak_tipi == 'k' or emlak_tipi == 'K':
                kiralanan_konut_sayisi += 1
                kiralanan_konut_bedeli += satis_kira_bedeli
                # en yüksek bedelle kiralanan konutun kira bedelinin alınması
                if satis_kira_bedeli > en_yuksek_bedelli_kiralanan_konut:
                    en_yuksek_bedelli_kiralanan_konut = satis_kira_bedeli
                if satis_kira_bedeli > ASGARI_UCRET:
                    asgari_ucretten_fazla_kiralik_konut_say += 1
            elif emlak_tipi == 'i' or emlak_tipi == 'İ':
                toplam_kiralanan_isyeri_say += 1
            else:
                toplam_kiralanan_arsa_say += 1

        yeni_emlak = input("Sattığınız/kiraladığınız başka emlak var mı? (E/e/H/h):")
        while yeni_emlak not in ['e', 'E', 'h', 'H']:
            yeni_emlak = input("Hatalı veri girdiniz, sattığınız/kiraladığınız başka emlak var mı? (E/e/H/h):")

    if danisman_satis_yapti_mi != True:
        satis_yapmayan_danisman_sayisi += 1

    # danışman verilerinin hesaplanması
    satilan_emlak_adedinin_kiralanana_orani_yuzde = format((satilan_emlak_adedi/(satilan_emlak_adedi + kiralanan_emlak_adedi))*100, '.2f')
    kiralanan_emlak_adedinin_satilana_orani_yuzde = format((kiralanan_emlak_adedi/(kiralanan_emlak_adedi + satilan_emlak_adedi))*100, '.2f')
    emlak_komisyonu_satis = (satilan_konut_bedeli + satilan_arsa_bedeli + satilan_isyeri_bedeli)*SATIS_KOMISYON_ORANI
    emlak_komisyonu = emlak_komisyonu_kira + emlak_komisyonu_satis
    prim = emlak_komisyonu*PRIM_ORANI
    yapilan_kota = emlak_komisyonu

    # danışman kotayı doldurduysa aylik toplam ücretine ikramiye eklenir
    if yapilan_kota >= kota:
        kota_dolduruldu_mu = True
        kota_dolduran_sayisi += 1
        aylik_toplam_ucret = maas + prim + IKRAMIYE
    else:
        kota_dolduruldu_mu = False
        aylik_toplam_ucret_ikramiyesiz = maas + prim

    # primi maaşından yüksek olanların sayısı bulunur
    if prim > maas:
        primi_maasindan_yuksek_olanlar += 1

    # en yüksek prim alan danışman bulunur
    if prim > en_yuksek_prim:
        en_yuksek_prim_danisman_ad_soyad = danisman_ad_soyad
        en_yuksek_prim_alanin_maasi = maas
        en_yuksek_prim = prim
        if kota_dolduruldu_mu == True:
            en_yuksek_prim_alanin_aylik_toplam_ucreti = aylik_toplam_ucret
        else:
            en_yuksek_prim_alanin_aylik_toplam_ucreti = aylik_toplam_ucret_ikramiyesiz

    # ilk danışmanın primi en düşük prim olarak alınır
    if danisman_sayisi == 1:
        en_dusuk_prim = prim
    # en düşük prim alan danışman bulunur
    if prim <= en_dusuk_prim:
        en_dusuk_prim_danisman_ad_soyad = danisman_ad_soyad
        en_dusuk_prim_alanin_maasi = maas
        en_dusuk_prim = prim
        if kota_dolduruldu_mu == True:
            en_dusuk_prim_alanin_aylik_toplam_ucreti = aylik_toplam_ucret
        else:
            en_dusuk_prim_alanin_aylik_toplam_ucreti = aylik_toplam_ucret_ikramiyesiz

    # o ay en yüksek bedelle kiralanan konutun bedeli ve kiralayan danışman bulunur
    if o_ay_en_yuksek_bedelli_kiralanan_konut < en_yuksek_bedelli_kiralanan_konut:
        o_ay_en_yuksek_bedelli_kiralanan_konut = en_yuksek_bedelli_kiralanan_konut
        en_yuksek_bedelle_kiralanan_konut_danisman_adi = danisman_ad_soyad

    # o ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısının bulunması
    if kiralanan_emlak_adedi >= MIN_KIRA_ADET or bir_danisman_kira_toplam_bedel >= MIN_KIRA_TUTAR:
        min_kira_kosullarini_saglayanlarin_sayisi += 1

    # her danışman için istenilen bilgilerin yazdırılması
    print("{kisi}. Emlak danışmanının adı-soyadı: ".format(kisi=danisman_sayisi), danisman_ad_soyad)
    print("o ay sattığı emlak adedi:", satilan_emlak_adedi, ", kiraladığı emlak adedi:", kiralanan_emlak_adedi,
          ", sattığı emlak adedinin oranı: %", satilan_emlak_adedinin_kiralanana_orani_yuzde, ", kiraldığı emlak adedinin oranı: % ", kiralanan_emlak_adedinin_satilana_orani_yuzde)
    print("o ay sattığı konut bedelleri:", format(satilan_konut_bedeli, ',.2f'), "TL,", ", işyeri bedelleri:", format(satilan_isyeri_bedeli, ',.2f') , "TL,", ", arsa bedelleri:", format(satilan_arsa_bedeli, ',.2f'), "TL")
    print("o ay kiraladığı konutların ortalama kira bedeli:", format((kiralanan_konut_bedeli/kiralanan_konut_sayisi), ',.2f'), "TL")
    print("o ay en yüksek bedelle kiraladığı konutun kira bedeli:", format(en_yuksek_bedelli_kiralanan_konut, ',.2f'), "TL")
    print("o ay alacağı maaş:", format(maas, ',.2f'), "TL")
    print("o ay alacağı primi:", format(prim, ',.2f'), "TL")
    print("o ay kotası:", format(kota, ',.2f'), "TL")
    print("o ay acenteye kazandırdığı toplam komisyon tutarı:", format(emlak_komisyonu, ',.2f'), "TL")
    if kota_dolduruldu_mu == True:
        print("o ay kotasını doldurmuştur. ")
        print("Alacağı ikramiye tutarı:", format(IKRAMIYE, ',.2f'), "TL")
        print("o ay alacağı toplam ücret:", format(aylik_toplam_ucret, ',.2f'), "TL")
    else:
        print("o ay kotasını dolduramamıştır. ")
        print("o ay alacağı toplam ücret:", format(aylik_toplam_ucret_ikramiyesiz, ',.2f'), "TL")

    toplam_kiralanan_konut_say += kiralanan_konut_sayisi
    satilan_konut_bedel_toplami += satilan_konut_bedeli
    satilan_isyeri_bedel_toplami += satilan_isyeri_bedeli
    satilan_arsa_bedel_toplami += satilan_arsa_bedeli
    tum_danismanlarin_aylik_toplam_ucreti += aylik_toplam_ucret
    tum_danismanlarin_aylik_toplam_ucreti_ikramiyesiz += aylik_toplam_ucret_ikramiyesiz
    toplam_ucretlerin_toplami = tum_danismanlarin_aylik_toplam_ucreti + tum_danismanlarin_aylik_toplam_ucreti_ikramiyesiz
    toplam_komisyon += emlak_komisyonu

# istenilen değerlerin hesaplanması ve formatlanması
konut_sayisinin_satilma_orani = format((toplam_satilan_konut_say/(toplam_satilan_konut_say + toplam_kiralanan_konut_say))*100, '.2f')
isyeri_sayisinin_satilma_orani = format((toplam_satilan_isyeri_say/(toplam_satilan_isyeri_say + toplam_kiralanan_isyeri_say))*100, '.2f')
arsa_sayisinin_satilma_orani = format((toplam_satilan_arsa_say/(toplam_satilan_arsa_say + toplam_kiralanan_arsa_say))*100, '.2f')
toplam_satilan_konut_bedeli_ortalamasi = format((satilan_konut_bedel_toplami/toplam_satilan_konut_say), ',.2f')
toplam_satilan_isyeri_bedeli_ortalamasi = format((satilan_isyeri_bedel_toplami/toplam_satilan_isyeri_say), ',.2f')
toplam_satilan_arsa_bedeli_ortalamasi = format((satilan_arsa_bedel_toplami/toplam_satilan_arsa_say), ',.2f')
asgari_ucretten_fazla_kiralik_konut_say_oran = format((asgari_ucretten_fazla_kiralik_konut_say/toplam_kiralanan_konut_say)*100, '.2f')
satis_yapmayan_danisman_orani = format((satis_yapmayan_danisman_sayisi/emlak_danisman_sayisi)*100, '.2f')
kotasini_dolduranlarin_orani = format((kota_dolduran_sayisi/emlak_danisman_sayisi)*100, '.2f')
primi_maasindan_yuksek_olanlarin_orani = format((primi_maasindan_yuksek_olanlar/emlak_danisman_sayisi)*100, '.2f')
toplam_ucretlerin_toplaminin_ortalamasi = format(toplam_ucretlerin_toplami/emlak_danisman_sayisi, ',.2f')

print('')
print('-------------------------------')
print('')

# Tüm emlak danışmanları için veri girişleri bittikten sonra istenilen istatistiksel bilgilerin yazdırılması
print("Tüm emlak danışmanları için veri girişleri bitmiştir.")
print("")
print("Toplam satılan konut sayısı:", toplam_satilan_konut_say, ", Toplam kiralanan konut sayısı:", toplam_kiralanan_konut_say, ", Satılma oranı:", "%", konut_sayisinin_satilma_orani)
print("Toplam satılan işyeri sayısı:", toplam_satilan_isyeri_say, ", Toplam kiralanan işyeri sayısı:", toplam_kiralanan_isyeri_say, ", Satılma oranı:", "%", isyeri_sayisinin_satilma_orani)
print("Toplam satılan arsa sayısı:", toplam_satilan_arsa_say, ", Toplam kiralanan arsa sayısı:", toplam_kiralanan_arsa_say, ", Satılma oranı:", "%", arsa_sayisinin_satilma_orani)
print("o ay satılan konutların satış bedelleri toplamı:", format(satilan_konut_bedel_toplami, ',.2f'), "TL", ", ortalaması:", toplam_satilan_konut_bedeli_ortalamasi, "TL")
print("o ay satılan işyerilerinin satış bedelleri toplamı:", format(satilan_isyeri_bedel_toplami, ',.2f'), "TL", ", ortalaması:", toplam_satilan_isyeri_bedeli_ortalamasi, "TL")
print("o ay satılan arsaların satış bedelleri toplamı:", format(satilan_arsa_bedel_toplami, ',.2f'), "TL", ", ortalaması:", toplam_satilan_arsa_bedeli_ortalamasi, "TL")
print("o ay en yüksek bedelle satılan emlak tipi:", en_yuksek_bedelle_satilan_emlak_tipi, ", satış bedeli:",
      format(o_ay_en_yuksek_bedelle_satilan_emlagin_bedeli, ',.2f'), "TL", ", satışı yapan danışmanın adı-soyadı:", en_yuksek_bedelle_satilan_emlak_danisman_adi)
print("o ay en yüksek bedelle kiralanan konutun kira bedeli:", format(o_ay_en_yuksek_bedelli_kiralanan_konut, ',.2f'), "TL", ", kiralayan danışmanın adı-soyadı:", en_yuksek_bedelle_kiralanan_konut_danisman_adi)
print("o ay kiralanan konutlardan kira bedeli, aylık asgari net ücretten yüksek olan konutların sayısı:",asgari_ucretten_fazla_kiralik_konut_say,
      "ve kiralanan konutlar içindeki oranı", "%", asgari_ucretten_fazla_kiralik_konut_say_oran)
print("o ay hiç satış yapamayan danışmanların sayısı:", satis_yapmayan_danisman_sayisi, "ve tüm danışmanlar içindeki oranı:", "%", satis_yapmayan_danisman_orani)
print("o ay satış adeti olarak en çok satış yapan danışmanın adı-soyadı:", en_cok_satis_yapan_danisman_adi, ", sattığı emlak sayısı", en_cok_satis_yapan_danismanin_satis_adedi,
      "ve toplam satış bedeli", format(en_cok_satis_yapan_danisman_bedelleri, ',.2f'), "TL")
print("o ay satış bedeli olarak en çok satış yapan danışmanın adı-soyadı", en_cok_satis_bedeli_yapan_danismanin_adi, ", sattığı emlak sayısı:",
      en_cok_satis_bedeli_yapan_danisman_emlak_say, "ve toplam satış bedeli:", format(en_cok_satis_bedeli_yapan_danisman_toplam_satis_bedeli, ',.2f'), "TL")
print("o ay kotasını dolduran danışmanların sayısı:", kota_dolduran_sayisi, "ve tüm danışmanlar içindeki oranı:", "%", kotasini_dolduranlarin_orani)
print("o ay primi maaşından yüksek olan danışmanların sayısı:", primi_maasindan_yuksek_olanlar, "ve tüm danışmanlar içindeki oranı:", "%", primi_maasindan_yuksek_olanlarin_orani)
print("o ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı:", min_kira_kosullarini_saglayanlarin_sayisi)
print("o ay en yüksek prim alan danışmanın adı soyadı:", en_yuksek_prim_danisman_ad_soyad, ", maaşı:", format(en_yuksek_prim_alanin_maasi, ',.2f'), "TL",
      ", primi:", format(en_yuksek_prim, ',.2f'), "TL", "ve aylık toplam ücret", format(en_yuksek_prim_alanin_aylik_toplam_ucreti, ',.2f'))
print("o ay en düşük prim alan danışmanın adı soyadı:", en_dusuk_prim_danisman_ad_soyad, ", maaşı:", format(en_dusuk_prim_alanin_maasi, ',.2f'), "TL",
      ", primi:", format(en_dusuk_prim, ',.2f'), "TL", "ve aylık toplam ücret", format(en_dusuk_prim_alanin_aylik_toplam_ucreti, ',.2f'))
print("o ay tüm emlak danışmanlarına ödenecek toplam ücretlerin toplamı:", format(toplam_ucretlerin_toplami, ',.2f'), "TL", " ve ortalaması:", toplam_ucretlerin_toplaminin_ortalamasi, "TL")
print("o ay acentenin kazandığı toplam komisyon:", format(toplam_komisyon, ',.2f'), "TL")
