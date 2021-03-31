import copy 
vil1 = ["Toshkent", "Xorazm"]
vil2 = copy.deepcopy(vil1)
vil2.append("Buxoro")
print(vil1)
print(vil2)