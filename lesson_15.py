# try:
#     sayi = input("sayı girin : ")
#     print(sayi-5)
# except:
#     print("hata verdi")

# print("tamam")


# try:
#     print(10/0)
# except Exception as e:
#     print("hata verdi", e)


# try:
#     print(3 - 'abv')
# except ValueError as e:
#     print("hata verdi",e)
# except ZeroDivisionError as e:
#     print("hata verdi 2", e)
# except Exception as e:
#     print("hata verdi 3", e)



# try:
#     dsy = open("deneme.txt")
#     dsy.write("ali amca") 
# except ValueError as e:
#     print("hata verdi",e)
# except ZeroDivisionError as e:
#     print("hata verdi 2", e)
# except Exception as e:
#     print("hata verdi 3", e)
# finally:
#     dsy.close()
#     print("dosya kapatıldı")




try:
    print("dfs"+34535)
except ValueError as e :
    print("hata verdi ")
except Exception as e:
    print("hata verdi",e)
else:
    print("başarılı bitti")
finally:
    print("ne olursa olsun ben çalışırım")


    


