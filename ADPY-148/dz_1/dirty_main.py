# dirty_main.py
# Используем импорт всех функций с помощью *
from datetime import datetime
from application.salary import *
from application.db.people import *

def main():
    """Грязная версия основной программы"""
    print("=" * 50)
    print("ПРОГРАММА БУХГАЛТЕРИЯ (DIRTY VERSION)")
    print("=" * 50)
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Текущая дата и время: {current_time}")
    print("-" * 50)
    
    # Используем функции напрямую, без префиксов модулей
    salary = calculate_salary()
    employees = get_employees()
    
    print("-" * 50)
    print(f"Результат расчета зарплаты: {salary} руб.")
    print(f"Список сотрудников: {', '.join(employees)}")
    print("=" * 50)

if __name__ == '__main__':
    main()
