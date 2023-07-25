# ---- Завдання 1 ----
def Task1():
    def ListDobutok(NumList):
        a = 1
        for num in NumList:
            a *= num
        print(a)
    NumList = [1,7,5,10]
    ListDobutok(NumList)
    
    print('\n')
# ---- Завдання 2 ----
def Task2():
    def ListMin(NumList):
        print(min(NumList))
    NumList = [123,23,44,11]
    ListMin(NumList)
    
    print('\n')
# ---- Завдання 3 ----
def Task3():
    print('ОООооооОоО я незнаю як визначати простоту числа :)))00))0)')
    
    print('\n')
# ---- Завдання 4 ----
def Task4():
    def ListDel(NumList):
        DeletedList = []
        counter_4_1 = 0
        counter_4_2 = 3
        while counter_4_1 <= 2:
            print(NumList)
            Cond1_4 = int(input(f'Введіть порядковий номер числа який ви хочете видалити(доступно - {counter_4_2}): ')) -1
            for item in NumList:
                if Cond1_4 == NumList.index(item):
                    NumList.pop(Cond1_4)
                    DeletedList.append(item)
            counter_4_1 +=1
            counter_4_2 -=1
        print(f'Видалені елементи: {DeletedList}')
    NumList = [1,2,3,4,5,6,7,8,9,10]
    ListDel(NumList)
    
    print('\n')
# ---- Завдання 5 ----
def Task5():
    List5_1 = [22,33,88,55]
    List5_2 = [33,77,22,11]
    result = []
    def ItemEquality(List5_1,List5_2):
        Cond1_5 = True
        while Cond1_5:
            for item1 in List5_1:
                for item2 in List5_2:
                    if item1 == item2:
                        result.append(item1)
                        result.append(item2)
                        Cond1_5 = False
        print(result)
        print('Баг. Попробував флажком виправити, йому фіолетово')
    ItemEquality(List5_1,List5_2)
    
    print('\n')
# ---- Завдання 6 ----
def Task6():
    def StepinList(NumList):
        for num in NumList:
            result.append(num**2)
        print(result)
    NumList = [2,4,6,8]
    result = []
    StepinList(NumList)
    
    print('\n')
# --------------------
GlobalCond_1 = True
while GlobalCond_1:
    GlobalCond_2 = input('Введіть номер завдання (1-6) або N щоб закінчити огляд:\n(Буквам (окрім N) вхід заборонений )\n--> ')
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
    elif GlobalCond_2 == '5':
        print('\n')
        Task5()
    elif GlobalCond_2 == '6':
        print('\n')
        Task6()
    elif GlobalCond_2.lower() == 'n':
        GlobalCond_1 = False
    else:
        print('\nП0ПАВSЯ')
        GlobalCond_1 = False