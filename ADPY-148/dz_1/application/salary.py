# application/salary.py
from datetime import datetime

def calculate_salary():
    """Функция расчета зарплаты"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Функция calculate_salary вызвана")
    print("Выполняется расчет заработной платы...")
    return 50000  # просто возвращаем какое-то значение
