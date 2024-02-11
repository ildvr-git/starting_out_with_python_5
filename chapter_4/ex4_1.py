total = 0
for day in range(1, 6):
    err_qty = int(input(f"Введите кол-во ошибок в {day} день >>> "))
    total += err_qty
print(f"За 5 дней обнаружено {total} ошибок!")