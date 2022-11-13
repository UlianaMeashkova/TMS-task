 #1
a = [1, 2, 4, 6, 7, 8, 6, 6, 3]
d = []
result = []
for i in a:
    if i not in d:
       d.append(i)
       result.append(i)
    else:
        if i in result:
            b = result.index(i)
            del result[b]
print(*result)

#2
par = 0
listOfPars = list()
inputList = list(input("Введите список чисел: ")) 

for i in inputList:
    inputListWithoutI = inputList[:]
    inputListWithoutI.remove(i)
    for j in inputListWithoutI:
        if i == j:
            listOfPars.append(i + j)
print(listOfPars)

for i in listOfPars:
    listOfParsWithoutI = listOfPars[:]
    listOfParsWithoutI.remove(i)

    for j in listOfParsWithoutI:
        if i == j:
            par += 1

print(par)

#3
C1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
C2 = (45, 21, 124, 76, 5, 23, 91, 234)
if sum(C1) >= sum(C2):
    print(sum(C2))
else:
    print(sum(C1))
print(C1.index(max(C1)) + 1, C2.index(max(C2)))
print(C1.index(min(C1)) + 1, C2.index (min(C2)))


#4
a = "An apple a day keeps the doctor away"
dict = {symbol: a.count(symbol) for symbol in a}  
print(dict)

#6
# list_1 = [1, 2, 3, 4, 5]    
# list_2 = [2, 3, 4, 5, 6]

#5
sweet_shop = {"Торт": [["мука","яйца","разрыхлитель","шоколад"], 6, 2000],
              "Пирожное": [["сахар","яйца","сметана","лимонный джем"], 3, 900],
              "Кекс": [["изюм","мука","яйца","разрыхлитель", "карамель"], 2, 1000]}
print('Здравствуйте. Что подсказать? Для выбора введите:"состав", "цена", "количество", '
      '"вся информация", "приступить к покупке"')
while True:
    a = input('Введите что вам подсказать: ')
    if a == "состав":
        for key, value in sweet_shop.items():
            print(key,'-',','.join(value[0]))
    if a == "цена":
        for key, value in sweet_shop.items():
            print(key,f'- {value[1]}р. за 100гр.')
    if a == "количество":
        for key, value in sweet_shop.items():
            print(key,f'- {value[2]} гр.')
    if a == "вся информация":
        for key, value in sweet_shop.items():
            print(f'\n {key}', '\nСостав:', ",".join(value[0]),
                  f'\nЦена: {value[1]}р. за 100гр.', f'\nКоличество: {value[2]} гр.')
    else:
        cost = 0
        while True:
            kond = input('Что вы хотите купить? "Торт", "Кекс", "Пирожное" или '
                             'введите n для завершения покупок')
            if kond == 'n':
                break
            gram = float(input('Сколько грамм вы хотите купить?'))
            if gram > sweet_shop[kond][2]:
                print("У нас столько нет, выберите другое количество или товар")
                continue
            cost = cost + (gram/100 * sweet_shop[kond][1])
            sweet_shop[kond][2] -= gram
        print(f"Вам надо заплатить {cost} р.")
    for key, value in sweet_shop.items():
        print(f'\n{key}', f'\nОсталось {value[2]} гр.')
    print("До свидания")