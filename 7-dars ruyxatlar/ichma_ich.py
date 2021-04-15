ishchi = [
    ["Xursand", 29],
    ["Humoyun", 3],
    ["Sayyora", 26]
]
print(ishchi[0]) #['Xursand', 29]
print(ishchi[0][0]) #Xursand
print(ishchi[0][1]) #29
#Ro'yxat yaratish
ishchi1 = list()
ishchi1.append("Sobirov")
ishchi1.append(30)
#Tashqi ro'yxatga yaratilgan ro'yxatni qo'shish
ishchi.append(ishchi1)
print(ishchi[-1]) #['Sobirov', 29)
#Tashqi ro'yxatning oxirgisiga element qo'shish
ishchi[-1].append("+998937458782")
print(ishchi[-1]) #['Sobirov', 29, '+998937458782']
#Oxirgi elementning oxirgi elementini o'chirish
ishchi[-1].pop()
print(ishchi[-1])
#Oxirgi elementni o'chirish
ishchi[-1].pop(-1)
print(ishchi[-1])
#Birinchi elementni o'zgartirish
ishchi[0] = ["Ro'za", 51]
print(ishchi[0])