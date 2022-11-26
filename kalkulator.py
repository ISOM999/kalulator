ism = input("ismingiz nima ? \n >>>")
print("Asalomu aleykum, " + ism.title() , "\nBu kalkulatorga hush kelibsiz")
a = float(input("birinchi soni yozing \n>>>"))
b = float(input("ikkinchi soni yozing \n>>>"))
asd = input("nima qilmoqchisiz :\n / = bo'ish * = ko'paytirish + = plus - = minus \n>>>")
if asd == "/":
    print(a / b)
if asd =="*":
    print(a * b)    
if asd == "+":
    print(a + b)
if asd == "-":
    print(a - b)
else:
    print("HATO")


