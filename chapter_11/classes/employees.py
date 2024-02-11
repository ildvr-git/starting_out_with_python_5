class Employee:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id


class ProductionWorker(Employee):

    def __init__(self, name, id, shift_num, rate):
        Employee.__init__(self, name, id)
        self.__shift_num = shift_num
        self.__rate = rate

    def get_shift_num(self):
        return self.__shift_num
    
    def get_rate(self):
        return self.__rate
    
    def set_shift_num(self, num):
        self.__shift_num = num

    def set_rate(self, rate):
        self.__rate = rate


class ShiftSupervisor(Employee):

    def __init__(self, name, id, anl_salary, anl_bonus):
        Employee.__init__(self, name, id)
        self.__anl_salary = anl_salary
        self.__anl_bonus = anl_bonus

    def get_annual_salary(self):
        return self.__anl_salary
    
    def get_annual_bonus(self):
        return self.__anl_bonus
    
    def __str__(self):
        result = \
            "Имя: " + str(self.get_name()) + "\n" + \
            "Номер: " + str(self.get_id()) + "\n" + \
            "Годовой оклад: " + str(self.get_annual_salary()) + "\n" + \
            "Годовая премия: " + str(self.get_annual_bonus())
        return result
        