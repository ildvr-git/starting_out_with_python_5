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
    
def main():
    person_1 = Information("John", "Moscow", 23, "8-800-555-35-35")
    person_2 = Information("Jack Snow", "Paris", 73, "8-800-545-35-35")
    person_3 = Information("Johnathan", "Not Moscow", 21, "8-800-GET-FOOD")

    for p in [person_1, person_2, person_3]:
        print(f"{p.get_name()} lives in {p.get_adress()}")
    print()

    print(person_1.get_name() == person_3.get_name())
    person_1.set_name(person_3.get_name())
    print(person_1.get_name() == person_3.get_name())

if __name__ == "__main__":
    main()
