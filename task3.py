# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# map, lambda 

import os
os.system('cls')
import random

def main():
   leng = int(input('Введите размер: '))
   my_L = [float(random.randint(100, 999))/100 for _ in range(leng)]
   print(my_L)
   my_L = list(map(lambda x: x%1, my_L))
   print(f'Разница между максимальным значением {round(max(my_L), 2)} и минимальным значением {round(min(my_L), 2)}  равна {round(max(my_L) - min(my_L), 3)}')

if __name__ == "__main__":
   main() 