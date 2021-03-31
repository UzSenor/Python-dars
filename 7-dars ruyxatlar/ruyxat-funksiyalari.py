users = ["Xursand", "Humoyun"]
# ro'yxatga element qo'shish
users.append("Sayyora") # ["Xursand", "Humoyun", "Sayyora"]
#ro'yxatning 2 elementiga qo'shish
users.insert(1, "Ro'zaxon") #["Xursand", "Ro'zaxon", "Humoyun","Sayyora"]
# ro'yxatning indexini tanlash
i = users.index("Xursand")
#index elementini o'chirish
uchirish = users.pop(i) #["Ro'zaxon", "Humoyun", "Sayyora"]
#ro'yxatdan oxirgi elementni olish
sunggi = users[-1] #["Sayyora"]
#ro'yxatdan oxirgi elementni o'chirish
users.remove(sunggi) #["Ro'zaxon", "Humoyun"]
print(users)
#Ro'yxatni tozalash
users.clear()