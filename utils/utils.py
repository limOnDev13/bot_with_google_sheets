"""
Модуль с утилитами - вспомогательными скриптами для работы бота
"""
from datetime import date
from typing import List


# Метод, который приводит к нормальному виду введенные даты
def make_right_date_format(str_date) -> date:
    list_str: List[str] = str_date.split('.')
    result_date: date

    if len(list_str) == 1:
        list_str.append(str(date.today().month))
    if len(list_str) == 2:
        list_str.append(str(date.today().year))

    result_date = date(day=int(list_str[0]), month=int(list_str[1]), year=int(list_str[2]))
    return result_date
