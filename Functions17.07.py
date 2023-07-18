# ---- Завдання перше 1 ----

def Citata(Text_pt1): # створюємо функцію і задаєм параметр з текстом
    print(Text_pt1.strip()) # на увазі відформатований я подумав що це текст з методом стріп якщо не правий сорі(
Text_pt1 = '"Don`t compare yourself with anyone in this world…\nif you do so, you are insulting yourself."\nBill Gates'
Citata(Text_pt1)    # у тексті у слові Don't я замінив ' на ` щоб номально зчитувало текст 
# ^^^ виводимо функцію та вказуємо параметр

print('\n')
# ---- Завдання друге 2 ----

def ParityChecker(Num1_2, Num2_2): # початок функції
    for Num in range(Num1_2, Num2_2+1): # +1 щоб включало 2 вказане число також
        if Num % 2 == 0: # умова
            print(f"{Num} is even.")
        else:   # умова x2
            print(f"{Num} isn't even.")
Num1_2 = int(input('Input first number: ')) # просимо користувача ввести два числа
Num2_2 = int(input('Input second number: '))
ParityChecker(Num1_2, Num2_2) # викликаємо функцію

print('\n')
# ---- Завдання третє 3 ----

# Напишіть функцію, яка відображає порожній або заповнений квадрат з певного символу. Функція приймає як параметри довжину сторони квадрата, символ і змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо — False, квадрат порожній.

# дуже мудро написано, може я тупий но я не розумія що від мене хоче завдання.

# ---- Завдання четверте 4 ----

def MinNum(NumList): # Функція - база
    print(min(NumList)) # виводить результат
NumList = [64664, 23441, 134511, 4646, 36245] # числа брав на рандом
MinNum(NumList) # ''призиваємо'' функцію.

print('\n')
# ---- Завдання п'яте 5 ----

    # я точно не знав що саме потрібно вивести проте думаю що це підійде :)
def Multiply(Num1_5, Num2_5):
    Condition = ''
    if Num1_5 >= Num2_5: # умова
        for num in range(Num2_5, Num1_5+1): # у циклі міняються межі діапазону
            Condition = 'and Num1 > Num2'
    elif Num1_5 < Num2_5: # ще одна умова
        for num in range(Num1_5, Num2_5+1): # у циклі міняються межі діапазону
            Condition = 'and Num2 > Num1'
    print(f"{Num1_5*Num2_5} {Condition}")
Num1_5 = int(input('Input first number: ')) # просимо користувача ввести два числа
Num2_5 = int(input('Input second number: '))
Multiply(Num1_5, Num2_5) # викликаємо функцію

print('\n')
# ---- Завдання шосте 6 ----  I hope my English is very good :))) *read with bad accent*

def FigChecker(Num1_6): # думаю що тут все зрозуміло
    print(len(Num1_6))
Num1_6 = input('input number: ') # нема int тому що int не має функції len.
FigChecker(Num1_6)

print('\n')
# ---- Завдання сьоме 7 ----

# можливо найпростіше тут завдання але поясню
def PaliCheck(Num1_7): # функцію
    Num1_7 = Num1_7.replace(' ','') # на всякій випадок забрав відступи
    if Num1_7 == Num1_7[::-1]: # умова якщо розвернуте число = простому числу то: ...
        print(f"{Num1_7} is palidrom")  # ...виводить що число є палідромом.
    else: # в іншому випадку число не палідромом
        print(f"{Num1_7} isn`t palidrom") 
Num1_7 = input('input number: ') # користувач вводить число
PaliCheck(Num1_7) # ну.. виводим.. так?