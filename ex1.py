#Фунцкия zip() - объединение нескольких коллекций в один итератор(перечисляемый объект).
#В результате получается кортеж.

# Объединение двух списков
names = ['Аня', 'Борис', 'Сергей']
ages = [16, 14, 18, 16]

users = zip(names, ages) # упаковка
print(users) # итератор <zip object at 0x0000021E6AC2BF80>

for user in users:
    print(user) # ('Аня', 16) ('Борис', 14) ('Сергей', 18)

# Сразу в новый список

users = list(zip(names, ages)) # упаковка
print(users)

# С разной длинной:
names = ['Аня', 'Борис', 'Сергей']
ages = [16, 14, 18, 16]
cities = ['Минск', 'Витебск']
users = list(zip(names, ages, cities))
print(users)

# Объединение двух списков с оператором * (распоковка)
names, ages, cities = zip(*users)
print(names, ages, cities) #('Аня', 'Борис') (16, 14) ('Минск', 'Витебск')

# Объединение с множеством
numbers = [1, 2, 3] # список
letters = {'a', 'b', 'c'} # множество(отсутствует индекс коллекции)
zipped = list(zip(numbers, letters))
print(zipped) #[(1, 'b'), (2, 'a'), (3, 'c')]

# Предсказуемый результат с множеством - это функция sorted()
zipped = list(zip(numbers, sorted(letters)))
print(zipped)

# Объединение со словарями
a = {"x":1, "y":2, "z":3}
b = {"a":10, "b":20, "c":30}
print(list(zip(a, b))) # [('x', 'a'), ('y', 'b'), ('z', 'c')]

# доп. методы keys(), values()
users = {"Аня": 16, "Борис": 14, "Сергей":18}
print(list(zip(users.keys(), users.values()))) #[('Аня', 16), ('Борис', 14), ('Сергей', 18)]

# С помощью items() - ключ + значение
a = {"x":1, "y":2, "z":3}
b = {"a":10, "b":20, "c":30}
print(list(zip(a.items(), b.items())))
#[(('x', 1), ('a', 10)), (('y', 2), ('b', 20)), (('z', 3), ('c', 30))]








