# ---- Завдання перше 1 ----

DayNum = int(input('Введіть номер дня тижня(1-7): '))
DayNum -= 1
DayList = [
    'Понеділок', 'Вівторок', 'Середа', 'Четверг', "П'ятниця", 'Субота', 'Неділя'
    ]
if DayNum < 0 or DayNum >= 7:
    print('Something went wrong.')
else:
    print(DayList[DayNum])

# ---- Завдання друге 2 ----

MonthNum = int(input('Введіть номер місяця(1-12): '))
MonthNum -= 1
MonthList = [
    'Січень', 'Лютий', 'Березень', 'Квітень', 
    'Травень', 'Червень', 'Липень', 'Серпень', 
    'Вересень', 'Жовтень', 'Листопад', 'Грудень'
    ]
if MonthNum < 0 or MonthNum >= 12:
    print('Something went wrong.')
else:
    print(MonthList[MonthNum])

# ---- Завдання третє 3 ----

Num1_3 = float(input('Input your number: '))
if Num1_3 < 0:
    print('Number is negative')
elif Num1_3 > 0:
    print('Number is positive')
elif Num1_3 == 0:
    print('Number is equal to zero')
else:
    print('Something went wrong.')

# ---- Завдання четверте 4 ----

Num1_4 = int(input('Input your first number: '))
Num2_4 = int(input('Input your second number: '))
if Num1_4 == Num2_4:
    print('Numbers are equal.')
else:
    print(min(Num1_4, Num2_4), max(Num1_4, Num2_4))