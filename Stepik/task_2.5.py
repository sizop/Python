# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну
# строку значения, которые встречаются в нём более одного раза.
#
# Для решения задачи может пригодиться метод sort списка.
#
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
#
# Sample Input 1:
#
# 4 8 0 3 4 2 0 3
# Sample Output 1:
#
# 0 3 4
# Sample Input 2:
#
# 10
# Sample Output 2:
#
# Sample Input 3:
#
# 1 1 2 2 3 3
# Sample Output 3:
#
# 1 2 3
# Sample Input 4:
#
# 1 1 1 1 1 2 2 2
# Sample Output 4:
#
# 1 2


list_num = list[input()]
list_num.sort()

list_out = []
for i in range(len(list_num)):
    if list_num[i] not in list_out and list_num.count(list_num[i]) > 1:
        list_out.append(list_num[i])
print(*list_out, sep=' ')
