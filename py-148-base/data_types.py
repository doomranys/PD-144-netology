# Методы работы со списками

fruits_string = ['1', '2', '3', '4']
print(fruits_string)
fruits_string.append('berries')
print(fruits_string)
fruits_string.insert(2, 'cliff')
print(fruits_string)

berries = ['blackberry', 'raspberry']
fruits_string.extend(berries)
print(fruits_string)

# Удаление элементов

fruits_string.remove('2')
print(fruits_string)

fruits_string.pop()
print(fruits_string)
remove_fruit = fruits_string.pop(3)
print(remove_fruit)
print(fruits_string)

fruits_string.clear() # Очистка списка

# Функции для работы со списками

december_temps = [2.5, 3.5, 7.2, -4.0, -18.1]

print()
print(len(december_temps))
print(max(december_temps))
print(min(december_temps))
print(sum(december_temps))

# Ищем среднюю температуру

print()
print(sum(december_temps) / len(december_temps))

# Сортировка списков

fruit = ['cherry', 'cocos', 'apple', 'potato', 'berries', 'blackberry', 'raspberry']

print()
print(max(fruit))
print(min(fruit))
print('apple' < 'banana')
# print(sum(fruit)) # будет ошибка тк суммирование идет 0 int со строкой str

fruit.sort(reverse=True)
print(fruit)

# Вложенные списки

climates = [
    ['2000', '2001', '2002'],
    [5, 6, 7],
    [56, 54, 61]
]
print(climates)

nested_list = [
    1,
    2,
    True,
    'sad',
    [1, 2, [['Hello']]]
]
print(nested_list[-1])
print(nested_list[-1][-1][0][0][1])

# Создание копий списков

# Кортежи

# Кортежи изменять нельзя!!!

print()

empty_tupple = tuple()
print(empty_tupple)
one_element_tuple = (1, )
print(one_element_tuple)

fruit = ['cherry', 'cocos', 'apple', 'potato', 'berries', 'blackberry', 'raspberry']

fruits_tuple = tuple(fruit)
print(fruits_tuple)
print(fruits_tuple.index('cocos'))
print(fruits_tuple.count('potato'))
# fruits_tuple[0] = 'pear' # Будет ошибка

# Множественное присваивание (распаковка)

a, b, c = 3, 5, 9

print(a, c, b)

x = 1, 2, 3, 4 # Будет кортеж
print(type(x))

a, b, c, d, f = ['cherry', 'cocos', 'apple', 'potato', 'berries']
print(f'{a=}')
print(f'{b=}')
print(f'{c=}')
print(f'{d=}')
print(f'{f=}')
print()

a, b, *rest = ['cherry', 'cocos', 'apple', 'potato', 'berries']
print(f'{a=}')
print(f'{b=}')
print(f'{rest=}')
print()

*rest, a, b = ['cherry', 'cocos', 'apple', 'potato', 'berries']
print(f'{a=}')
print(f'{b=}')
print(f'{rest=}')
print()

a,  *rest, b = ['cherry', 'cocos', 'apple', 'potato', 'berries']
print(f'{a=}')
print(f'{b=}')
print(f'{rest=}')
print()

x = 5
y = 7
x, y = y, x
print(x, y)

# Кортежи/списки -> строки

fruits_str = 'cherry, cocos, apple, potato, berries'
print(fruits_str)
fruits = fruits_str.split(', ')
print(fruits)
new_fruits_str = '; '.join(fruits)
print(new_fruits_str)

# Функция ZIP

fruits = ('cherry', 'cocos', 'apple')
prises = [140, 200, 130]
counters = [10, 30, 44]
inventory = list(zip(fruits, prises, counters))
print(inventory)
print(inventory[-1])

# in и not in

list_1 = [1, 2, 3, 4]
print(1 in list_1)
print(6 in list_1)
print(1 not in list_1)
print(6 not in list_1)
