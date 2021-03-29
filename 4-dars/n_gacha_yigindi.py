while True:
    ch = input("Chiqish uchun 'X' ni bosing: ")
    if ch.lower() == 'x':
        break
    s = 0
    n = int(input("n = "))
    for i in range(1, 1+n):
        s += i
    print("n gacha yig'indi: ", s)