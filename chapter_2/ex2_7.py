user_distance = float(input("Введите пройденное расстояние в километрах >>> "))
user_liters = float(input("Введите количество потраченного топлива в литрах >>> "))
consumption = user_distance/user_liters
print(f"Расход топлива за поездку составил {consumption: .2f} л. на километр")