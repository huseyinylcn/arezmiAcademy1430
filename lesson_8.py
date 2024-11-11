# while


# sayi = 0
# while sayi < 100 : 
#     print(sayi**2)
#     sayi += 1



# sayi = 0

# while True:
#     sayi+= 1
#     print(sayi)
#     if sayi == 100:
#         break



# x = 0
# while x < 10:
#     x += 1
#     if x == 6:
#         continue
#     print(x)



# x = 0
# while x < 10:
#     x += 1
#     print(x)
# else:
#     print("while döngüsü bitti. ")














# password = "123"
# x = 0
# while x < 3:
#     x+=1
#     inp = input("Lütfen şifrenizi giriniz .")
#     if inp == password:
#         print("Şİfre doğru")
#         break
#     else:
#         print("Şifreniz yanlış")
#         print(3 - x, "hakkınızız kaldı")
# else:
#     print("Hakkınız bitti ")






# filewrite = open("deneme.txt","w")

# while True:
#     inp = input("Yeni Şifrenizi giriniz: ")
#     if len(inp) >= 8:
#         print("Şifreniz belirlendi")
#         print(inp,file=filewrite)
#         break
#     else:
#         print("şifreniz 8 karakterden küçük olmamalı")







# while True:
#     print()
#     print(""" 
# carpma: 1
# bölme: 2
# toplama : 3
# çıkarma : 4
# çıkmak için: q
#             """)
#     print()

#     inp = input("Yapmak istedğiniz işlemi seçin: ")
#     if inp == 'q':
#         print("Çıkış yapılıyor")
#         break
#     if inp == '1':
#         sayi1 = int(input("çarpmak istediğinzi 1. sayıyı girin : "))
#         sayi2 = int(input("çarpmak istediğinzi 2. sayıyı girin : "))
#         print("#############################")
#         print("sonuc", sayi1 * sayi2)
#         print("#############################")

#     elif inp == '2':
#         sayi1 = int(input("bölmek istediğinzi 1. sayıyı girin : "))
#         sayi2 = int(input("bölmek istediğinzi 2. sayıyı girin : "))
#         print("#############################")
#         print("sonuc", sayi1 / sayi2)
#         print("#############################")

#     elif inp == '3':
#         sayi1 = int(input("toplamak istediğinzi 1. sayıyı girin : "))
#         sayi2 = int(input("toplamak istediğinzi 2. sayıyı girin : "))
#         print("#############################")
#         print("sonuc", sayi1 + sayi2)
#         print("#############################")
#     elif inp == '4':
#         sayi1 = int(input("çıkarmak  istediğinzi 1. sayıyı girin : "))
#         sayi2 = int(input("çıkarmak  istediğinzi 2. sayıyı girin : "))
#         print("#############################")
#         print("sonuc", sayi1 - sayi2)
#         print("#############################")
#     else:
#         print("#############################")
#         print("Böyle bir seçenek yok")
#         print("#############################")










# array = ["ali","beren","ceren","deniz","ekrem"]


# for aliamca in array:
#     print(aliamca.upper())

# text = 'Merhaba Dünya'

# for aliamca in text:
#     print(aliamca)

# array = ["ali","beren","ceren","deniz","ekrem"]

# for aliamca in array:
#     if aliamca == 'beren':
#         print(aliamca, "bulundu")
#         break
#     print(aliamca)


# for x in range(5,50,4):
#     print(x)


# for x in range(20):
#     print(x**2)



# array = range(50,100,2)

# for x in array:
#     print(x)
#     if x == 60:
#         print("60 sayısı buldum")
#         break



ciftsayilar = []
teksayilar = []


for x in range(30):
    if x % 2 == 0:
        # print("bu sayı çiftir",x)
        ciftsayilar.append(x)
    elif x % 2 == 1:
        # print("bu sayı tektir",x)
        teksayilar.append(x)

print(ciftsayilar)
print(teksayilar)










