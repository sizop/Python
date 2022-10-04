# def check(str_list):
#     for i, num in enumerate(str_list):
#         str_list[i] = num.strip('.,;:?!')
#         if not str_list[i].replace("-", "").isdigit():
#             return []
#     return str_list
#
#
# def find_max_min(nums_str: str):
#     list_nums = nums_str.split()
#     right_list = check(list_nums)
#
#     if right_list:
#         return min(right_list, key=int), max(right_list, key=int)
#     else:
#         print("The data is incorrect")
#         return []
#
#
# print(*find_max_min(input("Enter the numbers separated by a space: ")))

# from math import sqrt
#
# print("Введите коэффициенты квадратного уравнения")
# a = float(input("а = "))
# b = float(input("b = "))
# c = float(input("c = "))
#
# d = b**2 - 4 * a*c
# sqrtd = sqrt(d)
#
# with open("temp.txt", "a", encoding="utf-8") as output:
#     output.write(f"уравынение: {a}*x^2 + {b}*x + {c}\n")
#     if d > 0 and a:
#         x1 = (-b + sqrtd) / (2*a)
#         x2 = (-b - sqrtd) / (2*a)
#         output.write(f"корни уравнения: {x1, x2 }\n")
#     elif (int(d)) == 0:
#         x = -b / (2*a)
#         output.write(f"единственный корень: {x}\n")
#     else:
#         output.write("корней нет")

# from math import gcd
#
#
# print("Введите два числа: ")
# a = int(input("a = "))
# b = int(input("b = "))
#
# def nok (first, second):
#     return(first*second) // gcd(first, second)
# print(nok(a,b))

#decimal модуль для дробных чисел

