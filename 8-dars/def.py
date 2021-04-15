def get_user():
    name = "Xursand"
    age = 29
    is_married = True
    return name, age, is_married
user = get_user()
print(user[0]) #Xursand
print(user[1]) #29
print(user[2]) #True
#Yoki alohida o'zgaruvchi yuklanadi
name, age, is_married = get_user()
print(name) #Xursand
print(age) #29
print(is_married) #True