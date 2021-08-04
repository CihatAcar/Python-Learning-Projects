HOUSE_PRICE = 1000000

good_credit = True

if good_credit:
   down_payment = HOUSE_PRICE - (HOUSE_PRICE * 10 / 100)
else:
    down_payment = HOUSE_PRICE - (HOUSE_PRICE * 20 / 100)

print(down_payment)