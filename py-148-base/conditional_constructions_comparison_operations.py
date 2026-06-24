# Повторяем основы

a = 10 + 5 * 3
b = a * 4
a = b - a
print (a)

# Операторы сравнения 

print(10 < 5)
print(10 > 5)
print(100 >= 100)
print(100 <= 50)

print(100 == 100)
print(100 != 100)

# Сравнение строк

print('A: ', ord('A'))

name_1 = 'Валя'
name_2 = 'Варя'

print(name_1 > name_2)

# Оператор тождественности is

a = "Олег"
b = "Тимур"
print(id(a)) # id - адрес в памяти
print(id(b))

# name_1 = input ("Введите первое имя: ")
# name_2 = input ("Введите второе имя: ")
 
# print( name_1 == name_2)
# print(id(name_1))
# print(id(name_2))
# print( name_1 is name_2)

a = 123123123
b = 123123123
print(a is b)

# Логические операторы AND OR NOT

print(2 > 1)
print(not (2 > 1))
print(True and True)
print(True and False)
print(False and False)
print()

print(True or True)
print(True or False)
print(False or False)


# Условные операторы

is_rainy = False
is_in_home = True

if is_rainy and is_in_home:
    print("Возьми зонт")
else:
    print("Ты будешь без зонта")

print("Конец программы")

# Тернарный оператор

num = int(input("Введите число: "))

print('четное') if num % 2 == 0 else print('нечетное')


# Високосный год

# 1) делится нацело на 4, но не делится на 100 (2004, 2080, 2100 – невисокосный)
# 2) делится нацело на 400 (2000, 1600, 800)

year = int(input("Введите год: "))

# 1 вариант

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("Високосный")
else:
    print("Невисокосный")

# 2 вариант

num = 8

if num == 1:
    print("ввели 1")
elif num == 2:
    print("ввели 2")
elif num == 3:
    print("ввели 3")
elif num == 4:
    print("ввели 4")
elif num == 5:
    print("ввели 5")
else:
    print("Я не знаю что вы ввели")

# pattern matching

language = "russian"

if language == "russian":
    print("Привет!")
elif language == "german":
    print("Hallo")
elif language == "england":
    print("Hello")
else:
    print("???")


match language:
    case "russian":
        print("Привет!")
    case "german":
        print("Hallo")
    case "england":
        print("Hello")
    case _:
        print("???")
