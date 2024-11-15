# def ayir_cift_tek(dizi):
#     ciftler = []
#     tekler = []

#     for sayi in dizi:
#         if sayi % 2 == 0:
#             ciftler.append(sayi)
#         else:
#             tekler.append(sayi)

#     return ciftler, tekler

# print(ayir_cift_tek([1, 2, 3, 4, 5, 6]))  # Çıktı: ([2, 4, 6], [1, 3, 5])
















# def karakter_sayisi(metin, karakter):
#     return metin.count(karakter)

# print(karakter_sayisi("merhaba dünya", "a"))  # Çıktı: 2


















# def en_buyuk_ve_kucuk(dizi):
#     if len(dizi) == 0:
#         return "Dizi boş!"

#     en_buyuk = max(dizi)
#     en_kucuk = min(dizi)

#     return en_buyuk, en_kucuk

# print(en_buyuk_ve_kucuk([1, 5, 3, -2, 9]))  # Çıktı: (9, -2)























# def bosluk_temizle(metin):
#     return metin.strip()

# print(bosluk_temizle("   Merhaba Dünya   "))  # Çıktı: Merhaba Dünya



























# def en_uzun_kelime(dizi):
#     en_uzun = ""
#     for kelime in dizi:
#         if len(kelime) > len(en_uzun):
#             en_uzun = kelime

#     return en_uzun

# print(en_uzun_kelime(["elma", "armut", "çilek", "karpuz"]))  # Çıktı: karpuz



















# def a_ile_baslayanlar(dizi):
#     sayac = 0
#     for kelime in dizi:
#         if kelime.lower().startswith('a'):
#             sayac += 1

#     return sayac

# print(a_ile_baslayanlar(["armut", "elma", "anahtar", "kiraz"]))  # Çıktı: 2




















# def yazıcı():
#     def yaz(mesaj):
#         print(mesaj)
#     return yaz













# def kapsayıcı_fonk():
#     non_local_değişken = 1

#     def iç_fonk():
#         non_local_değişken = 2
#         print(non_local_değişken)

#     return iç_fonk

def x():
    global t
    t = 5

x()

print(t)




# def toplama(x):
#      r = x**2
#      return lambda  : r -4 , r
# result = toplama(5)
# print(result[0]())




# def topl(x):
#     x = x**2
#     def cıka():
#         return x -5
#     return cıka