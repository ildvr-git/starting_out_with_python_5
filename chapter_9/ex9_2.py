import io
import random

def main():
    file = io.open("chapter 9\data\countries.csv", mode="r", encoding="utf-8")
    lines = file.readlines()
    file.close()

    dict = {line.split(";")[0]:line.split(";")[1] for line in lines[1:]}
    
    amount = get_tries_number()
    right_counter = play(amount, dict)
    
    print(f"Вы угадали {right_counter} из {amount} столиц!")

def get_tries_number():
    n = input("Сколько столиц будем отгадывать? >>> ")
    while not n.isdigit():
        n = input("Введите целое число >>> ")
    return int(n)

def play(number, dict):
    right_counter = 0
    for n in range(number):
        country = random.choice(list(dict))
        user_input = input(f"Введите столицу государства {country} >>> ")      
        if user_input == dict.get(country, "Ошибка"):
            right_counter += 1
            print("Правлиьно!")
        else:
            print(f"Нет! Правильный ответ: {dict.get(country, 'Ошибка')}")

    return right_counter

if __name__ == "__main__":
    main()