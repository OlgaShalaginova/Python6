# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена.
# enumerate, list comprehension

import os
os.system('cls')
import random

def main():
   k = int(input('Введите значение степени: '))
   mylist = [random.randint(0, 5) for i in range(k + 1)]
   print(mylist)
   res = ' + '.join([f'{el}*x^{i+1}' for i, el in enumerate(mylist[:-1]) if el != 0][::-1])
   if int(res[-1]) == 1:
      res = res[:-2]
   res = res + ' + ' + str(random.randint(1, 100)) + ' = 0' 
   print(res)

if __name__ == "__main__":
   main()