from my_classes import RetailItem

class CashRegister:
    def __init__(self):
        self.__lst = []
    
    def purchase_item(self, obj):
        self.__lst.append(obj)

    def get_total(self):
        result = 0
        for i in self.__lst:
            result += i.get_price()
        return result
    
    def show_items(self):
        for i in self.__lst:
            print(i)
            print()
            
    def clear(self):
        self.__lst = []

    def __str__(self) -> str:
        pass

def main():
    glass_1 = RetailItem("Стакан стекляный 200 мл.", 1, 1000)
    glass_2 = RetailItem("Стакан пластиковый 500 мл.", 1, 23)
    plate_1 = RetailItem("Тарелка плоская", 1, 430)
    spoon_1 = RetailItem("Ложка деревянная", 1, 1)
    items = [glass_1, glass_2, plate_1, spoon_1]
    print("Список товаров:")
    for i in items:
        print(i.get_description())
    
    cart = CashRegister()

    num = ""
    item_nums = []
    while num != "0":
        print("Введите номер товара, который " + \
              "хотите положить в корзину " + \
              "или введите 0, чтобы прекратить ввод")
        num = input(">>> ")
        while not num.isdigit() or len(items) < int(num) < 0:
            print("Номер товара введен неверно " + \
                  "попробуйте ещё раз!")
            num = input(">>> ")
        if num != "0":
            cart.purchase_item(items[int(num)-1])
    
    print("В корзину добавлены следующие товары: ")
    print()
    cart.show_items()
    print(f"Общая стоимость товаров в корзине {cart.get_total()}")

if __name__ == "__main__":
    main()