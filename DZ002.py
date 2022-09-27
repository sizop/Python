# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#
# Пример:
# # - 6782 -> 23
# - 0,56 -> 11

# sum = int(0)
# number = float(input('Введите число: '))
# if number < 0:
#     number = number * -1
# str_number = str(number)
# number = number * (10 ** (abs(str_number.find('.') - len(str_number)) - 1))
# print(number)
# while number % 10 > 0:
#     sum += number % 10
#     number = number // 10
# print(int(sum))

# Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
#
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# result = 1
# str = []
# number = int(input('Введите число: '))
# for i in range(1, number + 1):
#     result = result * i
#     str += [result]
# print(str)


# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

# Пример:
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

# str = []
# number = int(input('Введите число: '))
# for i in range(1, number + 1):
#     result = round(((1 + 1 / i) ** i))
#     str += [result]
# print(f'{str} -> {sum(str)}')

# * 4. Напишите программу, которая принимает на вход 2 числа.
#  Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#   Найдите произведение элементов на указанных позициях(не индексах).

# number_elements = int(input("Введите количество элементов: "))
# first_element = -number_elements
# while True:
#     try:
#         pos_first_element = int(input("Введите позицию первого элемента: "))
#         pos_second_element = int(input("Введите позицию второго элемента: "))
#         if 0 <= pos_first_element <= number_elements * 2 + 1 and 0 <= pos_second_element <= number_elements * 2 + 1:
#             break
#         else:
#             print('Эти цифры вне диапазона! Повторим:')
#     except ValueError:
#         print('Это не число! Повторим:')
# list = []
# for i in range(number_elements * 2 + 1):
#     list += [first_element]
#     first_element += 1
# print(list)
# print(f'Произведение заданных элементов {int(list[pos_first_element - 1]) * int(list[pos_second_element - 1])}')


# Реализуйте алгоритм перемешивания списка.

# import random
#
# list_1 = list(range(1, 11))
# list_out = []
# print(f'Исходный список: {list_1}')
# for i in range(1, 11):
#     rnd = random.choice(list_1)
#     list_out += [rnd]
#     list_1.remove(rnd)
# print(f'Перемешанный список:{list_out}')
