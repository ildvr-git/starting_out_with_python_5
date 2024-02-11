TAX = 0.07

price1 = float(input("Enter price of the first product >>> "))
price2 = float(input("Enter price of the second product >>> "))
price3 = float(input("Enter price of the third product >>> "))
price4 = float(input("Enter price of the fourth product >>> "))
price5 = float(input("Enter price of the fifth product >>> "))

subtotal = price1 + price2 + price3 + price4 + price5
subtotal_tax = subtotal * TAX
total = subtotal + subtotal_tax

print(f"")
print(f"Subtotal of the sale is {subtotal: .2f}$.")
print(f"The amount of sales tax is {subtotal_tax: .2f}$.")
print(f"Total of the sale is {total: .2f}.")