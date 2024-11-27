# class Users:

#     kullanici_sayisi = 0

#     def __init__(self,name,surname) :
#         self.name = name
#         self.surname = surname
#         Users.kullanici_sayisi += 1
    
#     def bilgilergoster(self):
#         return f"kullanıcının adı {self.name} kullanıcın soyadı {self.surname}"

#     @classmethod
#     def kullanici_sayisi_goster (cls):
#         print(cls.kullanici_sayisi)

    

# u1 = Users("name","surname")

# Users.kullanici_sayisi_goster()





# class Users:
#     kullanicilar = []

#     def __init__(self,name,surname) :
#         self.name = name
#         self.surname = surname
#         Users.kullanicilar.append(self)
    
#     def bilgilergoster(self):
#         return f"kullanıcının adı {self.name} kullanıcın soyadı {self.surname}"

#     @classmethod
#     def kullanicilarigöster (cls):
#         for user in cls.kullanicilar:
#             print(user.name)
    
#     @classmethod
#     def kullanici_sayisi(cls) :
#         return len(cls.kullanicilar)


# print( Users.kullanici_sayisi() )







# class Users:
#     def __init__(self,name,surname) :
#         self.name = name
#         self.surname = surname

    
#     def bilgilergoster(self):
#         return f"kullanıcının adı {self.name} kullanıcın soyadı {self.surname}"
    
#     @staticmethod
#     def func1():
#         print("canım istedi selam verdim kime ne ")


# u1 = Users("Hüseyin", "Yalçın")

# u1.func1()
# Users.func1()








# class DB:
#     def __init__(self) :
#         self.ipadres = '192.168.1.1'
#         self.port = 1443
#         self.database = "Uyguamadb"
#         self.password = "123456789"
#         self.dbConnect()

#     def dbConnect (self):
#         print("connect")
#         return "connect"

# class dataWrite(DB):
#     pass


# dataWrite()






# class Users:

#     def __init__(self,name,surname) :
#         self.name = name
#         self.surname = surname
    
#     def bilgilergoster(self):
#         return f"kullanıcının adı {self.name} kullanıcın soyadı {self.surname}"



# class Developer(Users):

#     def __init__(self, name, surname,age):
#         super().__init__(name,surname)
#         self.age = age

#     def bilgilergoster(self):
#         return f"kullanıcının adı {self.name} kullanıcın soyadı {self.surname} yaşı {self.age}"
        

# dv = Developer("Emre","Şahin",20)

# print(dv.bilgilergoster())

