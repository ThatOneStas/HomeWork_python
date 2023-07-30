# ---- Завдання 1 ----
def Task1():
    Name = input('''Введіть ваше ім'я: ''')
    Age = int(input('Введіть ваш вік:'))
    try: 
        if Age < 0 or Age > 130:
            return 1/0
        else:
            print(f"Привіт, {Name}! Твій вік — {Age}")
    except Exception as err:
        print('Такого віку бути не може!')
        
            
    print('\n')
# ---- Завдання 2 ----
def Task2():
    
    def FirstVer():
        
        def InnerFirst(Name, Age):
            print(f"Привіт, {Name}! Твій вік — {Age}") 
            
        Name = input('''Введіть ваше ім'я: ''')
        Age = int(input('Введіть ваш вік:'))
        try: 
            if Age < 0 or Age > 130:
                return 1/0
            else:
                InnerFirst(Name, Age)
        except Exception as err:
            print('Такого віку бути не може!')
            
    def SecondVer():
        
        def InnerSecond(Name, Age):
            try: 
                if Age < 0 or Age > 130:
                    return 1/0
                else:
                    print(f"Привіт, {Name}! Твій вік — {Age}")
            except Exception as err:
                print('Такого віку бути не може!')
            
        Name = input('''Введіть ваше ім'я: ''')
        Age = int(input('Введіть ваш вік:'))
        InnerSecond(Name, Age)
        
    Task2_Cond = input('Виберіть версію 1 або 2: ')
    if Task2_Cond == '1':
        FirstVer()
    elif Task2_Cond == '2':
        SecondVer()
    
    print('\n')
# ---- Завдання 3 ----
def Task3():
    NumList = input('Введіть набір додатніх чисел через пробіл,\nПриклад - (1 2 5 7)\n-->').split()
    result = 0
    Task3Cond = True
    
    try:
        for num in NumList:
            if int(num) < 0:
                return 1/0
    except Exception as err:
        print('''Одне з чисел від'ємне!''')
        Task3Cond = False
    if Task3Cond == True:
        for num in NumList:
            result += int(num)
        print(result)
        
    print('\n')
# ---- Завдання 4 ----
def Task4():
    def FirstVer():
        def InnerFirst(NumList):
            result = 0
            if Task3Cond == True:
                for num in NumList:
                    result += int(num)
                print(result)
        NumList = input('Введіть набір додатніх чисел через пробіл,\nПриклад - (1 2 5 7)\n-->').split()
        Task3Cond = True
        try:
            for num in NumList:
                if int(num) < 0:
                    return 1/0
        except Exception as err:
            print('''Одне з чисел від'ємне!''')
            Task3Cond = False
        if Task3Cond != False:
            InnerFirst(NumList)
    def SecondVer():
        def InnerSecond(NumList):
            result = 0
            Task3Cond = True
            try:
                for num in NumList:
                    if int(num) < 0:
                        return 1/0
            except Exception as err:
                print('''Одне з чисел від'ємне!''')
                Task3Cond = False
            if Task3Cond == True:
                for num in NumList:
                    result += int(num)
                print(result)
        NumList = input('Введіть набір додатніх чисел через пробіл,\nПриклад - (1 2 5 7)\n-->').split()
        InnerSecond(NumList)
            
    Task2_Cond = input('Виберіть версію 1 або 2: ')
    if Task2_Cond == '1':
        FirstVer()
    elif Task2_Cond == '2':
        SecondVer()
    
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