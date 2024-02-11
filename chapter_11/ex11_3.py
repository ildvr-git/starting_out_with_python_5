class Person:
    def __init__(self, name, address, tel):
        self.__name = name
        self.__address = address
        self.__tel = tel

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_address(self, value):
        self.__address = value

    def get_address(self):
        return self.__address

    def set_tel(self, value):
        self.__tel = value

    def get_tel(self):
        return self.__tel


class Customer(Person):
    def __init__(self, name, address, tel, mail_agree):
        Person.__init__(self, name, address, tel)
        self.__mail_agree = mail_agree

    def set_mail_agree(self, value):
        self.__mail_agree = value

    def get_mail_agree(self):
        return self.__mail_agree


def set_customer():
    name = input("Введите имя: ")
    address = input("Введите адрес: ")
    tel = input("Введите номер телефона: ")
    agree = input("Клиент согласен на получение уведомлений? >>> ")
    while agree.lower() != "да" and agree.lower() != "нет":
        agree = input("Клиент согласен на получение уведомлений? >>> ")
    if agree.lower() == "да":
        mail_agree = True
    else:
        mail_agree = False

    customer = Customer(name, address, tel, mail_agree)
    return customer

customer = set_customer()

agree_dict = {True: "Да", False: "Нет"}

print("Имя: ", customer.get_name(),
      "\nАдрес: ", customer.get_address(),
      "\nНомер телефона: ", customer.get_tel(),
      "\nСогласие: ", agree_dict[customer.get_mail_agree()])
