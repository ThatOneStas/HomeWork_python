def MyFunc(NumList):
    for i in NumList:
        print(i*i)

def PaliCheck(Text):
    if Text[::-1] == Text:
        print('Pali')
    else:
        print('Not palidrom')

def WordCalc(Text_2):
    print(len(Text_2.split()))

def Factorial(Num, a):
    for i in range(1, Num+1):
        a = a * i
    print(a)

def CesersShrift(Text_3, ShryftData, key=3):
    code_in_number = []
    for letter in Text_3:
        for l in ShryftData:
            if ShryftData[f"{l}"] == letter.lower():
                code_in_number.append(int(l) + int(key))
    print(code_in_number)
    code_word = ''
    for num in code_in_number:
        if num <= 26:
            code_word += ShryftData[f"{num}"]
        else:
            code_word += ShryftData[f"{num - 26}"]
    print(code_word)
    
NumList = [5,3,21,1]
MyFunc(NumList)
    
print('\n')
    
Text = input('Vvedit text palidrom: ')
PaliCheck(Text)
    
print('\n')
    
Text_2 = input('Vvedit text: ')
WordCalc(Text_2)
    
print('\n')
    
Num = int(input('Vvedit vashe chyslo: '))
a = 1
Factorial(Num, a)
    
print('\n')

key = 3
Text_3 = input('Vvedit vash text: ')
ShryftData = {"1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i", "10": "j", "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", "16": "p", "17": "q", "18": "r", "19": "s", "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", "25": "y", "26": "z"}
CesersShrift(Text_3, ShryftData)

#---------------------------------
    # усе що є вище! Є завданнями які я виконав на уроці 
    # вибачте що підвів так як:
    # 1. я не зробив завдання сортування злиттям так як не знаю що це
    # 2. я не зробив завдання з пошуку простих чисел так як не знаю як знаходити прості числа.
#---------------------------------

print('\n')

def PolishCalc(Pl_Num): # завдання з польським записом
    Pl_Num = Pl_Num.strip().split()
    if Pl_Num[0] == '+':    # зробив за умовами, інакше не знаю(
        print(int(Pl_Num[1])+int(Pl_Num[2]))
    elif Pl_Num[0] == '-':
        print(int(Pl_Num[1])-int(Pl_Num[2]))
Pl_Num = input('Введіть дію у вигляді польського запису: ')
PolishCalc(Pl_Num)

print('\n')

def ListAdder(MainList, List1, List2): # перетин списків
    for item in List1:  # відкриваємо 1-ий цикл а за ни 2-ий і додаєм об'єкти з них у пустий список MainList
        MainList.append(item)
    for item in List2:
        MainList.append(item)
    print(MainList)
MainList = []
List1 = [34, True, 'Yes']
List2 = [422, False, 'No']
ListAdder(MainList, List1, List2)