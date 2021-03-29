try:
    son1 = int(input("Birinchi sonni kiriting: "))
    son2 = int(input("Ikkinchi sonni kiriting: "))
    print("Bo'linma: ",son1/son2)
    print("Ko'paytma: ", son1*son2)
    print("Yig'indi: ",son2+son1)
    print("Ayirma: ", son1-son2)
except ValueError:
    print("Qiymat kiritishda xato!")
except ZeroDivisionError:
    print("Nolga bo'lish borligi uchun xatolik!")
except Exception:
    print("Umumiy istisno holati!")
print("Dastur tugadi.")