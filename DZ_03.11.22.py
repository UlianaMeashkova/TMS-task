#1
a = input("Введите 7-ое число: ")
cht = 0
n_cht = 0
summ = 0
for i in a:
    summ = int(i) + summ
    if int(i) % 2 == 0:
        cht += 1
    if int(i) % 2 != 0:
        n_cht += 1
if cht > n_cht:
    print("Сумма: ", summ)
else: 
    pr = int(a[0]) * int(a[2]) * int(a[5])
    print("Произведение: ", pr)

#2
a = input("python: ")
count_vow = 0
count_cons = 0
vow = ""
cons = ""

for i in a:
    letter = i.lower()
    if letter == "a" or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
        count_vow += 1
        vow += letter 
    else:
        count_cons += 1
if count_vow == count_cons:
   print(vow) 

#3
from random import randint
result = 0
iteration_four_value_c = 0
iteration_four_value_d = 0
a: int = int(input('a ='))
b: int = int(input('b ='))
input_sum = a + b 
for i in range(7): #range = 0, 1, 2, 3, 4, 5, 6
    c: int = randint(1, 20)
    d: int = randint(1, 20)
    if i == 3:
        iteration_four_value_c = c
        iteration_four_value_d = d
    rand_sum_1 = c + d
    rand_sum_2 = iteration_four_value_c + iteration_four_value_d
    if input_sum > rand_sum_1:
        result += 1
    elif input_sum == rand_sum_2 and i >= 3:
        print(iteration_four_value_c, iteration_four_value_d)
print(result)
       
#4 не решила

# import random as randint 
# a =int(input("Size: "))
# find=input("Find: ")
# # b: int = randint(0, 9) 
# for i in range(a):
#     b = randint(0, 9) 
# print(b)
# print(b.count(find))

#5
s = input("Введите строку: ")
l = len(s)
integ = []
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))
 
print(integ)

#6
text = input("Введите текст: ")
pair_lower = 0
pair_upper = 0
for i in range(1, len(text)):
    print(text[i - 1], text[i])
    if text[i - 1].islower() and text[i].islower():
        pair_lower += 1
    if text[i - 1].isupper() and text[i].isupper():
        pair_upper += 1
print('Cколько пар верхнего регистра:', pair_upper)
print('Cколько пар нижнего регистра:', pair_lower)