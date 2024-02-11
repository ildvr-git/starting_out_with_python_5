class Employee:
   
    def __init__(self, name, num):
        self.name = name
        self.__num = num


class ProductionWorker(Employee):

    def __init__(self, name, num, shift_num, rate):
        Employee.__init__(self, name, num)
        self.__shift_num = shift_num
        self.__rate = rate
        