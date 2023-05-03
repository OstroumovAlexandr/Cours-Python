# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def amplif(a,b): 
    if b == 1: # базис функции
        return a
    elif b == 0:
        return 1
    else:
        return a * amplif(a, b -1)

num = int(input('Введите число А: '))
exp = int(input('Введите степень В: '))

print ("Число", num, " в степени", exp, "равно", amplif(num, exp))