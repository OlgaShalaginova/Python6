# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# enumerate

import os
os.system('cls')
import random

def main():
    my_list = [random.randint(0, 15) for el in range(random.randint(5, 10))]
    print('Список:', my_list)
    sum_odd_positions = [el for i, el in enumerate(my_list, 1) if not i % 2]
    print(f'На нечетных позициях находятся {sum_odd_positions} их сумма = {sum(sum_odd_positions)}')


if __name__ == '__main__':
    main()