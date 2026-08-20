import csv
import re
import os
from pprint import pprint

# 1. Функция для форматирования телефона
def format_phone(phone):
    if not phone:
        return ""
    
    phone = phone.strip()
    phone_pattern = r'(\+7|8)?\s*\(?(\d{3})\)?[\s\-]*(\d{3})[\s\-]*(\d{2})[\s\-]*(\d{2})'
    phone_match = re.search(phone_pattern, phone)
    
    if phone_match:
        formatted = f"+7({phone_match.group(2)}){phone_match.group(3)}-{phone_match.group(4)}-{phone_match.group(5)}"
        ext_pattern = r'доб\.?\s*(\d+)'
        ext_match = re.search(ext_pattern, phone, re.IGNORECASE)
        if ext_match:
            formatted += f" доб.{ext_match.group(1)}"
        return formatted
    return phone

# 2. Читаем правильный файл
try:
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
except FileNotFoundError:
    print("❌ Ошибка: файл phonebook_raw.csv не найден!")
    print("Текущая директория:", os.getcwd())
    print("Доступные файлы:", os.listdir())
    exit()

print("Исходные данные:")
pprint(contacts_list)
print("\n" + "="*80 + "\n")

# 3. Обрабатываем данные
header = contacts_list[0]
contacts = contacts_list[1:]
result = []

for contact in contacts:
    new_contact = contact.copy()
    
    # Нормализация ФИО с помощью среза и join
    full_name = ' '.join(new_contact[:3]).strip()
    name_parts = full_name.split()
    
    if len(name_parts) >= 1:
        new_contact[0] = name_parts[0]  # lastname
    if len(name_parts) >= 2:
        new_contact[1] = name_parts[1]  # firstname
    if len(name_parts) >= 3:
        new_contact[2] = name_parts[2]  # surname
    
    # Форматирование телефона
    if len(new_contact) > 5:
        new_contact[5] = format_phone(new_contact[5])
    
    result.append(new_contact)

# 4. Объединение дубликатов
unique_dict = {}
for contact in result:
    key = (contact[0].lower(), contact[1].lower())
    if key not in unique_dict:
        unique_dict[key] = contact
    else:
        existing = unique_dict[key]
        for i in range(len(contact)):
            if contact[i] and not existing[i]:
                existing[i] = contact[i]

final_contacts = [header] + list(unique_dict.values())

print("Обработанные данные:")
pprint(final_contacts)
print("\n" + "="*80 + "\n")

# 5. Сохраняем результат
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(final_contacts)

print(f"✅ Готово! Обработано {len(final_contacts) - 1} записей")
print("Результат сохранен в phonebook.csv")
print(f"Количество колонок: {len(header)}")
print(f"Заголовки: {', '.join(header)}")
