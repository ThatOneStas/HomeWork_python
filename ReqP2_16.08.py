# ---- Завдання 1 ----
def First():
    try:
        x = int(input('Введіть число: '))
        y = int(input('Введіть степінь: '))
        print(f"{x} ** {y} = {x**y}")
    except Exception as err:
        print("\nError 418")
# ---- Завдання 2 ----
def Second():
    def Checker(num):
        num_str = str(num)
        if num_str[0] == num_str[1] or num_str[0] == num_str[2] or num_str[1] == num_str [2]:
            return True
        else:
            return False
        
    Counter = 0
    for num in range(100, 1000):
        if Checker(num):
            Counter +=1
    print(f"К-сть цілих чисел з повторенням - {Counter}")
# ---- Завдання 3 ----
def Third():
    def Checker(num):
        num_str = str(num)
        if num < 1000:
            if num_str[0] == num_str[1] or num_str[0] == num_str[2] or num_str[1] == num_str [2]:
                return False
            else:
                return True
        elif num >= 1000:
            if num_str[0] == num_str[1] or num_str[0] == num_str[2] or num_str[0] == num_str[3] or num_str[1] == num_str [2] or num_str[2] == num_str[3]:
                return False
            else:
                return True    
        
    Counter = 0
    for num in range(100, 10000):
        if Checker(num):
            Counter +=1
    print(f"К-сть цілих чисел без повторення - {Counter}")
# ---- Завдання 4 ----
def Fourth():
    try:
        Number = int(input('Введіть число (цифри 3 і 6 будуть видалені): '))
        Number_str = str(Number)
        print(Number_str.replace('3','').replace('6',''))
    except Exception as err:
        print('\nError 418')
    
choice = input('Номер завдання(1-4):')
if choice == '1':
    First()
elif choice == '2':
    Second()
elif choice == '3':
    Third()
elif choice == '4':
    Fourth()
else:
    print('шо?')