FED_TAX_RATE = 0.05
REG_TAX_RATE = 0.025

def main():
    purchase_amount = float(input("Введите сумму покупки >>> "))
    
    fed_tax = purchase_amount * FED_TAX_RATE
    reg_tax = purchase_amount * REG_TAX_RATE
    
    all_tax = reg_tax + fed_tax
    total = purchase_amount + all_tax
    
    print(f"Сумма покупки = {purchase_amount}\n" +
          f"Федеральный налог с покупки составил {fed_tax: .2f}\n" +
          f"Региональный налог с покупки составил {reg_tax: .2f}\n" +
          f"Общий налог с продаж составил {all_tax: .2f}\n" +
          f"Общая сумма - {total: .2f}.")

if __name__ == "__main__":
    main()
    