# print('Hello World!')
# print('Привет, ребята!')



# Арифметические операции

# print(17 + 25)      # это операция сложения
# print(11 - 4)
# print(13 * 7)
# print(8 ** 3)
# print(-8)
# print(------8)
# print(82 / 5)
# print(82 // 5)
# print(82 % 5)
# # 82 => 5 * 16 + 2
#
# # приоритет операций https://pythonru.com/uroki/29-prioritetnost-i-associativnost-operatorov-dlja-nachinajushhih
# print(2 + 2 * 2)
# print((2 + 2) * 2)


# print(17.4 + 24.6)
# print(11.3 - 4)
# print(13.1 * 7)
# print(8.0 ** 3)
# print(-8.0)
# print(------8.1)
# print(82 / 5.0)
# print(82 // 5.0)
# print(82.3 % 5)
# # 82 => 5 * 16 + 2
#
# print(2.0 + 2 * 2)
# print((2 + 2.1) * 2)
# print(0.1 + 0.1 + 0.1)



# Переменные

# # print(cat_name)
# cat_name = 'Уличный кот'
# cat_age = 5
# cat_weight = 5.5
#
# cat_2_age = 6
# _num1er = 234
# # 1_number = 345    # нельзя начинать с цифры
#
# print('Этого кота зовут', cat_name)
# print('Я его подобрал')
# cat_name = 'Леви'
# print('И теперь его зовут', cat_name)
#
# print('Моему коту', cat_age, 'лет')
# cat_age = cat_age + 1
# print('Моему коту', cat_age, 'лет')
# cat_age += 5          # cat_age = cat_age + 1
# print('Моему коту', cat_age, 'лет')



# функция print

# print(234)
# print('dfghdrhdr')
# print(2 + 2, 10 // 3, 'Привет')

# s = 'Это первая строка\nЭто вторая строка'
# print(s)
# print('Всем', 'привет.', 'Меня', 'зовут', 'Тимур', sep='~~~')
# print(1, 345, 'dfghfd', sep='!')
# print(123, end='\n')
# print(345, end='!!\n??')
# print(567)
# print(1, 2, 3, 4, sep='~', end='!!!')
# print('продолжение строки')

# name = "Моя любимая книга \"Д'Артаньян и три мушкетера\""
# print(name)



# функция input()

# name = input('Введите ваше имя: ')
# print('Вас зовут', name)
# age = input('Сколько Вам лет: ')
# print('Вам', age, 'лет')


# distance = 800
# speed = input('С какой скоростью (км/ч) ты едешь? ')
# time = distance / speed
# print('ты проведешь в дороге', time, 'часов')


# print(type('100'))
# print(type(100))
# print(type(100.0))



# # print('Тебе ' + 38 + ' лет')  # ошибка
# print('Тебе ' + '38' + ' лет')
# print('hello' * 3)
# print(2 * 'hello')
# print('-' * 50)
#
# greeting = 'Hello World!'
# print(greeting[0])
# print(greeting[-12])
# print(greeting[6])
# print(greeting[-6])
# print(greeting[11])
# print(greeting[-1])
#
# # методы строк https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
#
# print('-' * 50)
# print(len(greeting))
# print(greeting.lower())
# print(greeting.upper())
# new_greeting = greeting.upper()
# print(greeting)
# print(new_greeting)
# print(greeting.find('World'))
# print(greeting.find('world'))
# print(greeting.replace('Hello', 'Goodbye'))


# int_str = '123'
# float_str = '42.13242'
# int_number = int(int_str)
# float_number = float(float_str)
#
# # print(type(int_str))
# # print(type(int_number))
# print(int_number * 3)
# print(float_number + 1)
#
# age = 39
# print("тебе " + str(age) + " лет")


# distance = 800
# speed = int(input('С какой скоростью (км/ч) ты едешь? '))
# time = distance / speed
# print('ты проведешь в дороге', time, 'часов')
# print('ты проведешь в дороге ' + str(time) + ' часов')
#
# answer = f'ты проведешь в дороге {distance / speed} часов'
# print(answer)


name = input('Как тебя зовут? ')
age = int(input('Сколько тебе лет? '))
print(f'{name}, ты родился в {2025 - age} году')



# книга https://ozon.ru/t/cskqfRR
# задачи - http://hackerrank.com/
# задачи - https://www.codewars.com/
