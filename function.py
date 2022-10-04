from random import sample


def cr_nln():
    while True:
        try:
            num = int(input('введите цифру: '))
            if num > 0:
                list_num = sample(range(1, num * 2), num)
                return list_num
            return "Negative value of the number of numbers!"
        except ValueError:
            print('Это не число! Повторим: ')


print(cr_nln())
