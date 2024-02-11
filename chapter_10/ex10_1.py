import my_classes as c

def main():
    name = input("Введите имя зверушки >>> ")
    a_type = input("Введите тип зверушки >>> ")
    age = input("Сколько зверушке лет? >>> ")

    my_pet = c.Pet(name, a_type, age)

    print(f"Зверушке типа {my_pet.get_animal_type()} {my_pet.get_age()} лет и зовут её {my_pet.get_name()}")

if __name__ == "__main__":
    main()
    