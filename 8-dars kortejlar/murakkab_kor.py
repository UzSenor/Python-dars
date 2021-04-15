davlatlar = (
    ("O'zbekiston", 33.8,
    (("Toshkent", 2.65),
    ("Samarqand", 1.1),
    ("Xorazm", 0.223))
),
("Qozog'iston", 17.5,
(("Nur Sulton", 1.1),
("Olmaota", 2.3))
))
for davlat in davlatlar:
    nomi, aholi_soni, shaharlar = davlat
    print(nomi, "-", aholi_soni)
    print("Katta shaharlar: ")
    for shahar in shaharlar:
        print(shahar[0], "-", shahar[1])