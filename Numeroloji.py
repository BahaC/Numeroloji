# Harflerin sayısal değerlerini tanımlayan sözlük
harf_degerleri = {
    'a': 1, 'j': 1, 's': 1, 'ş': 1,
    'b': 2, 'k': 2, 't': 2, 
    'c': 3, 'ç': 3, 'l': 3, 'u': 3, 'ü': 3,
    'd': 4, 'm': 4, 'v': 4,
    'e': 5, 'n': 5, 'w': 5,
    'f': 6, 'o': 6, 'ö': 6, 'x': 6,
    'g': 7, 'ğ': 7, 'p': 7, 'y': 7,
    'h': 8, 'q': 8, 'z': 8,
    'ı': 9, 'i': 9, 'r': 9
}

# Sayının rakamlar toplamını hesaplayan fonksiyon 
def rakam_toplami(sayi):
    return sum(int(rakam) for rakam in str(sayi))

# Sesli harfler listesi
sesli_harfler = "aeıioöuü"

# İsim ve doğum tarihi
kelime_grubu = "izel yıldız"
tarih = "25.06.1970"                                            #DOĞUM TARİHİ --------------------------------


# Değerlerin geçtiği frekansları tutmak için bir sözlük
deger_sayaci = {}

# String içindeki harfleri işleme
for harf in kelime_grubu.lower() :
    # Boşlukları atla
    if harf == " ":
        continue
    
    # Harf harf_degerleri sözlüğünde mi?
    if harf in harf_degerleri:
        deger = harf_degerleri[harf]
        # Sayacı artırma
        if deger in deger_sayaci:
            deger_sayaci[deger] += 1
        else:
            deger_sayaci[deger] = 1

# 1'den 9'a kadar tüm sayısal değerleri kontrol et
print()
for i in range(1, 10):
    if i in deger_sayaci:
        print(f"Değer {i} toplam {deger_sayaci[i]} kez geçiyor.")
    else:
        print(f"Değer {i} bulunmuyor.")
print()
# 11 ya da 11'in katı olan değerleri saklamak için listeler
sesli_11_ve_kati = []
sessiz_11_ve_kati = []

# Rakamlarının toplamını tutmak için listeler
sesli_rakam_toplamlari = []
sessiz_rakam_toplamlari = []


def iki_haneli_rakamlar(sayi):
    # Sayıyı string'e çevirip ayrı rakamları alıyoruz
    onlar_basamagi = sayi // 10  # Onlar basamağı
    birler_basamagi = sayi % 10  # Birler basamağı
    
    return birler_basamagi, onlar_basamagi 

def toplam_11_mi(Ekleyendizi,EklenenDizi):
    for i in range(len(Ekleyendizi)):
        for j in range(i + 1, len(Ekleyendizi)):
            if Ekleyendizi[i] + Ekleyendizi[j] == 11:
                EklenenDizi.append(11)
                del Ekleyendizi[j]
                del Ekleyendizi[i]
                break
AnaKulvarDizi = []    
# Her kelimeyi işlemek için döngü
anaK = 0
yanK = 0
sayac_11 = 0
sayac_22 = 0
for kelime in kelime_grubu.lower().split():
    sesli_toplam = 0
    sessiz_toplam = 0

    # Her harfi kontrol et
    for harf in kelime:
        if harf in harf_degerleri:  # Harfin değeri var mı?
            if harf in sesli_harfler:  # Sesli harf mi?
                sesli_toplam += harf_degerleri[harf]
            else:  # Sessiz harf mi?
                sessiz_toplam += harf_degerleri[harf]

    # Sesli harf toplamı 11 ya da 11'in katı mı?
    #if sesli_toplam % 11 == 0 and sesli_toplam != 0:
    if sesli_toplam in [11, 22, 33]:
        sesli_11_ve_kati.append(sesli_toplam)
        if sesli_toplam == 11:
            sayac_11 += 1
        if sesli_toplam == 22 and sayac_11 == 1:
            sayac_11 += 1
    else:
        if sesli_rakam_toplamlari and sesli_toplam + sesli_rakam_toplamlari[0] == 11:
            sayac_11 += 1
        sesli_rakam_toplamlari.append(sum(int(rakam) for rakam in str(rakam_toplami(sesli_toplam))))

    # Sessiz harf toplamı 11 ya da 11'in katı mı?
    if sessiz_toplam in [11, 22, 33]:  
        sessiz_11_ve_kati.append(sessiz_toplam)
    else:
        if sum(int(rakam) for rakam in str(sessiz_toplam)) % 11 == 0:
            sessiz_11_ve_kati.append(sum(int(rakam) for rakam in str(sessiz_toplam)))
        else:
            if sessiz_toplam > 9:
                sessiz_toplam = rakam_toplami(sessiz_toplam)    
            sessiz_rakam_toplamlari.append(sum(int(rakam) for rakam in str(rakam_toplami(sessiz_toplam))))

    # Sonuçları yazdır
    #print(f"\nKelime: {kelime}")
    birler3, onlar3 = iki_haneli_rakamlar(sesli_toplam)
    #anaK = kati_mi_11in(sesli_toplam, anaK)
    #yanK = kati_mi_11in(sessiz_toplam, yanK)
    #AnaKulvarDizi.extend([birler3, onlar3])


    # Eğer kelimenin anakulvarı 11,22 ya da 33 ise tipolojiye değerleri direk ekle (2 adet 1,2 ya da 3 ekle)
    # Aksi durumda iki haneli bir değerse rakamlar toplamını, tek haneyse birler basamağını ekle
    if sesli_toplam in [11, 22, 33]: 
        #AnaKulvarDizi.extend([birler3, onlar3])
        AnaKulvarDizi.append(birler3)
        AnaKulvarDizi.append(onlar3)
    elif onlar3 > 0:
        AnaKulvarDizi.append(rakam_toplami(sesli_toplam))       # Buralarda AnaKulvarDizi'ye değil sesli_rakam_toplamlarına yaz
    else: 
        AnaKulvarDizi.append(birler3)


# 11in katı olmayan sayıların olduğu elemanları diziye at, dizide toplamı 11 eden herhangi iki değeri bul
toplam_11_mi(sesli_rakam_toplamlari,sesli_11_ve_kati)
toplam_11_mi(sessiz_rakam_toplamlari,sessiz_11_ve_kati)

                                                #PİN KODU HESAPLAMA

#Tarihin tüm rakamlar toplamı
def tarih_rakam_toplami(tarih):
    # Tarihteki rakamları alıyoruz
    rakamlar = [int(char) for char in tarih if char.isdigit()]
    # Rakamları topluyoruz
    return sum(rakamlar)

#Gün - Ay - Yıl olarak ayrı ayrı değerlerin toplamı
def tarih_ayrik_toplam(tarih):
    # Tarihi gün, ay ve yıl olarak ayırıyoruz
    gun, ay, yil = tarih.split('.')   
    # Gün, ay ve yılın rakamlarını topluyoruz
    gun_toplam = sum(int(char) for char in gun)
    ay_toplam = sum(int(char) for char in ay)
    yil_toplam = sum(int(char) for char in yil)
    
    return gun_toplam, ay_toplam, yil_toplam

# Örnek tarih
gun_toplam, ay_toplam, yil_toplam = tarih_ayrik_toplam(tarih)   

# Örnek sayı
TDM = f"{tarih_rakam_toplami(tarih)} + {rakam_toplami(tarih_rakam_toplami(tarih))}"
TDM1 = tarih_rakam_toplami(tarih)
TDM2 = rakam_toplami(tarih_rakam_toplami(tarih))

onlar, birler = iki_haneli_rakamlar(TDM1)

hane4 = rakam_toplami(gun_toplam + ay_toplam + yil_toplam)    

Tipoloji=[rakam_toplami(gun_toplam), rakam_toplami(ay_toplam), rakam_toplami(yil_toplam), 
          rakam_toplami(hane4), rakam_toplami(hane4 + gun_toplam), 
          rakam_toplami(gun_toplam + ay_toplam), rakam_toplami(ay_toplam + yil_toplam), rakam_toplami(hane4 + ay_toplam),
          onlar, birler]

if TDM2 >= 10:
    onlar1, birler1 = iki_haneli_rakamlar(TDM2)
    #Tipoloji.extend([onlar1, birler1])
    Tipoloji.append(onlar1)
    Tipoloji.append(birler1)
else:
    Tipoloji.append(TDM2)

def liste_kopyala(liste1, liste2):
    # liste1'in elemanlarını liste2'ye ekliyoruz        # 10lu değeri kopylama işlemi (yanlış yer)
    for eleman in liste1:
        liste2.append(eleman)

liste_kopyala(AnaKulvarDizi, Tipoloji)    ##  Anakulvar dizi elemanlarını [10,8,2] gibi alıyor, [1,8,2] olacak

if sesli_rakam_toplamlari and sesli_11_ve_kati:
    toplam11 = sum(sesli_11_ve_kati)
    toplamD = sum(sesli_rakam_toplamlari)
    if toplamD > 9 and toplamD not in [11, 22, 33]:
        toplamD = rakam_toplami(toplamD)
    elif toplamD in [11, 22]:
        toplam11 = toplam11 + toplamD
        print(f"Ana Kulvar: {toplam11} / {rakam_toplami(rakam_toplami(toplam11))}")
        birler5, onlar5 = iki_haneli_rakamlar(toplam11)
        Tipoloji.append(birler5)
        if onlar5 > 0:
            Tipoloji.append(onlar5)
    if toplamD < 10:
        print(f"Ana Kulvar: {toplam11} + {toplamD} / {rakam_toplami(rakam_toplami(toplamD + toplam11))}")
        birlerr, onlarr = iki_haneli_rakamlar(toplamD)
        Tipoloji.append(birlerr)
        if onlarr > 0:
            Tipoloji.append(onlarr)

elif sesli_rakam_toplamlari:
    sesli_rakam_toplamlarii = sum(sesli_rakam_toplamlari)
    if sesli_rakam_toplamlarii > 9 and sesli_rakam_toplamlarii not in [11, 22, 33]:
        sesli_rakam_toplamlarii = rakam_toplami(sesli_rakam_toplamlarii)
        print(f"Ana Kulvar: {sesli_rakam_toplamlarii}")
        birrlerr, onnlarr = iki_haneli_rakamlar(sesli_rakam_toplamlarii)
        Tipoloji.append(birrlerr)
        if onnlarr > 0:
            Tipoloji.append(onnlarr)
    elif sesli_rakam_toplamlarii in [11, 22, 33]:
        print(f"Ana Kulvar: {sesli_rakam_toplamlarii} / {rakam_toplami(sesli_rakam_toplamlarii)}")
        birrler, onnlar = iki_haneli_rakamlar(sesli_rakam_toplamlarii)
        Tipoloji.append(birrler)
        if onnlar > 0:
            Tipoloji.append(onnlar)
    elif sesli_rakam_toplamlarii < 10: 
        print(f"Ana Kulvar: {sesli_rakam_toplamlarii}")
        Tipoloji.append(sesli_rakam_toplamlarii)
        
elif sesli_11_ve_kati:
    if sum(sesli_11_ve_kati) >= 44:
        print(f"Ana Kulvar: {sesli_11_ve_kati[0]} + {sesli_11_ve_kati[1]} = {sum(sesli_11_ve_kati)} / {rakam_toplami(sesli_11_ve_kati[0] + sesli_11_ve_kati[1])}")
        birler, onlar = iki_haneli_rakamlar(sesli_11_ve_kati[0])
        birler2, onlar2 = iki_haneli_rakamlar(sesli_11_ve_kati[1])
        birler3, onlar3 = iki_haneli_rakamlar(sesli_11_ve_kati[0] + sesli_11_ve_kati[1])
        Tipoloji.append(birler)
        Tipoloji.append(birler2)
        Tipoloji.append(birler3)
        Tipoloji.append(onlar)
        Tipoloji.append(onlar2)
        Tipoloji.append(onlar3)
    else:
        sesli_11_ve_katii = sum(sesli_11_ve_kati)
        print(f"Ana Kulvar: {sesli_11_ve_katii} / {rakam_toplami(sesli_11_ve_katii)}")          # HATANIN DÜŞTÜĞÜ YER
        birler4, onlar4 = iki_haneli_rakamlar(sesli_11_ve_katii)
        Tipoloji.append(birler4)  # "rakam_toplami(toplam2)" 22 değeri buradan geliyor VİDEOLARI İNCELE İKİ HANELİ OLAN SAYILARIN RAKAMLARINI AL
        if onlar4 > 0:
            Tipoloji.append(onlar4)

if sessiz_rakam_toplamlari and sessiz_11_ve_kati:
    toplam11s = sum(sessiz_11_ve_kati)
    toplamDs = sum(sessiz_rakam_toplamlari)
    if toplamDs > 9 and toplamDs not in [11, 22, 33]:
        toplamDs = rakam_toplami(toplamDs)
    elif toplamDs in [11, 22]:
        toplam11s = toplam11s + toplamDs
        print(f"Yan Kulvar: {toplam11s} / {rakam_toplami(toplam11s)}")
        birler7, onlar7 = iki_haneli_rakamlar(toplam11s)
        #Tipoloji.append(onlar7, birler7)
    if toplamDs < 10:
        print(f"Yan Kulvar: {toplam11s} + {toplamDs} / {rakam_toplami(toplamDs + toplam11s)}")
        birlerrr, onlarrr = iki_haneli_rakamlar(toplamDs)
        #Tipoloji.append([birlerrr, onlarrr])

elif sessiz_rakam_toplamlari:
    sessiz_rakam_toplamlarii = sum(sessiz_rakam_toplamlari)
    if sessiz_rakam_toplamlarii > 9 and sessiz_rakam_toplamlarii not in [11, 22, 33]:
        sessiz_rakam_toplamlarii = rakam_toplami(sessiz_rakam_toplamlarii)
        print(f"Yan Kulvar: {sessiz_rakam_toplamlarii}")
        birrlerr, onnlarr = iki_haneli_rakamlar(sessiz_rakam_toplamlarii)
        #Tipoloji.append([birrlerr, onnlarr])
    elif sessiz_rakam_toplamlarii in [11, 22, 33]:
        print(f"Yan Kulvar: {sessiz_rakam_toplamlarii} / {rakam_toplami(sessiz_rakam_toplamlarii)}")
        birrler, onnlar = iki_haneli_rakamlar(sessiz_rakam_toplamlarii)
        #Tipoloji.extend([birrler, onnlar])
    elif sessiz_rakam_toplamlarii < 10: 
        print(f"Yan Kulvar: {sessiz_rakam_toplamlarii}")
        #Tipoloji.append(sessiz_rakam_toplamlarii)

elif sessiz_11_ve_kati:
    sessiz_11_ve_katii = sum(sessiz_11_ve_kati)
    print(f"Yan Kulvar: {sessiz_11_ve_kati[0]} + {sessiz_11_ve_kati[1]} = {sessiz_11_ve_katii} / {rakam_toplami(sessiz_11_ve_katii)}")  
    #birlers, onlars = iki_haneli_rakamlar(sessiz_11_ve_katii)
    #Tipoloji.extend([birlers, onlars]) 


def dizi_elemanlarini_yazdir(dizi):
    for eleman in dizi:
        print(eleman)

if sayac_11 == 2:
    Tipoloji.append(1)
    Tipoloji.append(1)
    Tipoloji.append(1)
    Tipoloji.append(1)

print()
for i in range(0, 10):
    adet = Tipoloji.count(i)
    print(f"{i} değerinden {adet} adet var")

#dizi_elemanlarini_yazdir(Tipoloji)
