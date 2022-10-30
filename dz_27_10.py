# 1T
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
print(max(a, b, c))

# 2T
D = input("Что делаем? +, -, *, /: ")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if D == "+":
    c = a + b
    print("Результат: " + str(c))
elif D == "-":
    c = a - b
    print("Результат: " + str(c))
elif D == "*":
    c == a * b
    print("Результат: " + str(c))
elif D == "/":
    c == a / b
    print("Результат: " + str(c))
else:
    print("Операция выбрана неверно")

# first task
a = {}
b = a
c = b

print(id(a))
print(id(b))
print(id(c))

print(a)
print(b)
print(c)

# second task
d = {'a': 1}
e = {'a': 1}

print(id(d))
print(id(e))

print(d)
print(e)

# third task
d = e
print(id(d))
print(id(e))

a = {}
b = {}
c = {}
print(id(a))
print(id(b))
print(id(c))

# Fourth task
# D = int(input(" "))

# for i in range (''):
#     if i % 2 == 0:
#         print (str(i) + ' =четное')
#     else:
#         print (str(i) + ' =четное')