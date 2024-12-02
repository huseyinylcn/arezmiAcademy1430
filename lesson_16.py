import requests 
import json
# https://jsonplaceholder.typicode.com/posts
# https://jsonplaceholder.typicode.com/todos/2

# while True:
#     try:
#         inp = input("kaç numaralı ürünü getirmek istiyorsun: ")
#         result =  requests.get(f"https://jsonplaceholder.typicode.com/todos/{inp}")
#         if str(result.status_code) == '404':
#             print("hatalı ürün numarası girdiniz")
#         else:
#             print(result.json())
#     except Exception as e:
#         print(e,"hatasını verdi")




# result = requests.post(urll,data=datas)
# print(result.json())

# import json

# with open("veri.json","r") as dosya:
#     data = json.load(dosya)


# veri = [

#     {"name":"fatma","surname":"yalçın"},
#     {"name":"aylin","surname":"yılhan"},
# ]

# for i in veri:
#     data.append(i)


# with open("veri.json","w") as dosya:
#     json.dump(data,dosya, indent=4)




# veri = {
#     "name": "Eymen",
#     "job": "Full Stack Developer"
# }

# result = requests.post("https://reqres.in/api/users",json=veri)

# print(result.status_code)

# print(result.json())



# result = requests.get("https://jsonplaceholder.typicode.com/posts")


# result = result.json()

# with open("veri.json","w") as dosya:
#     json.dump(result,dosya, indent=4)



# with open("veri.json") as file:
#     data = json.load(file)









