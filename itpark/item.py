# talaba = {
#     'ism':'lazizbek',
#     'familya':'huddayquliyev',
#     'yosh':15
# }

# print(talaba.items())





# talaba = {
#     'ism':'lazizbek',
#     'familya':'huddayquliyev',
#     'yosh':15
# }
# for kalit , qiymat in talaba.items():
#     print(f"kalit: {kalit}")
#     print(f"qiymat: {qiymat}")


# telefonlar = {
#     'ali':'iphone 17',
#     'aziz':'redmi',
#     'vali':'poco',
#     'olim':'red magic 9 pro'
# }

# for k , q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")








# mahsulotlar = {
#     'olma':10000,
#     'shaftoli':15000,
#     'grusha':1000,
#     'tarvuz':20000
# }
# # print(mahsulotlar.keys())


# bozorlik = ['anor','uzum','shaftoli']
# for maxsulot in mahsulotlar:
#     if mahsulotlar in bozorlik:
#         print(f"{maxsulot.title()} {mahsulotlar[maxsulot]} som")
        
# for buyum in bozorlik:
#     if buyum not in maxsulot:
#         print(f"iltimos dokoningizga {buyum} ham olib keling")

# print("dokoninggizdagi maxsulotlar: ")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title()) 









 
# telefonlar = {
#     'ali':'iphone 17',
#     'aziz':'redmi',
#     'vali':'poco',
#     'olim':'red magic 9 pro'
    
# }
# # print(telefonlar.values())
# print('foydalonuvchida shunday telefon bor')
# for tel in set(telefonlar.values()):
#     print(tel)













# car1 ={
#     'model':'bmw',
#     'rang':'seriy',
#     'narxi':'150000',
#     'yil':2024,
#     'karobka':'avtamoat'
# }



# car2 ={
#     'model':'supra',
#     'rang':'qora',
#     'narxi':'100000',
#     'yil':2021,
#     'karobka':'avtamoat'
# }



# car3 ={
#     'model':'mers',
#     'rang':'siniy',
#     'narxi':'150000',
#     'yil':2024,
#     'karobka':'avtamoat'
# }

# cars = [car1,car2,car3]
# for car in cars:
#     print(f"{car['model'].title()} {car['rang']} rang {car['yil']} yil  {car['narxi']}$" )
# car = car1
# print(f"{car['model'].title()} {car['rang']} rang {car['yil']} yil  {car['narxi']}$")

# car = car2
# print(f"{car['model'].title()} {car['rang']} rang {car['yil']} yil {car['narxi']}$")


# car = car3
# print(f"{car['model'].title()} {car['rang']} rang {car['yil']} yil {car['narxi']}$")

































# malibu = []
# for n in range(10):
#     car={
#     'model':'bmw',
#     'rang':'none',
#     'narxi':'150000',
#     'yil':2024,
#     'karobka':'avtamoat'
#     }
#     malibu.append(car)
# print(malibu)

# for malibus in malibu[:3]:
#     malibus['rang']='qizil'
    
# for malibus in malibu[:3]:
#     malibus['mexanik']='avtamat'
    
    
#     for malibus in malibu:
#         if malibus['karobka']=='avto':
#             malibus['narx']=40000
#         else:
#             malibus['narx']=35000 
    
# print(malibu)





hm = {
    'ali':{
        'familya': 'valiyev',
        'yil': 1999,
        'malumot ':'oliy',
        'til':'pyton'
    },
        'ali':{
        'familya': 'valiyev',
        'yil': 1999,
        'malumot ':'oliy',
        'til':'pyton'
    },
        'ali':{
        'familya': 'valiyev',
        'yil': 1999,
        'malumot ':'oliy',
        'til':'pyton'
    }
}
for ism ,info in hm.items():
    print(f"/n{ism.title()}")