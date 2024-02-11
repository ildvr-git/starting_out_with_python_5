TIPS_RATE = 0.18
TAX_RATE = 0.07

def get_price():
    return float(input("Введите стоимость еды в чеке >>> "))

def get_add_expences(price, rate):
    return price * rate

def main():
    food_price = get_price()
    tips = get_add_expences(food_price, TIPS_RATE)
    tax = get_add_expences(food_price, TAX_RATE)

    total = food_price + tips + tax

    print("Общая сумма составила {:.2f}\n".format(total) +
          "Из них:\n" +
          "чаевые - {:.2f}\n".format(tips) +
          "налоги - {:.2f}".format(tax))

main()
