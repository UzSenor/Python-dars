try:
    son1 = int(input("Birinchi son: "))
    son2 = int(input("Ikkinchi son: "))
    if son2 == 0:
        raise Exception ("Nolga bo'lish yuzaga keldi!")
    print("Bo'linma: ", son1/son2)
except ValueError:
    print("Butun son kiritilmadi!")
except Exception as e:
    print("Xatolik: ",e)
print("Dastur tugadi!")