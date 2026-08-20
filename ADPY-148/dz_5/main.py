import os
from datetime import datetime
import types

# ============ Декораторы ============

def logger(old_function):
    """Простой декоратор для логирования"""
    def new_function(*args, **kwargs):
        call_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join([f'{k}={repr(v)}' for k, v in kwargs.items()])
        
        if args_str and kwargs_str:
            all_args = f'{args_str}, {kwargs_str}'
        elif args_str:
            all_args = args_str
        elif kwargs_str:
            all_args = kwargs_str
        else:
            all_args = ''
        
        result = old_function(*args, **kwargs)
        
        log_entry = f'{call_time} - {old_function.__name__}({all_args}) -> {repr(result)}\n'
        
        with open('main.log', 'a', encoding='utf-8') as log_file:
            log_file.write(log_entry)
        
        return result
    
    return new_function

def logger_with_path(path):
    """Параметризованный декоратор для логирования в указанный файл"""
    def __logger(old_function):
        def new_function(*args, **kwargs):
            call_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            args_str = ', '.join([repr(arg) for arg in args])
            kwargs_str = ', '.join([f'{k}={repr(v)}' for k, v in kwargs.items()])
            
            if args_str and kwargs_str:
                all_args = f'{args_str}, {kwargs_str}'
            elif args_str:
                all_args = args_str
            elif kwargs_str:
                all_args = kwargs_str
            else:
                all_args = ''
            
            result = old_function(*args, **kwargs)
            
            log_entry = f'{call_time} - {old_function.__name__}({all_args}) -> {repr(result)}\n'
            
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(log_entry)
            
            return result
        
        return new_function
    
    return __logger


# ============ Тест 1: Простой логгер ============

def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path, encoding='utf-8') as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'
    
    print("✅ Тест 1 (простой логгер) пройден!")


# ============ Тест 2: Параметризованный логгер ============

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        # Удаляем старый лог файл
        if os.path.exists(path):
            os.remove(path)

        # Внутри цикла создаем функции для каждого пути
        @logger_with_path(path)
        def hello_world():
            return 'Hello World'

        @logger_with_path(path)
        def summator(a, b=0):
            return a + b

        @logger_with_path(path)
        def div(a, b):
            return a / b

        # Тестируем функции
        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)
    
    # Проверяем все логи
    for path in paths:
        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path, encoding='utf-8') as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'
    
    print("✅ Тест 2 (параметризованный логгер) пройден!")


# ============ Итератор из предыдущего ДЗ ============

class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_index = 0
        self.inner_index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.outer_index < len(self.list_of_list):
            inner_list = self.list_of_list[self.outer_index]
            
            if self.inner_index < len(inner_list):
                item = inner_list[self.inner_index]
                self.inner_index += 1
                return item
            else:
                self.outer_index += 1
                self.inner_index = 0
        
        raise StopIteration


# ============ Генератор из предыдущего ДЗ с логгером ============

@logger  # Применяем декоратор к генератору
def flat_generator(list_of_lists):
    for outer_list in list_of_lists:
        for item in outer_list:
            yield item


# ============ Применение логгера к функциям из предыдущего ДЗ ============

@logger
def test_flat_iterator():
    """Функция для тестирования итератора с логированием"""
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    
    result = list(FlatIterator(list_of_lists_1))
    return result


@logger_with_path('test_generator.log')
def test_flat_generator():
    """Функция для тестирования генератора с логированием в отдельный файл"""
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    
    result = list(flat_generator(list_of_lists_1))
    return result


def test_3():
    """Тестирование применения логгера к предыдущему ДЗ"""
    
    # Удаляем старые логи
    for log_file in ['main.log', 'test_generator.log']:
        if os.path.exists(log_file):
            os.remove(log_file)
    
    # Вызываем функции с логгерами
    result1 = test_flat_iterator()
    result2 = test_flat_generator()
    
    # Проверяем результаты
    expected = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert result1 == expected, "Результат итератора не совпадает с ожидаемым"
    assert result2 == expected, "Результат генератора не совпадает с ожидаемым"
    
    # Проверяем, что логи создались
    assert os.path.exists('main.log'), 'Файл main.log должен существовать'
    assert os.path.exists('test_generator.log'), 'Файл test_generator.log должен существовать'
    
    # Проверяем содержимое логов
    with open('main.log', encoding='utf-8') as f:
        main_log = f.read()
    
    with open('test_generator.log', encoding='utf-8') as f:
        gen_log = f.read()
    
    assert 'test_flat_iterator' in main_log, 'Имя функции должно быть в логе'
    assert 'test_flat_generator' in gen_log, 'Имя функции должно быть в логе'
    
    print("✅ Тест 3 (применение логгера к предыдущему ДЗ) пройден!")


if __name__ == '__main__':
    # Запускаем все тесты
    test_1()
    test_2()
    test_3()
    print("\n🎉 Все тесты успешно пройдены!")
