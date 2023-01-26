# #1
# a=input("Введите целое число: ")
# if int(a) // 2:
#     print (True)
# else:
#     print (False)
# #2
# a = (1, 34, 56, 4, 9, 0, 67, 32, 54, 3)
# print(min(a), max(a))
# #3
# a ={1, 2, 3, 4, 5, 6}
# b = frozenset({1, 2, 5, 7, 9})
# c = a.union(b) #объединение
# print(c)
# d = a.intersection(b) #пересечение
# print(d)
# #4
# a = (45, 56, 7)
# print(max(a))
# #5
# a = float(input('Введите число: '))
# b = input('Операция: ')
# c = float(input('Введите второе число: '))
# if b == '+':
#     d = a + c
#     print("Результат:" + str(d))
# elif b == '-':
#     d = a - c
#     print(str(d))
# elif b == '*':
#     d = a * c
#     print(str(d))
# elif b == '/':
#     d = a/c
#     print(str(d))
# else:
#     print('Операция неверная')
#9
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in a:
#     if i < 5:
#         print(i)

#10
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [2, 3, 4, 7]
# for i in a:
#     for el in b:
#         if i == el:
#             print(i)


# a = (1, 2, 3, 4, 5, 6, 7, 8, 9 ,10)
# print(a[2])
# print(a[0:5])
# print(a[0:-2])
# for i in a:
#     if i % 2 == 0:
#        print(i)
# for i in a:
#     if i % 2 !=0:
#         print(i)
# print(a[::-1])
# print("Через один", a[::-2])
# print(len(a))

#21
# for i in range(1, 11):
#     print(i ** 2)

#22
# for i in range(15, 0, -1):
#     print(i)

#23
# a = 0
# mas = []
# while a < 98:
#     a += 7
#     mas.append(a)
# print(mas, len(mas))

#24
# a = 1
# b = 0
# while a < 50:
#     b += a
#     a += 1
# print(b)

#25
# a = [235, 32, 4, 34, 237]
# for i in a:
#     if i == 237:
#         break
#     elif i % 2 == 0:
#         print(i)

# 26
# a =[1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
# b = []
# for i in a:
#     if i not in b:
#        b.append(i)
#     elif i in b:
#        index = b.index(i)
#        del b[index]
# print(*b)

#27
# a =[1, 2, 3, 4, 5, 5, 6, 6]
# par = 0
# listpar = list()
# for i in a:
    
#         print(i)

#29
# a = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# b = (45, 21, 124, 76, 5, 23, 91, 234)
# if sum(a) > sum(b):
#     print(sum(a))
# elif sum(a) < sum(b):
#     print(sum(b))
# print(max(a), min(a), max(b), min(b))

#30
# a = [1, 2, 3, 4]
# def foo():
#     c = 0
#     for i in a:
#         c += i
#     print(c)
# foo()

#31
# a = int(input('введите год: '))
# def is_year_leap():
#     if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#         print(True)
#     else: 
#         print(False)
# is_year_leap()

#32
# a = int(input('Введите номер месяца(1-12)'))
# def season():
#     if a == 12 or a == 1 or a == 2:
#         print('зима')
#     elif a == 3 or a == 4 or a == 5:
#         print('весна')
#     elif a == 6 or a == 7 or a == 8:
#         print('лето')
#     elif a == 9 or a== 10 or a == 11:
#         print('осень')
#     else:
#         print('неправильный номер месяца')
# season()

#26
# a =[1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
# b = []
# for i in a:
#     for j in a:
#         if j ==i:
#             b.append(j)
# print(b)
        # print(b)
        # if i not in b:
        #    b.append(i)
    #     elif j in b:
    #         b.index(i)
    #     elif j == i:
    #         b.count(i)
    # print(b)
    
#         elif i in b:
#             index = b.index(i)
    
#             del b[index]
# print(*b)



# #36
# a =[1, 1, 2, 2, 3, 4, 5, 5, 6, 6]
# b = []
# for i in a:
#     index = a.index(i)
#     del a[index]
#     if i in a:
#         b.append(a)
# print(b)

#     if i not in b:

#        b.append(i)
#     elif i in b:
#        index = b.index(i)
#        del b[index]
# print(*b)



#35
# a = [1, 3, 2, 5, 4, 8, 6, 9, 7]
# a.sort()
# print(a)

#36
# from random import randint
# rot = lambda min, max: randint(min, max)
# print(rot(0, 100))

#37
# a = int(input('Введите число в км: '))
# f = 0.621371
# m = a * f
# print(m)

#38
# a = float(input('Введите любое число: '))
# if a > 0:
#     print('positive')
# elif a < 0:
#     print('Negative')
# elif a == 0:
#     print('zero')
# else: 
#     print('nothing')

#38(2)
# def foo(a):
#     if a > 0:
#         return('+')
#     elif a < 0:
#         return('-')
#     else:
#         return('0')
# print(foo(float(input('Введите любое число: '))))

#39
# def foo(a):
#     if a % 2 == 0:
#         return('chet')
#     elif a % 2 != 0:
#         return('nechet')
#     else:
#         return('nothing')
# print(foo(float(input('vvedite chislo'))))

#40
# def foo (a1, a2, a3):
#     if (a1 >= a2) and (a1 >= a3):
#         return a1
#     elif (a2 >= a1) and (a2 >= a3):
#         return a2
#     else:
#         return a3
# print(foo(1, 6, 3))

#41
# def foo(a):
#     for i in range(2, a):
#         if (a > 1) and (a % i == 0):
#              return True
#         elif a < 1:
#              return False
#         else:
#              return None
# print(foo(5))
   
#43
# def foo(a):
#     if a < 0:
#         print('false')
#     elif a < 2:
#         return a
#     return a * foo(a - 1)
# print(foo(6))

#44
# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 6, 5])))

#45
# a = [1, 2, 3, 4, 5, 6, 7]
# print('  '.join(map(str, a))) #join это перевод в строку
#45
# print(list(map(lambda x: x.join(), [1, 2, 3, 4, 5, 6]))) #неверный пример

#46
# b = list(filter(lambda x: x == x[::-1], ['ferref', 'frog', 'fof'] ))
# print(list(b))

#47
# import zipfile
# jangle_zip = zipfile.ZipFile ('C:\Users\Mi\Desktop\ test.zip')
# jangle_zip.extractall('C:\Users\Mi\Desktop')
# jangle_zip.close()


#открытие на чтение
# f = open('tt.txt', 'r')

# f = open('tt.txt')
# a = f.read(1)
# print(a)

#открытие на запись
# f = open('tt.txt', 'w')
# a = f.write('Hello Worllld')
# print(a)


#открытие на чтение
# f = open('tt.txt')
# for line in f:
#     print(line)



