from ex10_4 import Employee
import io
import pickle

FILE = "chapter_10\data\employees.dat"

class ChoiceCode:
# Пункты главного меню:
    SEARCH = "1"
    ADD = "2"
    EDIT = "3"
    DELETE = "4"
    QUIT = "5"

def main():
    try:
        in_file = io.open(FILE, mode="rb")
        emp_dict = pickle.load(in_file)
        print(
            "\nФайл загружен."
        )
    except IOError:
        print(
            "Файл словаря не найдён! ",
            "Создаю новый словарь.", "\n"
        )
        emp_dict = {}

    choice = get_choice()
    while choice != ChoiceCode.QUIT:
        match choice:
            case ChoiceCode.SEARCH:
                find_emp(emp_dict)
                choice = get_choice()
            case ChoiceCode.ADD:
                emp_dict = add_emp(emp_dict)
                choice = get_choice()
            case ChoiceCode.EDIT:
                emp_dict = edit_emp(emp_dict)
                choice = get_choice()
            case ChoiceCode.DELETE:
                emp_dict = delete_emp(emp_dict)
                choice = get_choice()
    
    save_dat(emp_dict)
    print()
    print("~~~Выход из программы~~~\n")
                
def get_choice():
    print(
        "Для выбора действия введите цифру:",
        "\n",
        "\n1 - Найти сотрудника;",
        "\n2 - Добавить сотрудника;",
        "\n3 - Изменить данные сотрудника",
        "\n4 - Удалить сотрудника;",
        "\n5 - Выйти из программы."
    )
    result = input("\n>>> ")
    while not result.isdigit or 5 < int(result) < 1:
        print(
            "Для выбора действия введите цифру,", 
            "соответствующую действию!"
        )
        result = input("\n>>> ")
    return result

def find_emp(dct):
    print()
    print("Введите номер для поиска")
    id = input(">>> ")
    try:
        employee = dct[id]
        print(employee)
        print()
        print("Выберите действие с найденным сотрудником: ")
        print(
            "1 - Изменить;",
            "\n2 - Удалить;",
            "\n3 - Выйти в главное меню"
        )
        choice = input(">>> ")
        while not choice.isdigit or 3 < int(choice) < 1:
            print(
                "Для выбора действия введите цифру,", 
                "соответствующую действию!"
            )
            choice = input("\n>>> ")
        if choice == "1":
            dct = edit_emp(dct, id)
        elif choice == "2":
            dct = delete_emp(dct, id)
        else:
            print()
            print("~~~Выход в главное меню~~~\n")
    except KeyError:
        print("Сотрудник с таким номером не найден\n")
      
def add_emp(dict):
    print()
    print("Введите имя сотрудника")
    name = input(">>> ")
    print()
    print("Введите номер сотрудника")
    id = input(">>> ")
    print()
    print("Введите отдел")
    dept = input(">>> ")
    print()
    print("Введите должность сотрудника")
    position = input(">>> ")

    employee = Employee(name, id, dept, position)
    dict[id] = employee

    return dict

def edit_emp(dct, id=None):
    print()
    if not id:
        print(
            "Введите номер сотрдуника, данные которого хотите изменить"
        )
        id = input(">>> ")
    try:
        employee = dct[id]
        print(employee)

        print()
        print("Введите новое имя сотрудника")
        name = input(">>> ")
        print()
        print("Введите новый отдел сотрудника") 
        dept = input(">>> ")
        print()
        print("Введите новую должность сотрудника")
        position = input(">>> ")

        employee = Employee(name, id, dept, position)
        dct[id] = employee

        return dct
    except KeyError:
        print("Сотрудник с таким номером не найден")

def delete_emp(dct, id=None):
    print()
    if not id:
        print(
            "Введите номер сотрудника, которого хотите удалить"
        )
        nmb = input(">>> ")
    try:
        del dct[nmb]
        return dct
    except KeyError:
        print(
            "Сотрудник с таким номером не найден!", \
            "Попробуйте ещё раз!"
        )

def save_dat(dict):
    try:
        out_file = io.open(FILE, mode="wb")
        pickle.dump(dict, out_file)
        out_file.close()
        print(
            "\nФайл успешно сохранен!"
        )
    except:
        print(
            "При сохранении файла произошла неизвестная ошибка!"
        )

if __name__ == "__main__":
    main()