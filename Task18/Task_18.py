goods = {'Хлеб': 24.3, 'Молоко': 88.7, 'Масло': 95.1, 'Вода': 15.5, 'Печенье': 35.1}
for good, price in goods.items():
    print(good, '-', price)
cost = 0
while True:
    good = input('Что хотите купить? (н - ничего)\n')
    if good == 'н':
       break
    else:
        good = good.capitalize()
    quantity = int(input('Сколько?\n'))
    cost += goods[good] * quantity
print('Общая цена покупки', cost)
