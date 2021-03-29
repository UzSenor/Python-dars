try:
    str = int(input("Son kiriting: ")) #Bu yerga faqat butun son kiritiladi
    print("Kiritilgan son: ",str) #Butun qiymatni ekranga chiqaradi
except:
    print("Kiritilgan qiymat int tipiga mansub emas!") # Agar kiritilga qiymat butun son bo'lmasa shu qator chiqadi
print("Dastur tugadi.")