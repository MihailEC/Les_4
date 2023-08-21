"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


def victorin(condition, quest_vict, vict_conditionr=None):
    while vict_conditionr != condition:
        vict_conditionr = victorin_quest(quest_vict, condition)

def victorin_quest(quest, answer):
    data = int(input(quest))
    if data == answer:
        print('Верно!')
    else:
        print('Неверно!')
    return data



victorin(1799, 'Введите год рождения А.С. Пушкина: ')
victorin(6, 'Введите день рождения: ')


