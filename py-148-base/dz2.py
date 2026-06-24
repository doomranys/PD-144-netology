from typing import List

def fio(initials: List[str]) -> str:

    initials = (''.join(initials[0][0] + initials[1][0] + initials[2][0]))
    return initials


if __name__ == '__main__':
    assert fio(['Иванов', 'Иван', 'Иванович']) == 'ИИИ'
    assert fio(['Жан', 'Клот', 'Вандамович']) == 'ЖКВ'
    assert fio(['Павлов', 'Иван', 'Уралович']) == 'ПИУ'
    assert fio(['Семейный', 'Доминик', 'Торретович']) == 'СДТ'
    print("\nОтличная работа, отправляйте на проверку!")

fio = ['Иванов', 'Иван', 'Иванович']

print(fio[0][0] + fio[1][0] + fio[2][0])

fio = ''.join(fio[0][0] + fio[1][0] + fio[2][0])
print(fio)
