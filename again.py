# Print komutu terminalden çıktı almamızı sağlar
# print('Hüseyin Yalçın')
# print(12)
# print(12.4)


# int, veri türüdür ve bu tam sayıları temsil edir 
# print( 12 )

# str veri türüdür ve bu metinleri temsil eder
# "Python dersleri"
# ' tek tırnak '

# print( "Hüseyin Yalçın " )

# float
# 12.4 
# 11.0

# print( 23.5 )

# terminale int , str ve float tipinde veriler yazdırın 

# print( 12 )
# print( "arezmi ile öğren" )
# print( 12.4 )


# type( 12 ) komutu bana verimin tipini verir 

# type(12.4) 


# print( type("12.5") )



# print( type(" ben metinim ") )
# print( type(12) )
# print( type(3.5) )



# = operatörü atama operatörüdür


# metin = " Arezmi academy ders tekrarları "
# sayi = 12
# sayi2 = 12.3


# print( sayi )
# print( metin )
# print( sayi2 )

# değişken isimleri sayı ile başlayamaz ve içerisnde ! ? { } vb karakterler bulunduramaz 



# temel operatörler 

# = atama operatörü

# + toplama operatörü 

#  - çıkarma operatörü

#  * çarpma operatörü 

# / bölme operatörü

# ** üst alma operatörü

#  // mod alma 


# result1 = 3 // 6
# print(result1)

# result2 = 5**2
# print(result2)

# result3 = 5 - 3
# print(result3)

# result4 = 2 + 2
# print(result4)

# result5 = 3 / 2
# print(result5)

# result6 = 3 * 4
# print(result6)




#^ str ile int veri türleri toplnamaz veya çıkartılamaz  
#! str ile float veri türleri toplanamz çıkarılaz
#TODO int ve float veri türleri toplanabilir veya çıkarılabilir vb.
#~ str ve str veri türleri sadece toplanabilir. 


# result = "12" + " ahmet"
# print(result)



# result = "Ahmet"+ " "+ "Amca" + " " + "Nasılsın"

# print(result)

# name = "Hüseyin"
# surname = 'Yalçın'

#^ print komutuna birden fazla ifade girmek istersek virgül ile ayırabiliriz 
# print( name, surname, 12 ,"Arezmi" )

#TODO 3 adet değişken tanımlayın ve bunları tek bir print içierinde konsola yazdırın süre 2 dk

# name = 'Hüseyin'
# surname = 'Yalçın'
# city = 'Edirne'

# print(name, surname, city)



#& değişkenlerimi sonrada güncellyebilirz atama operatörü ile
# age = 12
# print(type(age))
# age = "12"
# print(type(age))

#~ String İfadeleri integer çevirme  





# sayi = '12'
# print("ilk tipi", type(sayi) )

# sayi = int(sayi)

# result = 13 + sayi
# print("son tipi", type(sayi))

# print(result)

# sayi1 = "37"

# sayi1 = int(sayi1)

# result = sayi1 + 5.5
# print(result)


#! String bir sayi oluşturun ve bir değişkene atayın daha sonra bu verinin tipini konsola yazdırın süre 1.5dk



# ali  = "212"
# mehmet = "312"

# ali = int(ali)
# mehmet = int(mehmet)

# print( "alinin tipi ",type(ali) )

# print( "mehemetin tipi ",type(mehmet) )

# print("sonuc",  ali + mehmet)



# konya = "12"
# manisa = "144"

# konya = int(konya)
# manisa = int(manisa)

# print( type(konya), "konyanın tipi" )
# print( type(manisa) , "manisanın tipi" )

# toplam = konya + manisa

# print( "sonuc", toplam  )


#~ int ifadeleri str cevirme


# ahmet = 2010
# ahmet = str(ahmet)
# metin = "ahmet " + ahmet + " yıl " + "okula başladı"
# print(metin)



# https://www.w3schools.com/python/default.asp









# sayi = "12.4"

# print(sayi)

# sayi = float(sayi)

# print(sayi)




# gelenveri = input("Lütfen sayı girin : ")

# gelenveri = int(gelenveri)

# gelenveri = gelenveri**2

# print("alınan verinin karesi  ", gelenveri)





# sayi1 = input("toplamak istediğiniz 1. sayıyı girin: ")
# sayi1 = int(sayi1)

# sayi2 = input("toplamak istediğiniz 2. sayıyı girin: ")
# sayi2 = int(sayi2)

# print("sonuc", sayi1 + sayi2 )



# True
# False

# x = False
# print(type(x))




# == 



# print(2 == 3)
# print( 5 > 3)
# print(2 < 4)
# print(2 >= 2)
# print(3 <= 4)
# print(2 != 3)
# sonuc = 3 > 5
# print(type(sonuc))




# name = "merhaba konya"

# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.replace("a","A"))
# print(name.strip())
# print(name.isdigit())



# print(name[8])


# print(len(name))
# print(name[-2])
# print(name[3 : 5])



# password = "123"
# girilensifre = input("şifrenizi giriniz : ")


# if password == girilensifre :
#     print("sisteme hoşgeldiniz ")
#     print("ne yapmak istiyorsunuz ? ")
# else:
#     print("sisteme giremediiz")
#     print("şifrenizimi unuttunuz")






# if True:
#     print("merhaba")
#     print("hoşgelgin")
# else:
#     print("else çalıştı")
#     print("tamam")






# sayi = input("lütfen sayı girin : ")



# if sayi.isdigit() :
#     print("tüm karakterler rakam doğru girdiniz")
#     sayi = int(sayi)
#     print(sayi**2)
# else:
#     print("sadece sayı girmelisiniz")



# password = "123"
# username = 'hsyn'


# inputusername = input("kullanıcı adınızı giriniz : ")

# if username == inputusername:

#     inputpassword = input("lütfen şifrenizi giriniz : ")
#     if password == inputpassword:
#         print("şifrenizde doğru sisteme hoşgeldiniz")
#     else:
#         print("kullanıcı adınız doğru ama şifreniz yanlış")

# else:
#     print("kullanıcı adınız doğru değil")





# meyve = ["elma","armut","çilek",12,34,1.5,True]

# meyve.append("karpuz")
# meyve.insert(2,"karpuz")
# meyve.remove(12)
# meyve.pop(2)
# del meyve[1]
# meyve.clear()
# meyve2 = meyve.copy()
# print(meyve)
# print(type(meyve))



# meyve = ("elma","armut","karpuz")
# print(type(meyve))
# meyve = list(meyve)
# print(type(meyve))
# meyve.append("kiraz")
# meyve.remove("karpuz")
# print(meyve)
# meyve = tuple(meyve)
# print(type(meyve))






















