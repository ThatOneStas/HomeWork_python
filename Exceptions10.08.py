# ---- Завдання 1 ----
def Task1():
    Factorial_Num = int(input('Введіть число для обчислення факторіалу: '))
    Factorial = 1
    try:
        if Factorial_Num <= 0:
            return 1/0
        else:
            for i in range(1, Factorial_Num+1):
                Factorial = Factorial * i
            print(f"Результат: {Factorial}.")
    except Exception as err:
        print('Число менше або дорівнює нулю.')
    
    print('\n')
# ---- Завдання 2 ----
def Task2():
    def FirstVer():     # - Перша Версія -
        def FactorialFunc(Factorial_Num,Factorial):
            for i in range(1, Factorial_Num+1):
                Factorial = Factorial * i
            print(f"Результат: {Factorial}.")
        
        Factorial_Num = int(input('Введіть число для обчислення факторіалу: '))
        Factorial = 1
        try:
            if Factorial_Num <= 0:
                return 1/0
            else:
                FactorialFunc(Factorial_Num,Factorial)
        except Exception as err:
            print('Число менше або дорівнює нулю.')
            
    def SecondVer():    # - Друга Версія -
        def FactorialFunc(Factorial_Num,Factorial):
            try:
                if Factorial_Num <= 0:
                    return 1/0
                else:
                    for i in range(1, Factorial_Num+1):
                        Factorial = Factorial * i
                    print(f"Результат: {Factorial}.")
            except Exception as err:
                print('Число менше або дорівнює нулю.')
            
            
        Factorial_Num = int(input('Введіть число для обчислення факторіалу: '))
        Factorial = 1
        FactorialFunc(Factorial_Num,Factorial)
        
    # --- Вибір версій (варіантів) ---    
    Task2_Cond = input('Виберіть версію 1 або 2: ')
    if Task2_Cond == '1':
        FirstVer()
    elif Task2_Cond == '2':
        SecondVer()
        
    print('\n')
# ---- Завдання 3 ----
def Task3():
    Num_List = input('Введіть список чисел. (приклад: 1 2 5 7...)').split()
    Close_Choice = True
    while Close_Choice != False:
        Cond_Choice = input('\nЩо ви бажаєте зробити(1-3, n - закінчити)?\n1) - Показати список\n2) - Отримати максимальне/мінімальне значення\n3) - Показати елемент за індексом\n4) - Видалити елемент за індексом\n--> ')
        try: 
            if Cond_Choice.lower() != 'n' or int(Cond_Choice) >= 5 or int(Cond_Choice) <= 0:
                return 1/0
        except Exception as err:
            print('Введене значення не правильне.')
        if Cond_Choice.lower() == 'n':
            Close_Choice = False
        elif Cond_Choice == '1':
            print(Num_List)
        elif Cond_Choice == '2':
            MinMax_Choice = input('Показати 1 - максимальне, 2 - мінімальне значення? - ')
            if MinMax_Choice == '1':
                print(f"Результат: {max(Num_List)}")
            elif MinMax_Choice == '2':
                print(f"Результат: {min(Num_List)}")
            else:
                print('Щось пішло не так :(')
        elif Cond_Choice == '3':
            El_index = int(input(f"Введіть номер елемента (1-{len(Num_List)}): "))-1
            try:
                print(f"Результат: {Num_List[El_index]}")
            except Exception as err:
                print('Індекс не знайдений.')
        elif Cond_Choice == '4':
            El_index = int(input(f"Введіть номер елемента (1-{len(Num_List)}): "))-1
            try:
                Num_List.pop(El_index)
                print(Num_List)
            except Exception as err:
                print('Індекс не знайдений.')
                
    print('\n')
# ---- Завдання 4 ----
def Task4():        
    
# --- Я не робив 2-ий варіант так як то було б дуже заплутано
    def First_Choice(Num_List):
        print(Num_List)
    def Second_Choice(Num_List):
        MinMax_Choice = input('Показати 1 - максимальне, 2 - мінімальне значення? - ')
        if MinMax_Choice == '1':
            print(f"Результат: {max(Num_List)}")
        elif MinMax_Choice == '2':
            print(f"Результат: {min(Num_List)}")
        else:
            print('Щось пішло не так :(')
    def Third_Choice(Num_List):
        El_index = int(input(f"Введіть номер елемента (1-{len(Num_List)}): "))-1
        try:
            print(f"Результат: {Num_List[El_index]}")
        except Exception as err:
            print('Індекс не знайдений.')
    def Fourth_Choice(Num_List):
        El_index = int(input(f"Введіть номер елемента (1-{len(Num_List)}): "))-1
        try:
            Num_List.pop(El_index)
            print(Num_List)
        except Exception as err:
            print('Індекс не знайдений.')
    Num_List = input('Введіть список чисел. (приклад: 1 2 5 7...)').split()
    Close_Choice = True
    while Close_Choice != False:
        Cond_Choice = input('\nЩо ви бажаєте зробити(1-3, n - закінчити)?\n1) - Показати список\n2) - Отримати максимальне/мінімальне значення\n3) - Показати елемент за індексом\n4) - Видалити елемент за індексом\n--> ')
        try: 
            if Cond_Choice.lower() != 'n' or int(Cond_Choice) >= 5 or int(Cond_Choice) <= 0:
                return 1/0
        except Exception as err:
            print('Введене значення не правильне.')
        if Cond_Choice.lower() == 'n':
            Close_Choice = False
        elif Cond_Choice == '1':
            First_Choice(Num_List)
        elif Cond_Choice == '2':
            Second_Choice(Num_List)
        elif Cond_Choice == '3':
            Third_Choice(Num_List)
        elif Cond_Choice == '4':
            Fourth_Choice(Num_List)
    
    print('\n')
# --------------------
GlobalCond_1 = True
while GlobalCond_1:
    GlobalCond_2 = input('Введіть номер завдання (1-4) або N щоб закінчити огляд:\n(Буквам (окрім N) вхід заборонений )\n--> ')
    if GlobalCond_2 == '1':
        print('\n')
        Task1()
    elif GlobalCond_2 == '2':
        print('\n')
        Task2()
    elif GlobalCond_2 == '3':
        print('\n')
        Task3()
    elif GlobalCond_2 == '4':
        print('\n')
        Task4()
    elif GlobalCond_2.lower() == 'n':
        GlobalCond_1 = False
    else:
        print('\nП0ПАВSЯ')
        GlobalCond_1 = False