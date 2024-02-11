from my_classes import Patient
from my_classes import Procedure
from datetime import date

def main():
    patient_1 = Patient("Тестовый Тест тестович", "ул. Пушкина, дом Колотушкина", "8-800-555-35-35", "Василий Брюкин, +70909091")
    proc_1 = Procedure("Врачебный осмотр", date.today(), "Ирвин", 250.00)
    proc_2 = Procedure("Рентгенография", date.today(), "Джемисон", 500.00)
    proc_3 = Procedure("Анализ крови", date.today(), "Smittie", 10.00)

    print(patient_1)
    print()
    print("Процедура 1")
    print(proc_1.show_info())
    print()
    print("Процедура 2")
    print(proc_2.show_info())
    print()
    print("Процедура 3")
    print(proc_3.show_info())
    print("~"*40)
    total_price = proc_1.get_cost() + proc_2.get_cost() + proc_3.get_cost()
    print("Общая стоимость всех процедур составляет: {}".format(total_price))

if __name__ == "__main__":
    main()