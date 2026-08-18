# application/db/people.py
from datetime import datetime

def get_employees():
    """Функция получения списка сотрудников"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Функция get_employees вызвана")
    print("Получение списка сотрудников...")
    return ["Иван Петров", "Мария Смирнова", "Алексей Иванов"]
