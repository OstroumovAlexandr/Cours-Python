# Задача № 2
# Найти сумму цифр трехзначного числа

# print('Введите трехзначное число: ')
# n = input()
# a = 0
# a = int(n[0]) + int(n[1]) + int(n[2])
# print('Сумма цифр числа', n, 'равна',a)


# Задача № 4
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
#   6 -> 1  4  1
#   24 -> 4  16  4
#   60 -> 10  40  10

# print('Введите общее количество журавликов, сделанных детьми: ')
# n = int(input())
# if(n % 6 != 0):
#     print('Число должно быть кратным 6')
# else:
#     a = int(n / 6)
#     b = int(a * 4)
#     print('Петя и Сережа сделали по', a, 'журавликов, а Катя сделала', b, 'журавликов')


# Задача № 6
# Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#   *Пример:*
#   385916 -> yes
#   123456 -> no

# print('Введите шестизначный номер билета:')
# n = input()
# a = int (n[0]) + int (n[1]) + int(n[2])
# b = int (n[3]) + int (n[4]) + int(n[5])
# print(a,b)
# if (len(n) != 6):
#     print('Надо было ввести ШЕСТЬ цифр')
# elif a == b:
#     print('Билет с номером', n, 'счастливый')
# else:
#     print('В другой раз повезет')



# Задача №8
# Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой 
# между дольками (то есть разломить шоколадку на два прямоугольника).
#   *Пример:*
#   3 2 4 -> yes
#   3 2 1 -> no

# print('Введите количество долек шоколадки в ширину:')
# n = int(input())
# print('Введите количество долек шоколадки в длину:')
# m = int(input())
# print('Сколько долек будем отламывать?')
# k = int(input())
# if((k % n == 0) or (k % m == 0) and (k < n * m)):
#     print('Такой кусочек можно отломить')
# else:
#     print('Такой кусочек отломить НЕЛЬЗЯ')

