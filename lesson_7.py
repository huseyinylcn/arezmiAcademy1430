# set
# set tipindeki diziler sırasızdır.


# my_array = { "ahmet","Ali","Mehmet",212,3.3,True}
# print(my_array)
# print(type(my_array))







# meyveler = {"elma","armut","kiraz"}
# print(meyveler)
# print(type(meyveler))



# set tipindeki dizilerin içerisindeki elemanlar deiştirilemez fakat silinebilir ve yeni veri eklenebilir
# cars = {"Toyoto","Renault","TOGG","Opel"}
# cars.add("Ford")
# cars.add('Mercedes')

# print(len(cars))
# print(cars)

# cars = {"Toyoto","Renault","TOGG","Opel"}
# cars.update({"Ford","Fiat"})
# print(cars)









# urunler = {"Çanta","Gömlek","Ayakkabı"}

# urunler.add("kravat")
# print(urunler)
# print(len(urunler))


# print("###########################################")

# urunler.update({"Pantolon","Toka","Şişe"})
# print(urunler)
# print(len(urunler))





# urunler = {"Çanta","Gömlek","Ayakkabı"}


# remove set tipindeki listenin içerisinden elemanlı siler fakat silinmek istenen eleman yok ise hata verir
# urunler.remove("Yelek")

# discord liste içerisndeki belirtilen elemanı siler silinmek istenen eleman yok ise hata vermez
# urunler.discard("Yelek")
# print(urunler)



# yemekler = {"Fasulye","Pilav","Tavuk Sote"}

# yemekler.add("Mercimek Çorbası")

# print(yemekler)
# print(len(yemekler))

# yemekler.remove("Fasulye")
# yemekler.discard("Fasulye")

# yemekler.update({"İmam Bayıldı","KarnıYarık","Sarma"})
# print(yemekler)
# print(len(yemekler))







# user1 = { "name":"Hüseyin","surname":"Yalçın","city":"Edirne" }


# bu yönet ile verilerimize erişebilirz lakin erişmek isteğimiz veri yok ise hata alırız
# user1["name"]

# bu yönet ile verilerimize erişebilirz lakin erişmek isteğimiz veri yok ise hata almayız None değeri allırız
# user1.get("name")


# print(user1.get("cit"))

# car = {
#     "name":"kara şimşek",
#     "model":"e model",
#     "yıl":1999,
#     "renk":"kırmızı",
# }

# car.pop("yıl")
# car.popitem()

# del car["renk"]

# car.clear()
# del car


# car["renk"] = "Mavi"
# print(car.keys())
# print(car.values())
# print(list(car.items()))

# car["hp"] = 2000
# car.update({"yıl":2000})
# print(car)


# user1 = {
#     "fullname":"Hüseyin Yalçın",
#     "Derpartmen":"IT",
#     "city":"Konya",
#     "salary":1000000
# }

# print(user1)
# print(user1["fullname"])
# print(user1.get("city"))
# user1["city"] = "İstanbul"

# if user1.get("salary") != None:
#     if user1.get("salary")  < 25000:
#         user1["salary"] += user1.get("salary") * 0.20
#         print("Güncel maaşınız ",user1.get("salary") )
    

# else:
#     print("Maşşınız bulunamadı sistem hata verdi")
#     slr = int( input("Maaşınız giriniz : ") )
#     if slr < 25000:
#         user1["salary"] = slr*0.20 + slr
#         print("Güncel maaşınız ",user1.get("salary") )
#     else:
#         print("maaşınıza zam yapılmadı")
#         user1["salary"] = slr

        













