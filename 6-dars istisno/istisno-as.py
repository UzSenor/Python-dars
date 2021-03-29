try:
    son = int(input("Sonni kiriting: "))
except ValueError as e:
    print("Xatolik: ",e)
print("Dastur tugadi!")