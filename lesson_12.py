# class Canavar:
#     def ozellikler(self,name):
#         self.name = name

#     def vur(self):
#         print(self.name,"düşmana vuruldu")
        
#     def kos(self):
#         print("canavar kosuyor")


# c1 = Canavar()
# c1.ozellikler("van")
# c1.vur()

# c2 = Canavar()
# c2.ozellikler("hüseyin")
# c2.vur()



# class Car:
#     def ozellikler(self,model,renk):
#         self.model = model
#         self.renk = renk

#     def farac(self):
#         print("farlar acıldı")
        
#     def farkapama(self):
#         print("farlar kapandı")

#     def modelOgren(self):
#         print(self.model)



# toyota = Car()
# toyota.ozellikler(2024,"kırmızı")


# reno = Car()
# reno.ozellikler(2002,"beyaz")
# reno.modelOgren()



# class Person:
#     def __init__(self,name,surname,age) :
#         self.ad = name
#         self.soyad = surname
#         self.age = age
    

#     def elkaldır(self):
#         print(self.ad,"el kaldırddı")

#     def yasOgren(self):
#         print(self.ad, self.age ,"yaşında")



# u1 = Person("Hüseyin","Yalçın",67)
# u1.elkaldır()
# u1.yasOgren()


# u2 = Person("Eymen","Büyükkaplan",80)
# u2.elkaldır()


# class BankaHesabı:

#     def __init__(self,name):
#         self.name = name
#         self.TL_hesabı = 0
    
#     def paraYatır(self):
#         para = int(input("miktarı girin : "))
#         self.TL_hesabı += para
    
#     def paraCek(self,miktar):
#         if self.TL_hesabı - miktar < 0:
#             print("paranız yetersiz")
#             return
#         self.TL_hesabı -= miktar

#     def hesap_bilgisi(self):
#         return f"{self.name} kullanıcısının parası {self.TL_hesabı}"

#     def terminal(self):
#         while True:
#             inp = input("para yatırmak 1 cekmek için 2 görmek için 3 : ")
#             if inp == "1":
#                 self.paraYatır()

#             elif inp == '2':
#                 para = int(input("miktarı girin : "))
#                 self.paraCek(para)
#             elif inp == '3':
#                 print(self.hesap_bilgisi())


# k1 = BankaHesabı("Hüseyin")
# k2 = BankaHesabı("Emre")



# class Hayvan:
#     def __init__(self,name) :
#         self.name = name

#     def ses_cıkar(self,ses):
#         print(self.name,":", ses)


# kedi = Hayvan("yumak")
# kedi.ses_cıkar("miyav")


# kopek = Hayvan("karabas")
# kopek.ses_cıkar("hav hav")





























