# Строки

# Объявление строк
str1 = "Строка 1"
str2 = 'Строка 2'
str3 = '''
Стройка3
Стройка4
Стройка5
Стройка6
'''
str3_1 = """
Стройка3
Стройка4
Стройка5
Стройка6
"""
print(str3)

str4 = ""

# длина строки
print(len(str1))

# доступ к отдельному символу
print(str1[0])# C
print(str1[-1])# 1

# изменить символ в строке нельзя

# перебор строк
# 1
for i in range(len(str1)):
    print(str1[i], end=", ")
print()
# 2
for s in str1:
    print(s, end=", ")
print()
# 3
list_str = [s for s in str1]
print(list_str)

