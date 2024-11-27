import tkinter as tk

import time



class Users:
    kullanicilar = []
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        Users.kullanicilar.append(self)
    
    def bilgiGoster(self):
        return f"Ad:{self.name}, Soyisim : {self.surname}, Yaş : {self.age}"
    
    

        


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("İkinci Uygulamam")
        self.geometry("300x500")



class Content(Window):
    def __init__(self):
        super().__init__()

        self.nameLabel = tk.Label(text="İsim")
        self.nameLabel.pack(pady=10)

        self.name = tk.Entry()
        self.name.pack()


        self.surnameLabel = tk.Label(text="soyisim")
        self.surnameLabel.pack(pady=10)

        self.surname = tk.Entry()
        self.surname.pack()


        self.ageLabel = tk.Label(text="age")
        self.ageLabel.pack(pady=10)

        self.age = tk.Entry()
        self.age.pack()


        self.btn = tk.Button(text="Kaydet",command=self.save)
        self.btn.pack(pady=10)




class Metotlar(Content):
    def __init__(self):
        super().__init__()
        self.infoLabel = tk.Label(text="")
        self.infoLabel.pack()


    def save(self):
        Users(self.name.get(),self.surname.get(),self.age.get())

        self.Kullanıcilarisirala()



class Metotlar2(Metotlar):
    array = []
    def __init__(self):
        super().__init__()

        

    def temizleme(self):
        for i in self.array:
            i.destroy()
        
    def Kullanıcilarisirala(self):  
        self.temizleme()      
        for index,value in enumerate(Users.kullanicilar):
            k = tk.Label(text=f"{value.name}")
            k.pack()

            k.bind("<Button-1>",lambda e, v = value: self.bilgigöster(v.name))
            self.array.append(k)



    def bilgigöster(self,name):
        for i in Users.kullanicilar:
            if i.name == name:
                print(name)
                print(i.bilgiGoster())
                self.title(i.bilgiGoster())


    
    


        





w1 = Metotlar2()
w1.mainloop()