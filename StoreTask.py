UserBalance = 100
Products = {
    "Яблука": 10,
    "Банани": 15,
    "Апельсини": 12,
    "Груші": 8,
    "Киві": 20 
}
ShoppingCart = {}
TF = True
TF2 = False
while TF:
    print(Products)
    Cond = input(f"Який товар ви хочите придбати? (Ваш баланс-{UserBalance}): ").replace(' ','').capitalize()
    for items in Products.copy():
        if Cond == items:
            if UserBalance > Products[Cond]:
                UserBalance -= Products[Cond]
                del Products[Cond]
                ShoppingCart[Cond] = ''
                print('\nТовар додано до кошика.\n')
            else:
                print('\nНедостатньо коштів для покупки данного товару.\n')
        elif Cond.lower() == 'q':
            TF = False
#        else:        не працює і я не знаю чому саме
#            print('Товар не знайдено.')
print(f"\nВаш кошик: {ShoppingCart}\nЗалишок: {UserBalance} грн.")