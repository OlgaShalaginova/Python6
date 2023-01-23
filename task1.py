# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# filter, lambda 

import os
os.system('cls')
import random

def main():
   mylist = sorted([random.randint(1, 9) for i in range(10)])
   print('Первоначальная последовательность:', mylist)
   x = list(filter(lambda x: mylist.count(x) == 1, mylist))
   print('Неповторяющиеся элементы:', x)

if __name__ == '__main__':
    main()