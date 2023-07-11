# ---- Завдання перше 1 ----

Num1 = int(input('Input first number: ')) # берем числа
Num2 = int(input('Input second number: '))
for Nums in range(Num1, Num2): # робимо діапазон
    if (Nums % 7) == 0: # ставим умову за якої числа які при ділені з 7 мають в остачі 0 будуть виводитися на екран.
        print(Nums," ", end="") # показуємо результат
        
print('\n')
# ---- Завдання друге 2 ----
Num1_2 = int(input('Input first number: '))
Num2_2 = int(input('Input second number: '))
for Nums_2 in range(Num1_2, Num2_2 + 1):        # тут був присутній баг в якому воно з`їдало останнє число,  
    print(Nums_2, " ", end="")                  # прийшлось добавити до другого числа одиницю.
print('\n')
for Nums_2_Inv in range(Num2_2, Num1_2 - 1, -1):  # тут був присутній баг в якому воно з`їдало перше число,
    print(Nums_2_Inv, " ", end="")                # прийшлось відняти від першого числа одиницю.
print('\n')
for Nums_2_2 in range(Num1_2, Num2_2):
    if (Nums_2_2 % 7) == 0:
        print(Nums_2_2," ", end="") # я не знав як відділити їх,
    if (Nums_2_2 % 5) == 0:         # так що воно показує кратні числа і 7 і 5 разом.
        print(Nums_2_2," ", end="") # я не хотів робити більше циклів аби відділити їх.
print('\n')
# ---- Завдання третє 3 ----

Num1_3 = int(input('Input first number: ')) # берем числа
Num2_3 = int(input('Input second number: '))
for Nums_3 in range(Num1_3, Num2_3): # робимо діапазон
    if (Nums_3 % 3) == 0: 
        print("Fizz")       # кожному задаєм свою умову і виводим результат
    if (Nums_3 % 5) == 0:
        print("Buzz")
    if (Nums_3 % 3) == 0 and (Nums_3 % 5) == 0:
        print("Fizz Buzz")
    if (Nums_3 % 3) > 0 and (Nums_3 % 5) > 0:
        print(Nums_3)