# 1. Напишите программу, которая принимает на вход число N и выдаёт 
# последовательность из N членов.
    
#     *Пример:*
 #     - Для N = 5: 1, -3, 9, -27, 81

# import random
# def my_random(n):
# 	b = []
# 	for i in range (n):
# 		b.append(random.randint(0,100)) #все границы включаются
# 	return b
# number = int(input('Введите число '))
# # m = my_random(number)
# print(my_random(number))

# Второе решение

# from random import randint

# for _ in range(int(input('ведите число: '))):
# 	print(randint(0,100), end=' ')

# 2. Для натурального n создать словарь индекс-значение, состоящий 
# из элементов последовательности 3n + 1.
    #     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int (input('введите число: '))
# my_dict=[]
# for i in range(1,n+1):
# 	my_dict.append([i, 3 * i + 1])
# print(dict(my_dict)) #dict создаем словарь и печатаем

# n = int(input("Введите число n: "))
#     my_dict = {}
#     for i in range(1, n):
#         my_dict = {'ID': i, 'Value': 3 * i + 1}
#         print(my_dict)

# 3. Напишите программу, в которой пользователь будет задавать 
# две строки, а программа - определять количество вхождений 
# одной строки в другой.

text1 = input('введите 1 строку:')
text2 = input('введите 2 строку:')
for i in range(len(text1)):


