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

# Verilen kelime grubu
kelime_grubu = "nezaket nezahat ünal"

# Değerlerin geçtiği frekansları tutmak için bir sözlük
deger_sayaci = {}

# String içindeki harfleri işleme
for harf in kelime_grubu:
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

# 11 ya da 11'in katı olan değerleri saklamak için listeler
sesli_11_ve_kati = []
sessiz_11_ve_kati = []

# Rakamlarının toplamını tutmak için listeler
sesli_rakam_toplamlari = []
sessiz_rakam_toplamlari = []

"""def kati_mi_11in(sayi1, sayi2):
    if sayi1 not in [11, 22, 33]:
        if sayi1 > 9:
            birler = sayi1 // 10
            onlar = sayi1 % 10
    else:
        
    return birler, onlar
"""

def iki_haneli_rakamlar(sayi):
    # Sayıyı string'e çevirip ayrı rakamları alıyoruz
    onlar_basamagi = sayi // 10  # Onlar basamağı
    birler_basamagi = sayi % 10  # Birler basamağı
    
    return onlar_basamagi, birler_basamagi

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
    if sesli_toplam % 11 == 0 and sesli_toplam != 0:
        sesli_11_ve_kati.append(sesli_toplam)
    else:
        sesli_rakam_toplamlari.append(sum(int(rakam) for rakam in str(sesli_toplam)))

    # Sessiz harf toplamı 11 ya da 11'in katı mı?
    if sessiz_toplam % 11 == 0 and sessiz_toplam != 0:
        sessiz_11_ve_kati.append(sessiz_toplam)
    else:
        sessiz_rakam_toplamlari.append(sum(int(rakam) for rakam in str(sessiz_toplam)))

    # Sonuçları yazdır
    print(f"\nKelime: {kelime}")
    birler3, onlar3 = iki_haneli_rakamlar(sesli_toplam)
    AnaKulvarDizi = 
    #anaK = kati_mi_11in(sesli_toplam, anaK)
    #yanK = kati_mi_11in(sessiz_toplam, yanK)
    print(f"  Ana Kulvar: {anaK}")
    print(f"  Yan Kulvar: {yanK}")
    print()

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
tarih = "15.11.1982"                                            #DOĞUM TARİHİ --------------------------------
gun_toplam, ay_toplam, yil_toplam = tarih_ayrik_toplam(tarih)   

# Örnek sayı
TDM = f"{tarih_rakam_toplami(tarih)} + {rakam_toplami(tarih_rakam_toplami(tarih))}"
TDM1 = tarih_rakam_toplami(tarih)
TDM2 = rakam_toplami(tarih_rakam_toplami(tarih))


onlar, birler = iki_haneli_rakamlar(TDM1)

print(f"1. Hane: {rakam_toplami(gun_toplam)}")
print(f"2. Hane: {rakam_toplami(ay_toplam)}")
print(f"3. Hane: {rakam_toplami(yil_toplam)}")
hane4 = rakam_toplami(gun_toplam + ay_toplam + yil_toplam)
print(f"4. Hane: {hane4}")
print(f"5. Hane: {rakam_toplami(hane4 + gun_toplam)}")
print(f"6. Hane: {rakam_toplami(gun_toplam + ay_toplam)}")
print(f"7. Hane: {rakam_toplami(ay_toplam + yil_toplam)}")
print(f"8. Hane: {rakam_toplami(hane4 + ay_toplam)}") # 6. ve 7. hane toplamı = hane4 + ay_toplam
print(f"TDM: {TDM}")

Tipoloji=[rakam_toplami(gun_toplam), rakam_toplami(ay_toplam), rakam_toplami(yil_toplam), 
          rakam_toplami(hane4), rakam_toplami(hane4 + gun_toplam), 
          rakam_toplami(gun_toplam + ay_toplam), rakam_toplami(ay_toplam + yil_toplam), rakam_toplami(hane4 + ay_toplam),
          onlar, birler]

if TDM2 >= 10:
    onlar1, birler1 = iki_haneli_rakamlar(TDM2)
    Tipoloji.extend([onlar1, birler1])
else:
    Tipoloji.extend(TDM2)

Tipoloji.extend([birler3, onlar3])

def liste_kopyala(liste1, liste2):
    # liste1'in elemanlarını liste2'ye ekliyoruz
    for eleman in liste1:
        liste2.append(eleman)

liste_kopyala(AnaKulvarDizi, Tipoloji)    

if sesli_rakam_toplamlari and sesli_11_ve_kati:
    y = sum(sesli_11_ve_kati) + sum(sesli_rakam_toplamlari)
    print(f"Ana Kulvar: {sum(sesli_rakam_toplamlari)}+{sum(sesli_11_ve_kati)} / {rakam_toplami(y)}")
    Tipoloji.extend(sum(sesli_rakam_toplamlari), sum(sesli_11_ve_kati), rakam_toplami(y))
elif sesli_rakam_toplamlari:
    toplam1 = sum(sesli_rakam_toplamlari)
    print(f"Ana Kulvar: {rakam_toplami(toplam1)}")
    Tipoloji.append(rakam_toplami(toplam1))
elif sesli_11_ve_kati:
    toplam2 = sum(sesli_11_ve_kati)
    print(f"Ana Kulvar: {toplam2} / {rakam_toplami(toplam2)}")
    Tipoloji.extend([toplam2, rakam_toplami(toplam2)])        # VİDEOLARI İNCELE  İKİ HANELİ OLAN SAYILARIN RAKAMLARINI AL


if sessiz_rakam_toplamlari and sessiz_11_ve_kati:
    x = sum(sessiz_rakam_toplamlari) + sum(sessiz_11_ve_kati)
    print(f"Yan Kulvar: {sum(sessiz_rakam_toplamlari)}+{sum(sessiz_11_ve_kati)} / {rakam_toplami(x)}")
elif sessiz_rakam_toplamlari:
    toplam3 = sum(sessiz_rakam_toplamlari)
    print(f"Yan Kulvar: {rakam_toplami(toplam3)}")
elif sessiz_11_ve_kati:
    toplam4 = sum(sessiz_11_ve_kati)
    print(f"Yan Kulvar: {toplam4} / {rakam_toplami(toplam4)}")

def dizi_elemanlarini_yazdir(dizi):
    for eleman in dizi:
        print(eleman)

dizi_elemanlarini_yazdir(Tipoloji)
