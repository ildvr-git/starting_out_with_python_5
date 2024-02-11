class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, type):
        self.__animal_type = type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age

class Car:
    def __init__(self, y_model, make):
        self.__year_model = y_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
    
class Information:
    def __init__(self, name, adress, age, phone):
        self.__name = name
        self.__adress = adress
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_adress(self, adr):
        self.__adress = adr

    def set_age(self, age):
        self.__age = age

    def set_phone(self, number):
        self.__phone = number

    def get_name(self):
        return self.__name
    
    def get_adress(self):
        return self.__adress
    
    def get_age(self):
        return self.__age
    
    def get_phone(self):
        return self.__phone
    
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

class RetailItem:
    def __init__(self, description, qty, price):
        self.__description = description
        self.__qty = qty
        self.__price = price

    def get_description(self):
        return self.__description
    
    def get_qty(self):
        return self.__qty
    
    def get_price(self):
        return self.__price
    
    def set_description(self, desc):
        self.__description = desc

    def set_qty(self, qty):
        self.__qty = qty

    def set_price(self, price):
        self.__price = price
    
    def __str__(self):
        result = \
            self.get_description() + "\n" + \
            str(self.get_qty()) + "\n" + \
            str(self.get_price())
        return result
    
class Patient:
    def __init__(self, full_name, adress, tel, extra_contact):
        self.__full_name = full_name
        self.__adress = adress
        self.__tel = tel
        self.__extra_contact = extra_contact
    
    def get_name(self):
        return self.__full_name
    def get_adress(self):
        return self.__adress
    def get_tel(self):
        return self.__tel
    def get_extra_contact(self):
        return self.__extra_contact
    
    def set_name(self, name):
        self.__full_name = name
    def set_adress(self, adress):
        self.__adress = adress
    def set_tel(self, n):
        self.__tel = n
    def set_extra_contact(self, n):
        self.__extra_contact = n

    def __str__(self):
        result = \
        "full_name: " + str(self.get_name()) + "\n" + \
        "adress: " + str(self.get_adress()) + "\n" + \
        "tel: " + str(self.get_tel()) + "\n" + \
        "extra_contact: " + str(self.get_extra_contact())
        return result
    
class Procedure:
    def __init__(self, name, date, doctor_name, cost):
        self.__name = name
        self.__date = date
        self.__doctor_name = doctor_name
        self.__cost = cost
    
    def get_name(self):
        return self.__name
    def get_date(self):
        return self.__date
    def get_doctor_name(self):
        return self.__doctor_name
    def get_cost(self):
        return self.__cost
    
    def set_name(self, name):
        self.__name = name
    def set_date(self, date):
        self.__date = date
    def set_doctor_name(self, doctor_name):
        self.__doctor_name = doctor_name
    def set_cost(self, cost):
        self.__cost = cost
    
    def show_info(self):
        result = \
        "Название процедуры: {}".format(self.get_name()) + "\n" + \
        "Дата: {}".format(self.get_date()) + "\n" + \
        "Врач: {}".format(self.get_doctor_name()) + "\n" + \
        "Стоимость: {}".format(self.get_cost())
        return result
    
