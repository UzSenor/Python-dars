try:
    son = int(input("Sonni kiriting: "))
except ValueError:
    print("O'rganish muvoffaqiyatsiz amalga oshdi!")
finally:
    print("Try bloki ishi tugadi!")
print("Dastur tugadi!")