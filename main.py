# print('введите первое число')
# c = int(input())
# print(c)
# b = int(input('введите второе число: '))
# print (c + b)


# a=5.8945743
# b=6.4546922
# print(round(a*b,3))


# iter = 2
# iter += 3 # iter = iter +3
# iter -= 4 # iter = iter -4


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - ТОП')
# else:
#     print('Привет, ', username)


# a = 'qwerty'

# for i in a:
#     print(i)
    
    
# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))
# print('ещё' in text) # выводит true, если слово есть в строке, 
#                      # либо false если слова нет
# print(text.lower())  # переводит в нижний регистр
# print(text.upper())
# print(text.replace('ещё','снова')) # заменяет одно слово другим
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французких булок
# print(text[:2]) # съ
# print(text[len(text)-2]) # о
# print(text[2:9]) # ешь ещё 
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ЕШЬ ещёбСь
# print(text)




# def sum_numbers(n, y = 'Hello'):
    # summa = 0
    # print(y)
    # for i in range (1, n+1):
    #     summa += 1
    # return summa

# a = sum_numbers(5)
# print(a)

# def sum_str(*args):
#     res =''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q', 'e', 'l'))




# import modul1 # импортируем модуль напрямую
# print (modul1.max1(5,9))

# from modul1 import max1 - таким образом можно импортировать одтельную функцию (max1 в данном случае)
# print (max1(5,9)) - тогда вызываеть ее можно без обращения к конкретному файлу

# from modul1 import *   -  таким образом можно импортировать все функции из файла

# import modul1 as m1 #  импортируем наш модуль с сокращенным названием(просто чтобы меньше писать)
# print(m1.max1(10,9)) # функцию вызываем используя сокращенное название модуля





# def fib(n): # функция Фибоначи
#     if n in [1,2]: # базис функции
#         return 1
#     return fib(n-1)+fib(n-2)

# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print (list_1)




# def quick_sort(array): # сортировка разделением
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array [0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([10,5,2]))



# def merge_sort(nums):   # сортировка слиянием
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i +=1
#             else:
#                 nums[k] = right[j]
#                 j +=1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i +=1
#             k +=1
            
#         while j < len(right):
#             nums[k] = right [j]
#             j += 1
#             k += 1
            
# list1 = [1,5,6,7,9,0,7,5,3]
# merge_sort(list1)
# print(list1)