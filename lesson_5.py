# age = 15

# if age < 18:
#     print("18 yaşından küçükmüş ")
# elif age > 18 and age <30:
#     print("genç")
# elif age > 30:
#     print("yaşlı")
# else:
#     print("yaşını yanlış girdin")



# sayi = input("sayı girin : ")

# kontrol = sayi.isdigit()

# if kontrol:
#     sayi = int(sayi)
#     if sayi % 2 == 0:
#         print(sayi,"sayısı çiftir")
#     else:
#         print(sayi,"sayısı tektir")
# else:
#     print("lütfen sayı girin")





# boy = input("boyunuzu giriniz m olarak : ")

# if not boy.isalpha():
#     kilo = input("kilonuzu girinizi kg olarak : ")
#     boy = float(boy)
#     if kilo.isdigit():
#         kilo = float(kilo)
#         bdn = kilo / (boy ** 2)
#         print("bedeniniz : ", bdn)
#         if bdn <= 20:
#             print("zayıf")
#         elif bdn > 20 and bdn <= 30:
#             print("normal")
#         else:
#             print("kilolu")
            
#     else:
#         print("kilonuzu kg olarak yazın harf kullanmayın")
# else:
#     print("boyunuzu m olarak yazın harf kullanmayın")




# soru1 = input("evlimisin evliysen 1 değilsen 2 : ")

# if soru1 == "1":
#     soru2 = input("çocuğun varmı varsa 1 yoksa 2 ")
#     if soru2 == "1":
#         soru3 = input("kac çocuğun var: ")
#         if soru3.isdigit():
#             soru3 = int(soru3)
#             if soru3 >= 3:
#                 print("cumhurbaşkanını  sözünü dinlemişsin")
#             elif soru3 == 1:
#                 soru4 = input("kaç yılında doğdu: ")
#                 if soru4.isdigit():
#                     soru4 = int(soru4)
#                     age = 2024 - soru4
#                     if age < 18:
#                         print("18 yaşından küçük bir cocuğun var")
#                     elif age >= 18 and age < 30:
#                         print("genc bir çocuğun var")
#                     elif age >= 30 and age < 50:
#                         print("olgun bir oğlun var sen yaşlı olmalısın")
#                     else:
#                         print("yaşlı bir oğlun var")
#                 else:
#                     print("çocuğunun yaşını sayı olarak gir. ")
#             else:
#                 print("2 cocuk iyidir 3 cocuk daha iyidir")
#         else:
#             print("kaç cocuğun var sorusuna sayı gir. ")
#     else:
#         print("evlisin ama çocuğun yokmuş")
# else:
#     print("evli değilmiş")
    
