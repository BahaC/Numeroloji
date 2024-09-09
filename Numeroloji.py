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
kelime_grubu = "elon musk"

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


def toplam_11_mi(Ekleyendizi,EklenenDizi):
    for i in range(len(Ekleyendizi)):
        for j in range(i + 1, len(Ekleyendizi)):
            if Ekleyendizi[i] + Ekleyendizi[j] == 11:
                EklenenDizi.append(11)
                del Ekleyendizi[j]
                del Ekleyendizi[i]
                break
    

# Her kelimeyi işlemek için döngü
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
    anaK = rakam_toplami(sesli_toplam)
    yanK = rakam_toplami(sessiz_toplam)
    print(f"  Ana Kulvar: {anaK}")
    print(f"  Yan Kulvar: {yanK}")
    print()

# 11in katı olmayan sayıların olduğu elemanları diziye at, dizide toplamı 11 eden herhangi iki değeri bul
toplam_11_mi(sesli_rakam_toplamlari,sesli_11_ve_kati)
toplam_11_mi(sessiz_rakam_toplamlari,sessiz_11_ve_kati)

if sesli_rakam_toplamlari and sesli_11_ve_kati:
    y = sum(sesli_11_ve_kati) + sum(sesli_rakam_toplamlari)
    print(f"Ana Kulvar: {sum(sesli_rakam_toplamlari)}+{sum(sesli_11_ve_kati)} / {rakam_toplami(y)}")
elif sesli_rakam_toplamlari:
    toplam1 = sum(sesli_rakam_toplamlari)
    print(f"Ana Kulvar: {rakam_toplami(toplam1)}")
elif sesli_11_ve_kati:
    toplam2 = sum(sesli_11_ve_kati)
    print(f"Ana Kulvar: {toplam2} / {rakam_toplami(toplam2)}")

if sessiz_rakam_toplamlari and sessiz_11_ve_kati:
    x = sum(sessiz_rakam_toplamlari) + sum(sessiz_11_ve_kati)
    print(f"Yan Kulvar: {sum(sessiz_rakam_toplamlari)}+{sum(sessiz_11_ve_kati)} / {rakam_toplami(x)}")
elif sessiz_rakam_toplamlari:
    toplam3 = sum(sessiz_rakam_toplamlari)
    print(f"Yan Kulvar: {rakam_toplami(toplam3)}")
elif sessiz_11_ve_kati:
    toplam4 = sum(sessiz_11_ve_kati)
    print(f"Yan Kulvar: {toplam4} / {rakam_toplami(toplam4)}")

