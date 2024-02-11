boys_qty = int(input("Введите кол-во мальчиков >>> "))
girls_qty = int(input("Введите кол-во мальчиков >>> "))

boys_rate = boys_qty/(boys_qty + girls_qty)
girls_rate = girls_qty/(boys_qty + girls_qty)

print(f"Мальчиков - {boys_rate: .2%}")
print(f"Девочек - {girls_rate: .2%}")