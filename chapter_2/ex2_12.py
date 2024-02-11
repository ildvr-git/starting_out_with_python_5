buy_price = 2000 * 40
buy_commission = buy_price * 0.03

sell_price = 2000 * 42.75
sell_commission = sell_price * 0.03

print(buy_price)
print(buy_commission)
print(sell_price)
print(sell_commission)
print((sell_price-sell_commission)-(buy_price+buy_commission))