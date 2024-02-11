SUGAR = 1.5
OIL = 1
FLOUR = 2.75

user_qty = int(input("Введите, сколько булок Вы хотите приготовить >>> "))
ing_rate = user_qty/48

sugar_need = SUGAR * ing_rate
oil_need = OIL * ing_rate
flour_need = FLOUR * ing_rate

print(f"Для приготовления {user_qty} булок Вам потребуется:")
print(f"{sugar_need: .1f} ст. сахара,")
print(f"{oil_need: .1f} ст. масла,")
print(f"{flour_need: .1f} ст. муки.")