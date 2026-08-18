# main.py - базовая версия без faker
from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    """Основная функция программы"""
    print("=" * 50)
    print("ПРОГРАММА БУХГАЛТЕРИЯ")
    print("=" * 50)
    
    # Выводим текущую дату и время
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Текущая дата и время: {current_time}")
    print("-" * 50)
    
    # Вызываем функции
    salary = calculate_salary()
    employees = get_employees()
    
    print("-" * 50)
    print(f"Результат расчета зарплаты: {salary} руб.")
    print(f"Список сотрудников: {', '.join(employees)}")
    print("=" * 50)

if __name__ == '__main__':
    main()
