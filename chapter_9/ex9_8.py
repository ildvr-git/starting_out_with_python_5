import pickle
# import io

def main():
    try:
        file = open(f"chapter_9\data\emails.dat", "rb")
        emails = pickle.load(file)
        file.close()
    except IOError:
        print("Файл с контактами не найден. Создан пустой словарь.")
        emails = {}

    user_end = False
    while not user_end:
        user_choise = choose()    
        if user_choise == "1":
            emails = add_email(emails)
        if user_choise == "2":
            find(emails)
        if user_choise == "3":
            delete_email(emails)
        if user_choise == "4":
            show_all(emails)
        if user_choise == "5":
            user_end = True
    print("Завершение работы программы.")
    file = open(f"chapter_9\data\emails.dat", "wb")
    pickle.dump(emails, file)
    file.close()

def choose():
    print("Выберите действие:")
    print("1 - Добавить новый адрес;\n" + \
          "2 - Найти адрес по имени пользователя;\n" + \
          "3 - Удалить адрес;\n" + \
          "4 - Посмотреть весь список;\n" + \
          "5 - Выйти из программы")
    user_choise = input(">>> ")
    while not user_choise.isdigit() or int(user_choise) < 1 \
    or int(user_choise) > 5:
        print("Некорректный ввод, попробуйте ещё раз")
        user_choise = input(">>> ")
    return user_choise

def add_email(dict):
    name = input("Введите имя контакта >>> ")
    email = input("Введите E-mail >>> ")
    print()
    dict[name] = email
    return dict

def find(dict):
    print("Введите имя контакта, который хотите найти")
    search = input(">>> ")
    print()
    print(dict.get(search, "Контакт с таким именем не найден"))
    print()

def delete_email(dict):
    print("Введите имя контакта, которого хотите удалить")
    search = input(">>> ")
    print()
    try:
        del dict[search]
        print(f"Контакт {search} успешно удален")
        print()
    except KeyError:
        print(f"Контакт {search} не найден!")
        print()

def show_all(dict):
    for k, v in dict.items():
        print(k, " - ", v)

if __name__ == "__main__":
    main()