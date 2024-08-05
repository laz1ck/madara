# # 1chi 
# shaxs = [
#     {
#         "ism": "Abu Abdulloh Muhammad ibn Ismoil",
#         "yil": 810,
#         "shaxar": "Buxoro",
#         "yosh": 60
#     },
#     {
#         "ism": "Abdulla Qodiriy",
#         "yil": 1894,
#         "shaxar": "Toshkent",
#         "yosh": 44
#     },
#     {
#         "ism": "Erkin Vohidov",
#         "yil": 1936,
#         "shaxar": "Farg'ona",
#         "yosh": 80
#     },
#     {
#         "ism": "Alisher Navoiy",
#         "yil": 1441,
#         "shaxar": "Xirot",
#         "yosh": 60
#     }
# ]


# for shaxslar in shaxs:
#     print(f"Ism: {shaxslar['ism']}\nTug'ilgan yili: {shaxslar['yil']}\nTug'ilgan joyi: {shaxslar['shaxar']}\nYoshi: {shaxslar['yosh']} yil\n")








# 2 chi
# shaxs = [
#     {
#         "ism": "Abu Abdulloh Muhammad ibn Ismoil",
#         "yil": 810,
#         "shaxar": "Buxoro",
#         "yosh": 60,
#         "asarlari": ["Sahih al-Bukhari"]
#     },
#     {
#         "ism": "Abdulla Qodiriy",
#         "yil": 1894,
#         "shaxar": "Toshkent",
#         "yosh": 44,
#         "asarlari": ["O'tkan kunlar", "Mehrobdan chayon"]
#     },
#     {
#         "ism": "Erkin Vohidov",
#         "yil": 1936,
#         "shaxar": "Farg'ona",
#         "yosh": 80,
#         "asarlari": ["Ruhlar isyoni", "Inson o'g'li"]
#     },
#     {
#         "ism": "Alisher Navoiy",
#         "yil": 1441,
#         "shaxar": "Xirot",
#         "yosh": 60,
#         "asarlari": ["Xamsa", "Lison ut-Tayr"]
#     }
# ]

# for shaxslar in shaxs:
#     print(f"yozuvchi: {shaxslar['ism']}\n"
#           f"{shaxslar['asarlari']}"
#           )









# 3chi
# shaxs = [
#     {
#         "ism": "alining sevimli kinosi",
#         "kino_1": 'orgimchak odam',
#         'kino_2': 'lutsifer'
#     },
#     {
#         "ism": "valining sevimli kinosi",
#         "kino_1": 'tofon',
#         'kino_2': 'dengiz '
#     },
#     {
#         "ism": "azizning sevimli kinosi",
#         "kino_1": 'dinazavr',
#         'kino_2': 'kapitan'
#     },
#     {
#         "ism": "Alisherning sevimli kinosi",
#         "kino_1": 'sonic',
#         'kino_2': 'venom'
#     }
# ]

# for shaxslar in shaxs:
#     print(f"{shaxslar['ism']}\n"
#           f"{shaxslar['kino_1']}\n"
#            f"{shaxslar['kino_2']}\n"
#           )

















# 4chi vazifa
malumotar = [
    {
        "ism": "ozbekiston davlatining poytaxti toshkent",
        "hududi": '12345.0 km',
        'axoli': '38000000',
        'pul':'som'
    },
    {
        "ism": "aqsh davlating poytaxti vashington",
        "hududi": '128975.0 km',
        'axoli': '88000000',
        'pul':'dollar'
    },
    {
        "ism": "rossiya davlatining poytaxti moskva",
        "hududi": '999999999.0 km',
        'axoli': '1009000000',
        'pul':'rubl'
    },
    {
        "ism": "turkiya davlatining poytaxti ankara",
        "hududi": '123875.0 km',
        'axoli': '400000000',
        'pul':'lira'
    }
]

for py in malumotar:
    print(f"{py['ism']}\n"
          f"hududi: {py['hududi']}\n"
          f"axolisi: {py['axoli']}\n"
          f"pul birligi: {py['pul']}\n"
          )
