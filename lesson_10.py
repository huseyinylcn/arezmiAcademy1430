# def func1(dizi):
#     tekler = []
#     ciftler = []
#     for i in dizi:
#         if i % 2 == 0:
#             ciftler.append(i)
#         elif i % 2 == 1:
#             tekler.append(i)

#     result = {"tekler":tekler,"ciftler":ciftler}
#     return result


# array = [3,6,9,11,55,88,23]
# result = func1(array)

# # print(result["tekler"])
# # print(result["ciftler"])
# print(type(result))
# for x,y in result.items():
#     print(x,y)







# def func2 (metin,karakter):
#     sonuc = metin.count(karakter)
#     return sonuc

# result =  func2("merhaba dünya merhaba", "merhaba")
# print(result)


# def func2 (metin='',karakter=''):
#     sonuc = metin.count(karakter)
#     return sonuc

# result =  func2( karakter="merhaba",metin="merhaba dünya merhaba")
# print(result)







# liste = [-3,1,5,2,12,65,78]
# x = max(liste)
# y = min(liste)
# print(y)


# def func3(dizi):
#     if len(dizi) == 0:
#         return "listede eleman yok"
#     enbuyuk = max(dizi)
#     enkucuk = min(dizi)

#     return {"enbuyuk":enbuyuk,"enkucuk":enkucuk}



# result = func3([1,5,99,12,45,21])
# print(result)
# print()
# print(result["enbuyuk"])
# print(result["enkucuk"])
# print()
# for annahtar,deger in result.items():
#     print(annahtar,deger)






# metin = "merhaba, nasılsın ,ali , amca , nasıl"

# dizi = metin.split("na")
# print(dizi)
# for i in dizi:
#     print(i)



# print("     merhaba     ".strip())





# def func4(metin):
#     sonuc = metin.strip()
#     return sonuc

# result = func4("         arezmi       ")

# print(result)





# def func5(metin):
#     en_uzun = ''
#     for i in metin:
#         if len(i) > len(en_uzun):
#             en_uzun = i
#     return en_uzun, len(en_uzun)


# dizi = ["ali","kemal","yusuf","hamit burak","hasan"]

# result = func5(dizi)

# print(result)











# def func6():
#     myArray = ("elma","armut","kiraz")

#     print(myArray)

#     inp = input("silmek istediğiniz ifadeyi yazın silmek istemiyorsanız quit yazın: ")

#     if inp != 'quit':
#         myArray = list(myArray)
#         myArray.remove(inp)
#         print("veriniz silindi..")
#         print("Güncel veri",myArray)
#         myArray = tuple(myArray)
#     else:
#         print("çıkış yapılıyor")


# func6()










# name = 'hüseyin'
# print(name)



# user1 = "Hüseyin"
# def func7():
#     global user1
#     user1 = 'Mehmet'

# func7()
# print(user1)





# def func7(x):
#     def karealma():
#         return x **2
#     return karealma


# result = func7(5)
# print(result())



# def yazma (metin):
#     def terminaleyaz():
#         print(metin)
#     return terminaleyaz

# result = yazma("merhaba dünya")

# print(result)


