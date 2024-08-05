# son = 1
# while son<=5:
#     print(son, end=' ')
#     son = son+1



# print('kiritilgan sonni kvadratini qaytaruvchi dastur')
# savol = 'istalgan sonni kiriting'
# savol = "(dasturni toxtatish uchun exit deb yozing): "
# qiymat = True
# while qiymat:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         qiymat =False
#     else:
#         print(float(qiymat)**2)

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)




# sonlar = list(range(1,21))
# for son in sonlar:
#     if son ==5:
#         break
#     print(f"{son}ning kvadrati {son**2} ga teng")










ismlar =[]
print('yaqin dostizi royxatini tiuzamiz')
n=1
while True:
    savol = f"{n} dostizi ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob  = input("yana ism qoshasizmi  (ha/yoq)")
    if javob == 'ha':
        n+=1
        continue
    else:
        break
print(ismlar)    
