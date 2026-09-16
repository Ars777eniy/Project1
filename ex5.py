# Случайные велечины random и округление
import random
import math
from random import shuffle

from ex1 import cities

# random()
print(random.random())

# randint() случайное целое в диапозоне
print(random.randint(1, 10))

# uniform() случайное дробное в диапозоне
n = random.uniform(1.5, 10.99)
print(n)

# округление с функцией round()
print(round(n)) # до целого
print(round(n, 2)) # до 2 знаков после запятой

# floor() до целого меньшего
print(math.floor(n))

# ciel() до целого большего
print(math.ceil(n))

# randrange() случайное с шагом
print(random.randrange(0, 100, 10))

# choise() случайный элемент из списка
cities1 = ["Париж","Рим","Токио","Нью-Йорк","Минск"]
print(random.choice(cities1))

# choises() случайные элементы из списка с повторением
print(random.choices(cities1, k = 5))

# sample() случайные элементы из списка без повторения
print(random.sample(cities1, 5))

# shuffle() перемешивание элементов
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Задача сгенерировать 5 случайных целых чисел от 1 до 10
list_gen = [random.randint(0, 10) for n in range(5)]
print(list_gen)



