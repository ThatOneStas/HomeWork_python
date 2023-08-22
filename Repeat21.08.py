# ---- Завдання 2 ----

import random 
def TASK2():
    num_list = []
    info_dict = {
        'above_zero': 0,
        'below_zero': 0,
        'zero': 0
    }

    random_numbers_quant = random.randint(1,10)

    for num in range(0, random_numbers_quant+1):
        random_number = random.randint(-100,100)
        num_list.append(random_number)
    
    for num in num_list:
        if num > 0:
            info_dict['above_zero'] += 1
        elif num < 0:
            info_dict['below_zero'] += 1
        elif num == 0:
            info_dict['zero'] += 1
        
    print(f"{num_list}\nДодатні - {info_dict['above_zero']}\nВідємні - {info_dict['below_zero']}\nНулі - {info_dict['zero']}")
    
# ---- Завдання 1 ----
def TASK1():
    print(eval(input("Введіть вираз: ")))
    # Згадав що можна зробити калькулятор в 1 рядок коду,
    # тут рішає функція eval яка сприймає рядок як команду, що й може виконувати математичні операції.
    # Але на ній можна також й кодити, це вже може бути небезпечно так як деякі конди можуть нашкодити...
    # роботі програми та інше.
    
# --------------------
user_choice = input("Введіть номер Завдання (1, 2): ")
if user_choice == '1':
    TASK1()
elif user_choice == '2':
    TASK2()
else:
    print('шо')