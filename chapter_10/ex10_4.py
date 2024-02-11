class Employee:
    emp_lst = []

    def __init__(self, name, id, department, position):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__position = position
        Employee.emp_lst.append(self)
            
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_pos(self):
        return self.__position
    def get_dept(self):
        return self.__department

    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def set_pos(self, pos):
        self.__position = pos
    def set_dept(self, dept):
        self.__department = dept
    def __str__(self):
        result = \
            "Имя: " + self.get_name() + "\n" + \
            "ID: " + self.get_id() + "\n" + \
            "Отдел: " + self.get_dept() + "\n" + \
            "Должность: " + self.get_pos()
        return result
    def display_table_view(self):
        result = \
            f"{self.get_name(): ^14}" + \
            f"{self.get_id(): ^10}" + \
            f"{self.get_dept(): ^16}" + \
            f"{self.get_pos(): ^14}"
        print(result)

def main():
    vice_pres = \
        Employee("Сьюзан Мейерс", "47899", "Бухгалтерия", "Вице-президент")
    dev = \
        Employee("Марк Джоунс", "39119", "IТ", "Программист")
    engineer = \
        Employee("Джой Роджерс", "81774", "Производственный", "Инженер")

    print(f"{'Имя': ^14}{'ID': ^10}{'Отдел': ^16}{'Должность': ^14}")
    print("~"*54)

    for worker in Employee.emp_lst:
        # print(worker)
        worker.display_table_view()
    
if __name__ == "__main__":
    main()