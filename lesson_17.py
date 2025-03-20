# dışarıdan isim ve soyisim alan bir fonksiyon tanımlayın ve bu fonkiyon isim ve soyisimin birleşmiş halini geriye döndürsün
# eğer girilen değer str değilse fonksiyon sonlansın ve sonuç olarak hatalı giriş değerini döndürsün
# fonksiyon içerisindeki olası bir hatayı yakala ve hatanın ne olduğunu bul ve hata verdi yazdır
# fonksiyona girilen isim ve soyisim terminalden kullanıcı girsin


def yazma(isim,soyisim):

    try:
        if not( isinstance(isim,str) and isinstance(soyisim,str) ):
            return "hatalı giriş"
        return isim +" "+ soyisim
    except Exception as e:
        return f"hatam {e} genel fonksiyon hatası verdi"




result = yazma("hüseyin","yalçın")

print(result)








