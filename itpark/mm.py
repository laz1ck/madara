# 1hi vazifa Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida
# alifbo ketma-ketligida chiroyli qilib konsolga chiqaring


# lugat = {
#     'Boolean': 'Mantiqiy qiymat',
#     'Float': 'Onlik son',
#     'For': 'Biror amalni qayta-qayta bajarish tsikli',
#     'If': 'Shartlarni tekshirish operatori',
#     'Integer': 'Butun son'
# }


# sorted_lugat = dict(sorted(lugat.items()))


# for kalit, qiymat in sorted_lugat.items():
#     print(f"{kalit}: {qiymat}")






# 2chi vazifa
# poytaxtlar = {
#     'O‘zbekiston': 'Toshkent',
#     'Rossiya': 'Moskva',
#     'AQSh': 'Vashington',
#     'Qozog‘iston': 'Ostona',
#     'Fransiya': 'Parij',
#     'Germaniya': 'Berlin',
#     'Yaponiya': 'Tokio',
#     'Hindiston': 'Dehli',
#     'Italiya': 'Rim',
#     'Turkiya': 'Anqara'
# }

# sorted = dict(sorted(poytaxtlar.items()))

# for davlat, poytaxt in sorted.items():
#     print(f"{davlat}: {poytaxt}")







# 3chi vazifa

poytaxtlar = {
    "Ozbekiston": "toshkent",
    "aqsh": "vashington",
    "rossiya": "moskva",
    "germaniya": "berlin",
    "fransiya": "parij",
    "xitoy": "pekin",
    "hindiston": "dehli",
    "italiya": "rim",
    "braziliya": "braziliya",
}


davlat = input("Davlat nomini kiriting: ")


if davlat in poytaxtlar:
    print(f"{davlat} davlatining poytaxti {poytaxtlar[davlat]}")
else:
    print("Bizda bunday ma'lumot yo'q")
