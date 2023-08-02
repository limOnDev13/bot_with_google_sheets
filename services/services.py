"""
Модуль с реализацией бизнес-логики.
"""
import gspread
from gspread import Worksheet
from typing import List, Any
from datetime import datetime, date

from utils.utils import make_right_date_format


gc = gspread.service_account(
    filename='mytestpythonproject-394706-4cc29a499b41.json'
)
sh = gc.open("Test_table")


def _get_worksheet(sheet_num: int) -> Worksheet:
    gc = gspread.service_account(
        filename='mytestpythonproject-394706-4cc29a499b41.json'
    )
    sh = gc.open("Test_table")
    return sh.worksheet(sheet_num)


def _create_text(input_table: List[dict]) -> str:
    result: str = ''

    for row in input_table:
        text_row: str = ''
        for elem in row:
            text_row += str(row[elem]) + '_'

        text_row = text_row[:-1] + '\n'
        result += text_row

    return result


def name_ticker_share() -> str:
    result_table: List[dict[str, Any]] = []
    worksheet: Worksheet = _get_worksheet(0)
    column_names: set[str] = {'Наименование', 'Тикер', 'Доля в портфеле'}

    table: List[dict[str, Any]] = worksheet.get_all_records()

    for row in table:
        result_row: dict[str, Any] = dict()

        for key in column_names:
            result_row[key] = row[key]

        result_table.append(result_row)

    return _create_text(result_table)


def branch_share() -> str:
    result_table: List[dict[str, Any]] = []
    worksheet: Worksheet = _get_worksheet(1)
    column_names: set[str] = {'Отрасль', 'Доля'}

    table: List[dict[str, Any]] = worksheet.get_all_records()

    for row in table:
        result_row: dict[str, Any] = dict()

        for key in column_names:
            result_row[key] = row[key]

        result_table.append(result_row)

    return _create_text(result_table)


def name_ticker_profit(input_dates: str) -> str:
    # Обозначим переменные
    result_table: List[dict[str, Any]] = []
    worksheet: Worksheet = _get_worksheet(0)
    column_names: set[str] = {'Дата', 'Наименование', 'Тикер', 'Доход в процентах'}

    # Переведем введенные даты в тип datetime
    list_str_dates: List[str] = input_dates.split(' ')
    dates: set[date] = set()

    for str_date in list_str_dates:
        if ':' in str_date:
            str_date_range: List[str] = str_date.split(':')
            start_date: date = make_right_date_format(str_date_range[0])
            end_date: date = make_right_date_format(str_date_range[1])
            day: date = start_date

            while day <= end_date:
                dates.add(day)
        else:
            day: date = make_right_date_format(str_date)

            dates.add(day)

    # Заполним таблицу необходимыми данными
    table: List[dict[str, Any]] = worksheet.get_all_records()

    for row in table:
        result_row: dict[str, Any] = dict()
        day: date = datetime.strptime(row['Дата'], "%d.%m.%Y")

        if day in dates:
            for key in column_names:
                result_row[key] = row[key]

        result_table.append(result_row)

    result_text: str = _create_text(result_table) + 'Всего доход %%: ' + str(worksheet.get('E2'))

    return result_text
