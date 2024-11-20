# import test as tt
# from test import karealma

# print(karealma(5))

# import test as tt

# tt.karealma()

# from test import selmaverme

# selmaverme()








import tkinter as tk
window =  tk.Tk()

kullanicilar = []

def kayıt_ekle():
    if not(age.get().isdigit()):
        info["text"] = "Lütfen yaşı doğru girin"
        return
    user = {
        "name":name.get(),
        "surname":surname.get(),
        "age":age.get()
    }
    kullanicilar.append(user)
    info["text"] = "Kullanıcı başarıyla eklendi"

def goruntule():
    for i in kullanicilar:
        print(i)

window.title("İlk Uygulamam")
window.geometry("500x400")


tk.Label(text="Adınız: ").pack(pady=3)
name = tk.Entry()
name.pack(pady=5)

tk.Label(text="Soyadınız : ").pack(pady=3)
surname = tk.Entry()
surname.pack(pady=5)

tk.Label(text="Yaşınız : : ").pack(pady=3)
age = tk.Entry()
age.pack(pady=5)

btn = tk.Button(text="Ekle",command=kayıt_ekle)
btn.pack()


btn2 = tk.Button(text="Kullanıcıları görüntüla",command=goruntule)
btn2.pack(pady=3)

info = tk.Label(text="")
info.pack()

window.mainloop()



# kullaniciler = []

# def kullanivi_ekle():
#     name = input("isim : ")
#     surname = input("soyisim : ")
#     age = input("yaşınız : ")

#     user = {
#         "name":name,
#         "surname":surname,
#         "age":age
#     }
#     kullaniciler.append(user)


# while True:
#     inp = input("çıkmak için quit yazın kullanıcı eklemek için ekle kullanıcıları görüntülemek için gör : ")
#     if inp == 'quit':
#         break
#     elif inp == "ekle":
#         kullanivi_ekle()
#     elif inp == "gör":
#         for i in kullaniciler:
#             print(i)
#     else:
#         continue




















